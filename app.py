from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mail import Mail,Message
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    logout_user,
    current_user
)
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_
from itsdangerous import URLSafeTimedSerializer

import os
import re


# =============================
# App Configuration
# =============================

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_super_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///users.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# =============================
# Mail Configuration (SMTP)
# =============================
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = "Please login to continue"
login_manager.login_message_category = "error"

# Token serializer for password reset
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# =============================
# Database Model
# =============================

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#============================
# Password Strength Validation
#============================

def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True


# =============================
# Routes
# =============================

@app.route('/')
def home():
    return render_template("base.html")


# =============================
# Register
# =============================
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    # Check if username exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        flash("Username already exists!", "error")
        return redirect(url_for('home'))

    # Check if email exists
    existing_email = User.query.filter_by(email=email).first()
    if existing_email:
        flash("Email already registered!", "error")
        return redirect(url_for('home'))
    
    if not is_strong_password(password):
        flash("Password must be strong!", "error")
        return redirect(url_for('home'))

    # Hash password
    hashed_password = generate_password_hash(password)

    # Create new user
    new_user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    flash("Account created successfully!", "success")
    return redirect(url_for('home'))


# =============================
# Login (Email or Username)
# =============================

@app.route('/login', methods=['POST'])
def login():
    identifier = request.form.get("identifier")
    password = request.form.get("password")

    # Check if identifier is email or username and query accordingly
    user = User.query.filter(or_(User.username == identifier, User.email == identifier)).first()

    if user and check_password_hash(user.password, password):
        login_user(user)
        return redirect(url_for('dashboard'))
    else:
        flash("Invalid username or password!", "error")
        return redirect(url_for('home'))


# =============================
# Dashboard (Protected)
# =============================

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")


# =============================
# Logout
# =============================

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.", "success")
    return redirect(url_for('home'))


# =============================
# Forgot Password
# =============================

mail = Mail(app)
@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get("email")
        user = User.query.filter_by(email=email).first()
        if user:
            token = serializer.dumps(email, salt="reset-password")
            reset_link = url_for(
                'reset_password',
                token=token,
                _external=True
            )
            msg = Message(
                "Password Reset Request",
                sender="iamgroot130204@gmail.com",
                recipients=[email]
            )
            msg.body = f"Click the link to reset your password: {reset_link}"

            msg.html = f"""
            <h2>Password Reset Request</h2>
            <a href="{reset_link}">Reset Password</a>
            """
            print("MAIL USER:", app.config['MAIL_USERNAME'])
            print("MAIL PASS:", app.config['MAIL_PASSWORD'])
            
            mail.send(msg)
            flash("Password reset link sent to your email!", "success")
        else:
            flash("Email not Found!", "error")
        return redirect(url_for('home'))
    return render_template("forgot_password.html")

# =============================
# Reset Password
# =============================

@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        email = serializer.loads(token, salt="reset-password", max_age=600)
    except:
        flash("Reset link expired or invalid!", "error")
        return redirect(url_for('home'))
    if request.method == 'POST':
        password = request.form.get("password")
        if not is_strong_password(password):
            flash("Password must be strong!", "error")
            return redirect(request.url)
        
        user = User.query.filter_by(email=email).first()
        if not user:
            flash("User not found!", "error")
            return redirect(url_for('home'))
        
        user.password = generate_password_hash(password)
        db.session.commit()
        flash("Password reset successful!", "success")
        return redirect(url_for('home'))
    return render_template("reset_password.html")


# =============================
# Run App
# =============================

with app.app_context():
    db.create_all()

# Vercel needs this to run the app
app = app