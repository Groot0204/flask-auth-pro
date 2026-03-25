# 🔐 Flask Authentication System  
### (Flask • Vercel Serverless • PostgreSQL • Email Reset)

A **production-ready authentication system** built using Flask and deployed on **Vercel serverless architecture**, featuring secure login, registration, and password recovery using token-based authentication.

> ⚡ Built with real-world deployment constraints and solutions (Flask on Vercel + cloud database integration)

---

# 🚀 Live Demo

https://flask-auth-system-groot.vercel.app

---

## ✨ Core Features

### 🔑 Authentication System
- User Registration with validation
- Login using **username OR email**
- Secure logout system
- Protected routes using Flask-Login

### 🔐 Security Implementation
- Password hashing using `Werkzeug`
- Strong password validation:
  - Minimum 8 characters
  - Uppercase, lowercase
  - Number + special character
- Secure token-based password reset
- Token expiration handling

### 📧 Password Recovery
- Email-based reset system (SMTP)
- Unique signed reset links using `itsdangerous`
- Safe password update flow

### ⚡ Deployment & Backend
- Serverless deployment using **Vercel**
- Cloud database using **Neon PostgreSQL**
- Environment variable-based configuration
- Production-ready structure

---

# 🛠 Tech Stack

| Technology            | Purpose                             |
| --------------------- | ----------------------------------- |
| **Flask**             | Backend Web Framework               |
| **Flask-Login**       | Authentication & session management |
| **Flask-SQLAlchemy**  | ORM for database operations         |
| **PostgreSQL (Neon)** | Cloud database                      |
| **psycopg2**          | PostgreSQL adapter                  |
| **Werkzeug**          | Password hashing                    |
| **itsdangerous**      | Secure token generation             |
| **Vercel**            | Serverless deployment platform      |

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

### Login Page

![Login Page](assets/login.png)
![Login Page](assets/mobile-login.png)

### Registration Page

![Register Page](assets/register.png)
![Register Page](assets/mobile-register.png)

### Dashboard

![Dashboard](assets/dashboard.png)
![Dashboard](assets/mobile-dashboard.png)

---

# 🏗 System Architecture

```
User Browser
      ↓
Vercel Serverless Flask Application
      ↓
Neon PostgreSQL Cloud Database
```

Flow:

1. User sends request from browser
2. Flask serverless function processes request
3. SQLAlchemy communicates with PostgreSQL
4. Database returns data to Flask
5. Flask renders response to user

---

# ⚙️ Environment Variables

The following environment variables must be configured in **Vercel → Project Settings → Environment Variables**

| Variable       | Description                                    |
| -------------- | ---------------------------------------------- |
| `DATABASE_URL` | PostgreSQL connection string from Neon         |
| `SECRET_KEY`   | Secret key used for session and token security |

Example:

```
DATABASE_URL=postgresql://username:password@host/dbname?sslmode=require
SECRET_KEY=your_secure_secret_key
```

---

# 💾 Database

The application uses **PostgreSQL (Neon)**.

### User Table

| Field    | Type          |
| -------- | ------------- |
| id       | Integer       |
| username | String        |
| email    | String        |
| password | Hashed String |

Passwords are stored using **secure hashing**, never in plain text.

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
git clone https://github.com/YOUR_USERNAME/flask-auth-system.git
cd flask-auth-system
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

Deployment steps:

1. Push project to GitHub
2. Import repository into Vercel
3. Configure environment variables
4. Deploy application

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

• Email sending for password reset
• JWT authentication system
• User profile management
• Admin dashboard
• REST API version of authentication
• Database migrations using Flask-Migrate
• Docker containerization

---

# 👨‍💻 Author

**Rupesh**

Python Developer | Web Developer

---

# 📄 License

This project is licensed under the **MIT License**.
