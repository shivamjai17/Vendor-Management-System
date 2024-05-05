# Vendor Management System API Documentation

The Vendor Management System API provides endpoints for managing vendor profiles, tracking purchase orders, and evaluating vendor performance metrics.

## Setup Instructions

To set up the Vendor Management System API locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/shivamjai17/Vendor-Management-System
2. Navigate to the project directory:
     ```bash
    cd vendor-management-system
3. Install dependencies:
    ```base
    pip install -r requirements.txt
4. Activate Virtual Environment
    ```base
    cd env
    scripts/activate
4. Apply database migrations:
    ```base
    python manage.py migrate
5. python manage.py createsuperuser
    ```base
    python manage.py createsuperuser

6. Start the development server:
    ```base
    python manage.py runserver
7. Access the API at http://127.0.0.1:8000/api/


API Endpoints

# Vendor Profile Management

## Create a New Vendor
- **URL:** /api/vendors/
- **Method:** POST
- **Parameters:**
  - name (string): Vendor's name
  - contact_details (string): Contact information of the vendor
  - address (string): Physical address of the vendor
  - vendor_code (string): Unique identifier for the vendor

## List All Vendors
- **URL:** /api/vendors/
- **Method:** GET

## Retrieve Vendor Details
- **URL:** /api/vendors/{vendor_id}/
- **Method:** GET
- **Parameters:**
  - vendor_id (integer): ID of the vendor

## Update Vendor Details
- **URL:** /api/vendors/{vendor_id}/
- **Method:** PUT
- **Parameters:**
  - vendor_id (integer): ID of the vendor
  - (optional) name (string): Vendor's name
  - (optional) contact_details (string): Contact information of the vendor
  - (optional) address (string): Physical address of the vendor
  - (optional) vendor_code (string): Unique identifier for the vendor

## Delete a Vendor
- **URL:** /api/vendors/{vendor_id}/
- **Method:** DELETE
- **Parameters:**
  - vendor_id (integer): ID of the vendor

# Purchase Order Tracking

## Create a Purchase Order
- **URL:** /api/purchase_orders/
- **Method:** POST
- **Parameters:**
  - po_number (string): Unique number identifying the PO
  - vendor (integer): ID of the vendor
  - order_date (date): Date when the order was placed
  - delivery_date (date): Expected or actual delivery date of the order
  - items (JSON): Details of items ordered
  - quantity (integer): Total quantity of items in the PO
  - status (string): Current status of the PO (e.g., pending, completed, canceled)
  - (optional) quality_rating (float): Rating given to the vendor for this PO

## List All Purchase Orders
- **URL:** /api/purchase_orders/
- **Method:** GET

## Retrieve Purchase Order Details
- **URL:** /api/purchase_orders/{po_id}/
- **Method:** GET
- **Parameters:**
  - po_id (integer): ID of the purchase order

## Update Purchase Order Details
- **URL:** /api/purchase_orders/{po_id}/
- **Method:** PUT
- **Parameters:**
  - po_id (integer): ID of the purchase order
  - (optional) po_number (string): Unique number identifying the PO
  - (optional) vendor (integer): ID of the vendor
  - (optional) order_date (date): Date when the order was placed
  - (optional) delivery_date (date): Expected or actual delivery date of the order
  - (optional) items (JSON): Details of items ordered
  - (optional) quantity (integer): Total quantity of items in the PO
  - (optional) status (string): Current status of the PO (e.g., pending, completed, canceled)
  - (optional) quality_rating (float): Rating given to the vendor for this PO

## Delete a Purchase Order
- **URL:** /api/purchase_orders/{po_id}/
- **Method:** DELETE
- **Parameters:**
  - po_id (integer): ID of the purchase order

# Vendor Performance Evaluation

## Retrieve Vendor Performance Metrics
- **URL:** /api/vendors/{vendor_id}/performance/
- **Method:** GET
- **Parameters:**
  - vendor_id (integer): ID of the vendor

# Authentication

All API endpoints require token-based authentication. Obtain an authentication token by logging in as a superuser.


