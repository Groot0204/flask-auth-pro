from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    logout_user,
)
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_
from itsdangerous import URLSafeTimedSerializer
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
load_dotenv()

import os
import re

# =============================
# App Configuration
# =============================

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "dev-secret-key")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///database.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# =============================
# Mail Configuration
# =============================

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

# =============================
# Login Manager
# =============================

db = SQLAlchemy(app)
mail = Mail(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = "Please login to continue"
login_manager.login_message_category = "error"

# =============================
# Token Serializer
# =============================

serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# =============================
# OAuth Configuration
# =============================

oauth = OAuth(app)

google = oauth.register(
    name='google',
    client_id= os.environ.get("GOOGLE_CLIENT_ID"),
    client_secret = os.environ.get("GOOGLE_CLIENT_SECRET"),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)

github = oauth.register(
    name='github',
    client_id = os.environ.get("GITHUB_CLIENT_ID"),
    client_secret=os.environ.get("GITHUB_CLIENT_SECRET"),
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'}
)

# =============================
# Database Model
# =============================

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# =============================
# Password Validation
# =============================

def is_strong_password(password):
    return (
        len(password) >= 8
        and re.search(r"[A-Z]", password)
        and re.search(r"[a-z]", password)
        and re.search(r"[0-9]", password)
        and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    )

# =============================
# Routes
# =============================

@app.route('/')
def home():
    return render_template("base.html")

# =============================
# Register + Email Verification
# =============================

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    if User.query.filter_by(username=username).first():
        flash("Username already exists!", "error")
        return redirect(url_for('home'))

    if User.query.filter_by(email=email).first():
        flash("Email already registered!", "error")
        return redirect(url_for('home'))

    if not is_strong_password(password):
        flash("Password must be strong!", "error")
        return redirect(url_for('home'))

    user = User(
        username=username,
        email=email,
        password=generate_password_hash(password)
    )

    db.session.add(user)
    db.session.commit()

    # 🔐 Send verification email
    token = serializer.dumps(email, salt="email-verify")
    verify_link = url_for('verify_email', token=token, _external=True)

    msg = Message(
        "Verify Your Email",
        sender=app.config['MAIL_USERNAME'],
        recipients=[email]
    )

    msg.html = f"""
    <h2>Email Verification</h2>
    <p>Click below to verify your account:</p>
    <a href="{verify_link}">Verify Email</a>
    """

    print("Mail system initialized")

    mail.send(msg)

    flash("Check your email to verify your account before login.", "success")
    return redirect(url_for('home'))

# =============================
# Verify Email
# =============================

@app.route('/verify-email/<token>')
def verify_email(token):
    try:
        email = serializer.loads(token, salt="email-verify", max_age=3600)
    except:
        flash("Verification link expired or invalid!", "error")
        return redirect(url_for('home'))

    user = User.query.filter_by(email=email).first()

    if user:
        user.is_verified = True
        db.session.commit()
        flash("Email verified successfully!", "success")

    return redirect(url_for('home'))

# =============================
# Login
# =============================

@app.route('/login', methods=['POST'])
def login():
    identifier = request.form.get("identifier")
    password = request.form.get("password")

    user = User.query.filter(
        or_(User.username == identifier, User.email == identifier)
    ).first()

    if user and check_password_hash(user.password, password):

        if not user.is_verified:
            flash("Please verify your email first!", "error")
            return redirect(url_for('home'))

        login_user(user)
        return redirect(url_for('dashboard'))

    flash("Invalid username or password!", "error")
    return redirect(url_for('home'))

# =============================
# Dashboard
# =============================

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")

# =============================
# Forgot Password
# =============================

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get("email")
        user = User.query.filter_by(email=email).first()

        if user:
            token = serializer.dumps(email, salt="reset-password")
            reset_link = url_for('reset_password', token=token, _external=True)

            msg = Message(
                "Password Reset",
                sender=app.config['MAIL_USERNAME'],
                recipients=[email]
            )

            msg.html = f"""
            <h2>Password Reset</h2>
            <a href="{reset_link}">Reset Password</a>
            """

            mail.send(msg)
            flash("Reset link sent!", "success")
        else:
            flash("Email not found!", "error")

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
        flash("Reset link expired!", "error")
        return redirect(url_for('home'))

    if request.method == 'POST':
        password = request.form.get("password")

        if not is_strong_password(password):
            flash("Weak password!", "error")
            return redirect(request.url)

        user = User.query.filter_by(email=email).first()

        if user:
            user.password = generate_password_hash(password)
            db.session.commit()
            flash("Password updated!", "success")

        return redirect(url_for('home'))

    return render_template("reset_password.html")

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
# OAuth: Google
# =============================

@app.route('/login/google')
def google_login():
    return google.authorize_redirect(url_for('google_callback', _external=True))


@app.route('/callback/google')
def google_callback():
    token = google.authorize_access_token()
    user_info = google.get('https://www.googleapis.com/oauth2/v3/userinfo').json()
    print("TOKEN:", token)

    email = user_info.get("email")
    username = user_info.get("name")

    user = User.query.filter_by(email=email).first()

    if not user:
        user = User(
            username=username,
            email=email,
            password=generate_password_hash(os.urandom(16).hex()),
            is_verified=True
        )
        db.session.add(user)
        db.session.commit()

    login_user(user)
    return redirect(url_for('dashboard'))

# =============================
# OAuth: GitHub
# =============================

@app.route('/login/github')
def github_login():
    return github.authorize_redirect(url_for('github_callback', _external=True))

@app.route('/callback/github')
def github_callback():
    token = github.authorize_access_token()
    user_info = github.get('user').json()

    email = user_info.get('email')
    username = user_info.get('login')

    if not email:
        emails = github.get('user/emails').json()
        email = next((e['email'] for e in emails if e['primary']), None)

    user = User.query.filter_by(email=email).first()

    if not user:
        user = User(
            username=username,
            email=email,
            password=generate_password_hash(os.urandom(16).hex()),
            is_verified=True
        )
        db.session.add(user)
        db.session.commit()

    login_user(user)
    return redirect(url_for('dashboard'))

# =============================
# Run App
# =============================

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)