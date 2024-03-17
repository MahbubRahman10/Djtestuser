# Django Authentication System
This project implements a simple authentication system using Django, a high-level Python web framework. Users can register, log in, log out, and update their profile information.

## Features
- User registration: Users can create a new account by providing their username, email, and password.
- User authentication: Registered users can log in using their credentials.
- Password reset: Users can request a password reset if they forget their password.
- Profile update: Logged-in users can update their profile information such as username and email.
- User management: Administrators have access to user management features, including viewing, editing, and deleting user accounts.

## Usage
- Navigate to the registration page (/accounts/register) to create a new account.
- After registering, log in using the credentials on the login page (/accounts/login).

- Once logged in, can update the profile information by visiting the profile page (/accounts/profile).
- Administrators can access user management features via the Django admin interface (/admin). Use the command python manage.py createsuperuser to create an admin account.

## Technologies Used
- Django: Web framework for building web applications in Python
- HTML/CSS: Front-end technologies for designing user interfaces
- SQLite: Database management system used for storing user data