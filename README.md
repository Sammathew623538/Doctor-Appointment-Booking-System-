# Doctor-Appointment-Booking-System-





# 🏥 Doctor Booking System (Django)

This is a simple **Doctor Booking System** built using Django framework.  
It allows users to register, login, book appointments with doctors, and lets doctors manage their bookings.

---

## 🚀 Features

- 🔐 User authentication (Register, Login, Logout)
- 👨‍⚕️ Doctor and Patient profiles
- 📆 Patients can book appointments with doctors
- ✅ Doctors can approve or reject bookings
- 📋 Patients can view their appointment status
- 🧾 Profile edit page for users

---

## 🛠️ Technologies Used

- Django (Python Backend)
- SQLite (Default Django DB)
- HTML & CSS (Frontend)
- Django Templates
- Django Forms & ModelForms

---

## 🔑 User Roles

1. **Admin** (Superuser)
2. **Doctor** (`is_staff=True`, `is_superuser=False`)
3. **Patient/User** (`is_staff=False`, `is_superuser=False`)

---

## 📂 Important Files

| File | Description |
|------|-------------|
| `views.py` | Contains all the backend logic |
| `urls.py` | URL routing for all views |
| `models.py` | Models for User, Profile, Booking etc. |
| `forms.py` | Django forms used for Registration and Booking |
| `templates/` | HTML files like login, register, profile etc. |

---

## 🔄 Core Functionalities

### ✍️ Registration & Login
- Users can register using a Django form
- Profile is auto-created on registration
- Login redirects to the homepage

### 📄 Profile Management
- Users can view and edit their profile

### 📅 Booking Appointments
- Patients can book appointments with doctors
- Doctors can view pending appointments
- Doctors can accept or reject bookings

### 👁️ View Appointments
- Patients can view status of their bookings
- Doctors can manage bookings from their dashboard

---

## 🔧 How to Run

```bash
# Clone the repository
git clone https://github.com/your-username/your-repo-name.git

cd your-repo-name

# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser (admin)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
