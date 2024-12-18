

# Gas Utility Service Application

## Overview
The Gas Utility Service Application is a web-based platform built with Django to manage customer service requests for gas utilities. Customers can register, log in, submit service requests, and track their status, while admins can oversee and manage these requests, including updating their statuses.

---

## Features

### Customer Features
- **User Registration**: Customers can create accounts to access the service.
- **Login and Authentication**: Secure access to the platform via username and password.
- **Submit Requests**: Customers can submit detailed service requests for gas-related services.
- **Track Requests**: View the real-time status of submitted requests.
- **Password Reset**: Customers can reset their passwords using email verification.

### Admin Features
- **Request Management**: Admins can view and filter service requests by type and status.
- **Status Updates**: Admins can directly update the status of requests from the admin panel.

---

## Technology Stack
- **Backend**: Django 5.1.3 (Python 3.12+)
- **Frontend**: HTML, CSS
- **Database**: SQLite (default Django configuration)
- **Authentication**: Django's built-in authentication system

---

## Installation Guide

### Prerequisites
- Python 3.12+
- Virtual environment (recommended)

### Steps
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/jayasaisrikar/gas-utility-service.git
    cd gas-utility-service
    ```

2. **Set Up a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Start the Server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the Application**:
    Open your browser and navigate to `http://127.0.0.1:8000`.

---

## Requirements

To run this application, you need the following Python packages:

- Django==5.1.3
- gunicorn==20.1.0
- pillow==9.0.1
- psycopg2==2.9.5
- djangorestframework==3.14.0
- python-dotenv==0.21.0

You can install them by running:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should look like this:

```
Django==5.1.3
gunicorn==20.1.0
pillow==9.0.1
psycopg2==2.9.5
djangorestframework==3.14.0
python-dotenv==0.21.0
```

---

## Usage Instructions

### Customer Workflow
1. **Register**: Go to `/register/` to create an account.
2. **Login**: Log in at `/login/`.
3. **Submit a Request**: Use `/submit-request/` to file a service request.
4. **Track Requests**: Check the status of your requests at `/track-request/`.

### Admin Workflow
1. **Admin Login**: Access the admin panel at `/admin/`.
2. **Manage Requests**: View, filter, and update service requests via the admin interface.

---

## Application Structure

```
gas_utility_service/
├── customer_service/
│   ├── admin.py           # Admin configuration for request management
│   ├── models.py          # Database models for service requests
│   ├── views.py           # Logic for handling customer actions
│   ├── urls.py            # URL patterns for customer endpoints
│   ├── templates/         # HTML templates for customer-facing pages
│       ├── login.html
│       ├── register.html
│       ├── submit_request.html
│       ├── track_request.html
├── gas_utility_service/
│   ├── settings.py        # Project settings
│   ├── urls.py            # Root URL configuration
│   ├── wsgi.py            # WSGI entry point
└── manage.py               # Project management command
```

---

## Key Functionalities

### Password Reset
- **URL**: `/password-reset/`
- **Description**: Enables customers to reset their password via email verification.

### Request Management (Admin)
- **Admin Panel**: Accessible at `/admin/`, allowing admins to view and manage service requests, including updating their status (e.g., "In Progress", "Completed").

### Request Submission and Tracking (Customer)
- **Submit Request**: Customers can submit requests on the `/submit-request/` page, providing information such as the request type and description.
- **Track Requests**: Customers can track the status of their requests in real-time on the `/track-request/` page.

---
### Admin Controls
- View all customer requests.
- Filter requests by type and status.
- Update the status of requests directly from the admin interface.

---

## Future Enhancements
- Add email notifications for service request updates.
- Integrate a payment gateway for service fees.
- Implement advanced analytics for admins to track service performance.

