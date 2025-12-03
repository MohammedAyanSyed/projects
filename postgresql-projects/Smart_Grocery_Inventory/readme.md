# 🛒📦 Smart Grocery Inventory Management (PostgreSQL Project)

The Smart Grocery Inventory Management System is a PostgreSQL-based project designed to manage and analyze grocery inventory using a structured relational database.

# 📝 Project Description
This project contains four core tables:

- products – stores item details like name, category, price, and stock quantity

- suppliers – stores supplier information

- sales – records customer purchases and quantities sold

- product_supplier – a mapping table that links products with their suppliers

Helps in:

- Tracking product availability and stock levels

- Monitoring sales activity

- Managing supplier relationships

- Analyzing inventory performance using SQL queries

# ⭐ Features

- Structured Database Design — Products, suppliers, sales, and a link table for relationships.

- Realistic Relationships — Proper primary keys, foreign keys, and many-to-many mapping.

- Inventory & Sales Tracking — Track products, suppliers, stock, and daily sales.

# 🛠️ Tech Stack

- PostgreSQL — Database engine for storing and managing all tables

- SQL — For writing queries, joins, constraints, and analytics

- pgAdmin 4 — GUI tool used for managing and visualizing the database

# 📂 Database Schema

- products – Stores product details like name, category, price, stock

- suppliers – Contains supplier information

- product_supplier – Mapping table for product–supplier relationships

- sales – Stores daily sales records

# 📜 SQL Queries Included 

The project includes a queries.sql file organized into the following sections:

1. Basic Queries

Simple SELECT statements to view data from each table.

2. Filtering & Sorting

Queries using filtering & ordering operators such as: 
- = , < , > 
- WHERE 
- ORDER BY 
- LIMIT

3. Aggregate Queries

Uses functions like:

- SUM()

- COUNT()

- MIN()

- MAX()

- AVG()


4. Join Queries

Inner joins across:

- products

- suppliers

- product_supplier

- sales

5. Grouping Queries

Grouping and filtering aggregated data using:

- GROUP BY

- HAVING

6. Relational Queries

Queries involving foreign keys and related table lookups.

7. Advanced Queries

Includes:

- Views for reusable queries

- Window functions like SUM() OVER() for running totals

# 🚀 How to Run

- Install PostgreSQL & pgAdmin4

- Create a new database (smart_grocery)

- Open queries.sql in pgAdmin

- Run the script to create tables and insert sample data

- Execute any query section (Basic, Joins, Advanced, etc.) as needed

# 📁 Folder Structure

Smart_Grocery_Inventory/

│── queries.sql          # SQL queries (basic to advanced)

│── products.sql         

│── suppliers.sql           

│── products_suppliers.sql           

│── sales.sql      

│── README.md           

# 📊 Sample Output
Example : Products with Price > 5

 product_id | product_name        | category     | price | stock
------------+---------------------+--------------+-------+-------

     5      | Cheddar Cheese      | Dairy        | 6.00  | 70
    11      | Butter              | Dairy        | 5.50  | 80
    12      | Mozzarella Cheese   | Dairy        | 6.20  | 50
    21      | Honey               | Condiments   | 6.50  | 60
    47      | Almonds             | Nuts         |10.00  | 80
    49      | Walnuts             | Nuts         |15.00  | 50

# 📄 License
This project is licensed under the MIT License.

