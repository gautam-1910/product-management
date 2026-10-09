# Product Management System

A simple e-commerce product management app built with Django. Admins can log in, see store stats on a dashboard, and add, view, edit, search, filter and delete products.

## Technologies Used
- Python, Django 5
- SQLite
- HTML, Bootstrap 5
- Pillow (image uploads)

## How to Install
```
git clone https://github.com/gautam-1910/product-management.git
cd product-management
python -m venv venv
venv\Scripts\activate        (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

## How to Run
```
python manage.py runserver
```
Open http://127.0.0.1:8000/ and log in.

Before adding products, create at least one category at http://127.0.0.1:8000/admin/ (Products > Categories).

## Login Credentials
- Username: `admin`
- Password: `admin123`

(Create these yourself with `createsuperuser` in the install step.)

## About the Project
- Login and logout (all product pages require login)
- Dashboard cards: total, active, inactive and low stock products
- Product list with search by name, category filter, status filter and pagination
- One form for adding and editing products with validation
- Product detail page and delete with confirmation

## Business Rules
- SKU must be unique
- Price must be greater than 0
- Stock cannot be negative
- Stock of 5 or below shows a Low Stock badge
- Inactive products show a clear Inactive badge
- Only logged-in users can add, edit or delete products