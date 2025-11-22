-- =========================================== 
-- 1️⃣ Basic Queries
-- =========================================== 

-- Display each product's name, category, and price.
select name,category,price from products; 

-- Show supplier names along with the city they operate from.
select name,city from suppliers; 

-- Retrieve sales transactions showing sale date and total price.
select sale_date,total_price from sales; 

-- Count how many products exist in each category.
select category,count(*) as products from products group by category; 

-- Find all products that currently have stock less than 50.
select * from products where stock_quantity<50;


-- ===========================================
-- 2️⃣ Filtering & Sorting
-- ===========================================
-- Show all Beverages category products.
select * from products
where category = 'Beverages';

-- List all suppliers located in the city of Seattle..
select * from suppliers
where city = 'Seattle';

-- Retrieve sales entries where sold quantity is more than 5.
select * from sales
where quantity > 5;

-- Fetch the 5 most expensive products.
select  * from products order by price desc limit 5;


-- ===========================================
-- 3️⃣ Aggregate Functions
-- ===========================================

-- Calculate total revenue generated from all sales.
select sum(total_price) sales_revenue from sales;

-- Compute the average product price for each category.
select category,round(avg(price),2) as Avg_price from products
group by category;

-- Count how many products each supplier provides.
select s.name,count(p.name) as total_products 
from product_suppliers ps
inner join products p 
on p.product_id = ps.product_id
inner join suppliers s
on s.supplier_id = ps.supplier_id
group by s.name;

-- Find the minimum and maximum stock quantity among all products.
select min(stock_quantity) as min_stock,max(stock_quantity) AS max_stock from products;


-- ===========================================
-- 4️⃣ Joins
-- ===========================================

-- List each product along with its supplier(s).
select p.name,s.name from product_suppliers as ps
join products as p
on p.product_id = ps.product_id
join suppliers as s
on s.supplier_id = ps.supplier_id;

-- Display each sale including product name, quantity sold, and supplier.
select p.name,sl.quantity,s.name from product_suppliers as ps
join products as p
on p.product_id = ps.product_id
join suppliers as s
on s.supplier_id = ps.supplier_id
join sales as sl
on sl.product_id = ps.product_id;

-- Calculate total quantity sold for products supplied by each supplier.
select s.name as supplier_name,sum(sl.quantity) as total_sales 
from product_suppliers as ps
join suppliers s 
on s.supplier_id = ps.supplier_id
join sales sl
on sl.product_id = ps.product_id
group by s.name;

-- Identify the supplier who provides the highest number of products.
select s.name as supplier_name,count(p.name) as total_products 
from product_suppliers ps
join products p 
on p.product_id = ps.product_id
join suppliers s
on s.supplier_id = ps.supplier_id
group by s.name
order by count(p.name) desc
limit 1;


-- ===========================================
-- 5️⃣ Grouping & Having
-- ===========================================

-- Sum total stock quantity for each product category.
select category,sum(stock_quantity) as tot_quantity 
from products
group by category;

-- Calculate total sales quantity grouped by product category.
select p.category,sum(sl.quantity) as total_sales 
from product_suppliers as ps
join products as p
on p.product_id = ps.product_id
join sales as sl
on sl.product_id = ps.product_id
group by p.category;

-- Show suppliers who supply more than 5 different products.
select s.name,count(p.name) as tot_products 
from product_suppliers as ps
join products as p
on p.product_id = ps.product_id
join suppliers as s
on s.supplier_id = ps.supplier_id
group by s.name
having count(p.name) > 5;

-- Compute average quantity sold for each month.
select to_char(sale_date,'YYYY-MM') as month ,
round(avg(quantity)) as avg_sales 
from sales group by to_char(sale_date,'YYYY-MM');


-- ===========================================
-- 6️⃣ Advanced / Relational Queries
-- ===========================================

-- List products with stock below 50 along with supplier details.
select * from product_suppliers ps
join products p
on p.product_id = ps.product_id
join suppliers s
on s.supplier_id = ps.supplier_id
where p.stock_quantity < 50;

-- Find products that have no sales record.
select * from product_suppliers ps
join products p
on p.product_id = ps.product_id
left join sales s
on s.product_id = ps.product_id
where s.product_id is null;

-- Retrieve the top 3 products that generated the highest revenue.
select p.product_id,p.name,sum(s.total_price) as total_revenue
from products p
join sales s
on s.product_id = p.product_id
group by p.product_id
order by total_revenue desc
limit 3;

-- Identify suppliers who provide products from more than one category.
select s.supplier_id,s.name,
count(distinct p.category) as category_count
from product_suppliers ps
join products p
on p.product_id = ps.product_id
join suppliers s
on s.supplier_id = ps.supplier_id
group by s.supplier_id, s.name
having count(distinct p.category) > 1;

-- Calculate total revenue generated from all products of each supplier.
select s.name,sum(total_price) as revenue 
from product_suppliers as ps
join suppliers as s
on s.supplier_id = ps.supplier_id
join sales as sl
on sl.product_id = ps.product_id
group by s.name;


-- ===========================================
-- 7️⃣ Advanced SQL Features
-- ===========================================

-- Create a stored view showing product, supplier, total sales, and stock.
create view product_info as 
select p.product_id,p.name as product_name,s.name supplier_name,
sum(sl.total_price) as total_price,p.stock_quantity as total_quantity
from product_suppliers ps
join products p
on p.product_id = ps.product_id
join suppliers s
on s.supplier_id = ps.supplier_id
join sales sl
on sl.product_id = ps.product_id 
group by p.product_id,p.name,s.name,p.stock_quantity;
select * from product_info;

-- Calculate cumulative total sales for each product ordered by sale date.
select p.product_id,p.name,s.sale_date,sum(s.total_price) 
over(partition by p.product_id order by s.sale_date) as sale_amount 
from products p
join sales as s
on s.product_id = p.product_id
order by s.sale_date;













