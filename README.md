# ReceiptTrackerApp


## Overview

This Django application allows users to manually enter and track their receipt information. It emphasizes basic CRUD operations (Create, Read, Update, Delete) and incorporates user authentication. The application utilizes MySQL as the database backend for storing receipt and user data.

## Requirements

- Django 4.2.7
- Python 3.10.11
- MySQL Database Server
- MySQL Client for Python
- Git


## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/h-tounsi/ReceiptTrackerApp.git

2. **Navigate to the Project Directory:**
    ```bash
    cd ReceiptTracker
3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt  

4. **Create MySQL Database:**
    - "Create a database with the name specified in the .env file, and update the MySQL username and password in the .env file accordingly."
5. **Apply Database Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
6. **Create a Superuser Account (for Admin Access):**
    ```bash
    python manage.py createsuperuser
7. **Collect Static Files:**
    ```bash
    python manage.py collectstatic

8. **Run the Development Server:**
    ```bash
    python manage.py runserver

## Access the application at http://localhost:8000/.

9. **Run Tests:**
    ```bash
    python manage.py test


## Functionalities


### User Authentication
- The application includes user **registration**, **login**, and **logout** functionalities using Django's built-in User model. 
Users can only view and manage their own receipts.


### Receipt Management

- **Create Receipt:**
  - Users can manually enter and create a new receipt.
  - 
- **Edit Receipt:**
  - Users can modify the details of an existing receipt.

- **Show Receipt Details:**
  - Users can view detailed information about a specific receipt.

- **Delete Receipt:**
  - Users can delete a single receipt.

- **Delete Multiple Receipts:**
  - Users can select and delete multiple receipts at once.


