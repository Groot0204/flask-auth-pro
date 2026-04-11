# 🔐 Flask Auth Pro  
### Production-Ready Authentication System (Flask • PostgreSQL • OAuth • Email Verification)

A **full-stack authentication system** built using Flask, featuring secure login, registration, email verification, OAuth login, and password recovery.

> ⚡ Designed with real-world practices: secure authentication, token-based flows, and scalable backend.

---

## 🌐 Live Demo

🔗 https://flask-auth-pro-groot.vercel.app  

---

## ✨ Features

### 🔑 Authentication System
- User Registration with validation
- Login using **username OR email**
- Secure logout system
- Protected dashboard (`@login_required`)

### 📧 Email Verification System
- Verification email sent on registration
- Token-based verification using `itsdangerous`
- Expiring verification links (1 hour)
- Prevent login until email is verified

### 🔐 Password Reset System
- Forgot password via email
- Secure reset link with token
- Token expiration (10 minutes)
- Strong password validation enforced

### 🔗 OAuth Login
- Google Login
- GitHub Login
- Auto account creation on first OAuth login

### 🔐 Security Features
- Password hashing using `Werkzeug`
- Strong password validation:
  - Minimum 8 characters
  - Uppercase + lowercase
  - Number + special character
- Secure token generation (`itsdangerous`)
- Session management with `Flask-Login`
- Environment variables for sensitive data

### 🎨 UI / UX
- Modern glassmorphism design
- Fully responsive (mobile + desktop)
- Animated login/register toggle  
- Password strength meter (real-time) :contentReference[oaicite:0]{index=0}  
- Flash messages with auto-dismiss  
- Button loading states  

---

## 🛠 Tech Stack

| Technology          | Purpose                             |
|---------------------|-------------------------------------|
| Flask               | Backend framework                   |
| Flask-Login         | Authentication & session handling   |
| Flask-SQLAlchemy    | ORM for database                    |
| PostgreSQL / SQLite | Database                            |
| Flask-Mail          | Email system                        |
| Authlib             | OAuth integration                   |
| Werkzeug            | Password hashing                    |
| itsdangerous        | Token generation                    |
| HTML / CSS / JS     | Frontend UI                         |

Dependencies used: :contentReference[oaicite:1]{index=1}  

---

# 📂 Project Structure

```
flask-auth-system/
│
├── app.py
├── requirements.txt
├── vercel.json
├── .gitignore
│
├── templates/
│ ├── base.html
│ ├── dashboard.html
│ ├── forgot_password.html
│ └── reset_password.html
│
├── static/
│ ├── style.css
│ ├── script.js
│ └── bg.jpg
│
└── README.md
```

---

# 🏗 System Architecture

```
User Browser
      ↓
Flask Application
      ↓
SQLAlchemy ORM
      ↓
Database (PostgreSQL/SQlite)
```

## 🔄 Authentication Flow:

1. User registers with email + password  
2. Verification email is sent  
3. User clicks verification link  
4. Account gets activated  
5. User logs in  
6. Dashboard is accessible  

---

# ⚙️ Environment Variables\

Create a `.env` or set environment variables:

The following environment variables must be configured in **Vercel → Project Settings → Environment Variables**

Example:

```
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key

MAIL_USERNAME=your_email
MAIL_PASSWORD=your_app_password

GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_secret

GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_secret

```

---

# 🧪 Running Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/flask-auth-pro.git
cd flask-auth-pro
```

### 2️⃣ Create virtual environment

```
python -m venv venv
```

### 3️⃣ Activate environment

**Windows**

```
venv\Scripts\activate
```

**Mac / Linux**

```
source venv/bin/activate
```

### 4️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 5️⃣ Configure environment variables

```
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
```

### 6️⃣ Run the application

```
python app.py
```

---

# 🔐 Security Highlights
- Passwords are hashed (never stored in plain text)
- Email verification required before login
- Token-based password reset with expiration
- Regex-based strong password validation
- Secure session handling

---

# 🔐 Security Features

• Password hashing using `generate_password_hash()`
• Password verification using `check_password_hash()`
• Secure password reset tokens using `itsdangerous`
• Strong password validation rules
• Environment variable protection for sensitive data

---

# 📚 Key Learnings

Through this project:

* Learned how to deploy **Flask apps on Vercel**
* Implemented **authentication using Flask-Login**
* Connected Flask with **PostgreSQL cloud database**
* Managed **environment variables for security**
* Implemented **secure password hashing**
* Handled **serverless deployment debugging**
* Built a **production-ready authentication system**

---

# 🚀 Future Improvements

Possible upgrades:

• Email resend verification
• JWT authentication API
• User profile system
• Admin dashboard
• Docker deployment
• Rate limiting for security

---

# 👨‍💻 Author

**Rupesh**

Python Developer | Web Developer

GitHub: https://github.com/Groot0204
---

# 📄 License

This project is licensed under the **MIT License**.