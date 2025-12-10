# 🏥 Hospital Management System (Postgresql Project)

A PostgreSQL project for analyzing patients ,doctors ,appointments and bills with SQL queries

# 📝 Project Description
This project has 4 tables :
- patients - stores patients information like name,age,gender,phone,patient id.
- doctors - stores doctors information like name, doctor id , phone , specialization.
- appointments - stores appointment information like appointment date,appointment time etc.
- bills - stores bill information like amount , bill status etc

# ⭐ Features 
- Structured Database Design - patients,doctors,appointments,bills
- Realistic Relationships - proper primary key.

# 🛠️ Tech Stack

- PostgreSQL — Database engine for storing and managing all tables.

- SQL — For writing queries, joins, constraints, and analytics.

- pgAdmin 4 — GUI tool used for managing and visualizing the database.

#  📂 Database Schema

- patients - Stores patient data
- doctors - Stores doctors data
- appointment - Stores appointment data
- bills - Stores bills data

# 📜 SQL Queries Included 

The project includes a queries.sql file organized into the following sections:

1. Filtering and Basic Queries

Simple SELECT statements to view data from each table and filtering and oerators such  as:
=,!=,ilike

2. DISTINCT, LIKE, ALIASES

Using Different Clauses like :
Distinct , like , ilike and Aliases 

3. GROUP BY + AGGREGATION

Using functions like : count(),min(),sum() ...
and clauses like : group by , having

4.  JOINS

Inner/left/right join on :

- patients
- doctors
- appointments
- bills

5.  SUBQUERIES

Using Subqueries in all tables and subquiers in from,select,where

6. CTEs

Creating CTEs for implementing for some common problems to solve

7. Window Functions 

Using Window Functions such as rank(),row_number(),lag(),lead() etc

8. VIEW , PROCEDURE , ALTER

Implementing SQL VIEWs, Stored Procedures & Table Alterations for Hospital Management System

# 🚀 How to Run

- Install PostgreSQL & pgAdmin4.

- Create a new database (startup_funding).

- Open queries.sql in pgAdmin.

- Run the script to create tables and insert sample data.

- Execute any query section (Basic, Joins, Views, etc.).

# 📁 Folder Structure

Startup_Funding/

│── queries.sql          # SQL queries (basic to advanced)

│── patients.sql         

│── doctors.sql

│── appointments.sql      

│── bills.sql

│── readme.md

# 📊 Sample Output
Example : cumulative sum of bills sorted by date + bill id.

amount |  sum
-------+------
450       450 
620       1070
300       1370

# 📄 License
This project is licensed under the MIT License.