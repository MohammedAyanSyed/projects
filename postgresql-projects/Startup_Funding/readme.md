# 💰 Startup Funding (Postgresql Project)

A PostgreSQL project for analyzing startups, investors, and funding rounds with real-world SQL queries.

# 📝 Project Description
This project contains three core tables :
- startups - stores startup information like name,id,city,founded year.
- investors - stores investors information like name , headquarter country.
- funding - stores funding information like amount , equity.

# ⭐ Features
- Structured Database Design - startups , investors , funding.
- Realistic Relationships - proper primary key.

# 🛠️ Tech Stack

- PostgreSQL — Database engine for storing and managing all tables.

- SQL — For writing queries, joins, constraints, and analytics.

- pgAdmin 4 — GUI tool used for managing and visualizing the database.

#  📂 Database Schema

- startups - Stores startups information
- investors - Stores investors information
- funding - Stores funding information


# 📜 SQL Queries Included 

The project includes a queries.sql file organized into the following sections:

1. Basic & Filtering Queries

Simple SELECT statements to view data from each table and filtering and oerators such  as:
<,=,!=,like,ilike,isnull

2. Functions

Using simple string inbuild functions such as :
lower(),upper(),length(),round() ....

3. Aggregations & GROUP BY

Using Functions like : sum(),min(),max(),....
and clauses like : group by , having

4. Joins

Inner/left/right join on :

- startups
- investors
- funding

5. Subqueries

Using Subqueries in all tables and subquiers in from,select,where

6. CTE (Common Table Expression)

Creating CTEs for implementing for some common problems to solve

7. Window Functions 

Using Window Functions such as sum(),dense_rank(),lag()

# 🚀 How to Run

- Install PostgreSQL & pgAdmin4.

- Create a new database (startup_funding).

- Open queries.sql in pgAdmin.

- Run the script to create tables and insert sample data.

- Execute any query section (Basic, Joins, CTE, etc.).

📁 Folder Structure

Startup_Funding/

│── queries.sql          # SQL queries (basic to advanced)

│── startups.sql         

│── investors.sql

│── funding.sql      

│── README.md

# 📊 Sample Output
Example : Countries with more than 5 startups.

country | tot_startups
--------+-------------
India              8
USA                10

# 📄 License
This project is licensed under the MIT License.