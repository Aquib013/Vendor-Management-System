# README

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for?

Vendor Management System (VMS)

Overview

The Vendor Management System (VMS) is a web-based application designed to streamline vendor management processes within
an organization. This system provides a set of APIs to manage vendors, purchase orders, and monitor vendor performance
efficiently.

### Core Feature

1. **Vendor Profile Management:**

    - Create, retrieve, update, and delete vendor profiles.
    - Track vendor information including name, contact details, address, and a unique vendor code.
2. **Purchase Order Tracking:**

    - Create, retrieve, update, and delete purchase orders.
    - Track purchase order details such as PO number, vendor reference, order date, items, quantity, and status.
3. **Vendor Performance Evaluation:**

    - Calculate vendor performance metrics, including on-time delivery rate, quality rating average, average response
      time, and fulfillment rate.
    - Retrieve performance metrics for a specific vendor.

### Installation

1. Clone the repository:

   ```bash
   git clone git clone git@bitbucket.org:aquib013/vms.git
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Apply database migrations:

   ```bash
   python manage.py migrate
   ```
4. Run the development server:

   ```bash
   python manage.py runserver
   ```

# API Endpoints

Below is a summary of the available API endpoints:

**Vendor Profile Management**

| Endpoint             | Method      | Description                           |
|----------------------|-------------|---------------------------------------|
| `/api/vendors/`      | POST        | Create a new vendor.                  |
| `/api/vendors/`      | GET         | List all vendors.                     |
| `/api/vendors/{id}/` | GET         | Retrieve a specific vendor's details. |
| `/api/vendors/{id}/` | PUT / PATCH | Update a vendor's details.            |
| `/api/vendors/{id}/` | DELETE      | Delete a vendor.                      |

**Purchase Order Tracking**

| Endpoint                                | Method      | Description                                    |
|-----------------------------------------|-------------|------------------------------------------------|
| `/api/purchase_orders/`                 | POST        | Create a purchase order.                       |
| `/api/purchase_orders/`                 | GET         | List all purchase orders.                      |
| `/api/purchase_orders/{id}/`            | GET         | Retrieve details of a specific purchase order. |
| `/api/purchase_orders/{id}/`            | PUT / PATCH | Update a purchase order.                       |
| `/api/purchase_orders/{id}/`            | DELETE      | Delete a purchase order.                       |
| `/api/purchase_orders/{id}/acknowledge` | POST        | Acknowledge a purchase order.                  |

**Vendor Performance Evaluation**

| Endpoint                                | Method | Description                              |
|-----------------------------------------|--------|------------------------------------------|
| `/api/vendors/{id}/performance`         | GET    | Retrieve a vendor's performance metrics. |
| `/api/vendors/{id}/performance/history` | GET    | Retrieve a vendor's performance history. |

### Contribution guidelines

Inputs and contributions to this project are appreciated. To make them as transparent and easy as possible, please
follow this steps:

### How to contribute

1. Fork the repository and create your branch from master with different name.
2. Clone the project to your own machine
3. Commit changes to your own branch
4. Push your work back up to your fork
5. Submit a Pull request

* Other guidelines
    - Don't include any license information when submitting your code as this repository is MIT licensed, and so your
      submissions are understood to be under the same MIT License as well.
* How to report a bug:
    1. Open a new Issue.
    2. Write a bug report with details, background, and when possible sample code. That's it!

### Who do I talk to? ###

* This Repo Belongs to AQUIB JAWED.

### LICENSE ###

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)






