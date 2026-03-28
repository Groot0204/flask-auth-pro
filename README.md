# 🔐 Flask Auth Pro  
### Production-Ready Authentication System (Flask • Vercel • PostgreSQL • Email Reset)

A **full-stack authentication system** built using Flask and deployed on **Vercel serverless architecture**, featuring secure login, registration, and email-based password recovery.

> ⚡ Built with real-world challenges: serverless backend, cloud database, and secure authentication flow.

---

## 🌐 Live Demo

🔗 https://flask-auth-pro-groot.vercel.app

---

## ✨ Core Features

### 🔑 Authentication System
- User Registration with validation
- Login using **username OR email**
- Secure logout system
- Protected Dashboard(@login_required)

### 🔐 Security Implementation
- Password hashing using `Werkzeug`
- Strong password validation:
  - Minimum 8 characters
  - Uppercase, lowercase
  - Number + special character
- Secure token-based password reset (itsdangerous)
- Token expiration (10 minutes)

### 📧 Email System
- Password reset via SMTP(Flask-Mail)
- Secure reset links
- HTML email support

### ⚡ Deployment & Backend
- Serverless deployment using **Vercel**
- Cloud database using **Neon PostgreSQL**
- Environment variable-based configuration
- Production-ready structure

### 🎨 UI / UX
- Modern Glassmorphism Design
- Fully responsive (Mobile + Desktop)
- Animated login/register toggle
- Password strength meter (real-time)
- Flash messages with auto-dismiss
- Button loading states
---

# 🛠 Tech Stack

| Technology            | Purpose                             |
| --------------------- | ----------------------------------- |
| **Flask**             | Backend Web Framework               |
| **Flask-Login**       | Authentication & session management |
| **Flask-SQLAlchemy**  | ORM for database operations         |
| **PostgreSQL (Neon)** | Cloud database                      |
| **Flask-Mail**        | Email                               |
| **Werkzeug**          | Password hashing                    |
| **itsdangerous**      | Secure token generation             |
| **Vercel**            | Serverless deployment platform      |
| **Frontend**          | HTML, CSS, JavaScript               |

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

# 📸 Application Screenshots

*(You can add screenshots here for better presentation)*

## 📸 Screenshots

### 🔐 Authentication UI
![Login](assets/login.png)
![Register](assets/register.png)

### 📱 Mobile View
![Mobile Login](assets/mobile-login.png)

### 📊 Dashboard
![Dashboard](assets/dashboard.png)


# 🏗 System Architecture

```
User Browser
      ↓
Vercel Serverless Function (Flask)
      ↓
SQLAlchemy ORM
      ↓
Neon PostgreSQL Cloud Database
```

# 🔄 Authentication Flow:

1. User sends request from browser
2. Flask serverless function processes request
3. SQLAlchemy communicates with PostgreSQL
4. Database returns data to Flask
5. Flask renders response to user

---

# ⚙️ Environment Variables

The following environment variables must be configured in **Vercel → Project Settings → Environment Variables**

| Variable      | Description                       |
| ------------- | --------------------------------- |
| DATABASE_URL  | Neon PostgreSQL connection string |
| SECRET_KEY    | Flask secret key                  |
| MAIL_USERNAME | Email for SMTP                    |
| MAIL_PASSWORD | App password                      |

Example:

```
DATABASE_URL=postgresql://username:password@host/dbname?sslmode=require
SECRET_KEY=your_secret_key
MAIL_USERNAME=your_email
MAIL_PASSWORD=your_app_password

```

---

# 🔐 Security Highlights
- Passwords are hashed (never stored in plain text)
- Token-based password reset with expiration
- Strong password validation using regex
- Secure session handling with Flask-Login
- Environment variables for sensitive data

---

# 🔐 Security Features

• Password hashing using `generate_password_hash()`
• Password verification using `check_password_hash()`
• Secure password reset tokens using `itsdangerous`
• Strong password validation rules
• Environment variable protection for sensitive data

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

# 🌐 Deployment

The project is deployed using **Vercel serverless Python functions**.

Key Challenges Solved
- Running Flask in serverless environment
- Connecting external Neon PostgreSQL database
- Fixing `postgres:// → postgresql://` issue
- Managing environment variables securely

Deployment steps:

1. Push project to GitHub
2. Import repository into Vercel
3. Configure environment variables
4. Deploy

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

• Email verification system
• OAuth login (Google, GitHub)
• JWT authentication API
• User profile system
• Admin dashboard
• Docker deployment

---

# 👨‍💻 Author

**Rupesh**

Python Developer | Web Developer

GitHub: https://github.com/Groot0204
---

# 📄 License

This project is licensed under the **MIT License**.