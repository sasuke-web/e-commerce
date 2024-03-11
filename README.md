# E-Commerce API

This is an e-commerce API built with Django Rest Framework for managing customers, orders, and products.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/e-commerce.git
    cd e-commerce
    ```
2. Create and activate a virtual environment (optional but recommended):
    ```
        python3 -m venv venv
        source venv/bin/activate
    ```
3. Install dependencies:
    ```
        pip install -r requirements.txt
    ```
4. Set up the database (SQLite is used by default):
    ```
        python manage.py migrate
    ```
5. Create a superuser:
    ```
        python manage.py createsuperuser
    ```
6. Run the development server:
    ```
        python manage.py runserver
    ```

## API Endpoints

    List all customers: GET /api/customers/
    Create a new customer: POST /api/customers/
    Update an existing customer: PUT /api/customers/<id>/
    List all orders: GET /api/orders/
    Create a new order: POST /api/orders/
    Update an existing order: PUT /api/orders/<id>/
    List orders based on products: GET /api/orders/?products=Product1,Product2
    List orders based on customer: GET /api/orders/?customer=CustomerName

Payload Examples
    Create Customer (POST /api/customers/)
    
    ```
    {
        "name": "John Doe",
        "contact_number": "1234567890",
        "email": "john.doe@example.com"
    }
    ```

Create Order (POST /api/orders/)

    ```
    {
        "customer": 1,
        "order_date": "2024-03-11",
        "address": "Ahmedabad",
        "order_items": [
            {
                "product": 1,
                "quantity": 2
            },
            {
                "product": 2,
                "quantity": 1
            },
            {
                "product": 3,
                "quantity": 500
            },
            {
                "product": 4,
                "quantity": 500
            }
        ]
    }
    ```

Create Product (POST /api/products/)

    ```
    {
        "name": "eraser",
        "weight": "0.05"
    }
    ```