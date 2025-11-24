-- =========================================== 
-- Session 1: Filtering & Basic WHERE Clauses 
-- =========================================== 

-- Startups founded after 2017
select * from startups where founded_year>2017; 

-- Startups located in India or USA 
select * from startups where country = 'India' or country = 'USA';

-- Investors whose HQ is not in USA 
select * from investors where hq_country != 'USA';

-- Startups founded between 2015 and 2020
 select * from startups where founded_year between 2015 and 2020;
 
-- Startup names containing 'tech'
select * from startups where startup_name ilike '%tech%'; 

-- Startup names starting with A
 select * from startups where startup_name like 'A%';
 
-- Startups with NULL city value
 select * from startups where city is null;
 
-- Investor names ending with 'Ventures'
 select * from investors where investor_name like '_%Ventures';

 -- ===========================================
-- Session 2: Functions
-- ===========================================

-- Startup names in uppercase
select upper(startup_name) as startup_name from startups;

-- Investor names in lowercase.
select lower(investor_name) as investor_name from investors;

-- Length of startup name.
select length(startup_name) as name_length from startups;

-- Funding amount rounded to the nearest integer.
select round(amount) as amount from funding;

-- Current date and time
select current_date, current_time;

-- Total equity for startup 1 (rounded to 2 decimal places)
select round(sum(equity_percentage),2) as equity from funding
where startup_id = 1;


-- ===========================================
-- Session 3: Aggregations & GROUP BY
-- ===========================================

-- Total startups per country
select country,count(startup_name) as tot_startups from startups
group by country;

-- Average funding amount per startup
select startup_id,round(avg(amount)) as avg_fund from funding
group by startup_id;

-- Max funding amount per round
select funding_round,max(amount) as max_funding from funding
group by funding_round;

-- Total equity taken by each investor
select investor_id,sum(equity_percentage) as tot_equity from funding
group by investor_id;

-- Min, max, avg founded year
select min(founded_year),max(founded_year),avg(founded_year)
from startups;

-- Total funding amount per startup
select startup_id,round(sum(amount)) as tot_fund from funding
group by startup_id;

-- Countries with more than 5 startups
select country,count(*) as tot_startups from startups
group by country
having count(*)>5;


-- ===========================================
-- Session 4: JOINs
-- ===========================================

-- Funding rounds with startup + investor details
select s.startup_id ,i.investor_id,f.funding_round from funding f
join startups s
on s.startup_id = f.startup_id
join investors i
on i.investor_id = f.investor_id;

-- Total funding per startup (LEFT JOIN)
select s.startup_name,sum(amount) as total_amount from startups s
left join funding f 
on s.startup_id = f.startup_id
group by s.startup_name;

-- All investors with startups they funded (include investors with no funding)
select s.startup_name,i.investor_name from investors i
left join funding f
on i.investor_id = f.investor_id
left join startups s
on s.startup_id = f.startup_id;

-- Funding where startup & investor belong to same country
select s.startup_name,i.investor_name from funding f
join investors i
on i.investor_id = f.investor_id
join startups s
on s.startup_id = f.startup_id
where s.country = i.hq_country;

-- All investors with funded startups (RIGHT JOIN)
select s.startup_name,i.investor_name from funding f
right join investors i
on i.investor_id = f.investor_id
left join startups s
on s.startup_id = f.startup_id;

-- All startups and investors (FULL OUTER JOIN)
select s.startup_name,i.investor_name from funding f
full outer join investors i
on i.investor_id = f.investor_id
full outer join startups s
on s.startup_id = f.startup_id;


-- ===========================================
-- Session 5: Subqueries
-- ===========================================

-- Startups whose total funding > average funding of all startups
select s.startup_name,sum(f.amount) as tot_fund from funding f
join startups s
on s.startup_id =f.startup_id
group by s.startup_id,s.startup_name
having sum(f.amount)>(select avg(tot_amt)
from (select startup_id , sum(amount) as tot_amt
from funding 
group by startup_id
));

-- Investors who funded more than 2 startups
select i.investor_name,count(distinct f.startup_id) as tot_invested from funding f
join investors i 
on i.investor_id = f.investor_id
group by i.investor_id
having count(distinct f.startup_id)>2;

-- Startups funded by Indian investors
select s.startup_name, i.hq_country from funding f
join investors i
on i.investor_id = f.investor_id
join startups s
on s.startup_id = f.startup_id
where i.hq_country = 'India';

-- Startups whose funding amount > max funding of startup 1
select s.startup_name from funding f
join startups s
on s.startup_id = f.startup_id
where f.amount > (select max(amount) max_amount from funding
where startup_id = 1);


-- ===========================================
-- Session 6: CTEs (Common Table Expressions)
-- ===========================================

-- Total funding per startup (CTE) and filter > 2M
with tot_funding as (
select s.startup_name,sum(f.amount) as tot_funds from funding f
join startups s
on s.startup_id = f.startup_id
group by s.startup_id , s.startup_name
)
select * from  tot_funding
where tot_funds>2000000;

-- Rank investors by total funding
with investor_funding as (
select i.investor_name,sum(f.amount) as tot_funds from funding f
join investors i
on i.investor_id = f.investor_id
group by i.investor_id , i.investor_name
)
select *,rank() over(order by tot_funds desc)from investor_funding;

-- Average funding per startup (CTE)
with tot_funding as (
select s.startup_name,round(avg(f.amount)) as avg_funds from funding f
join startups s
on s.startup_id = f.startup_id
group by s.startup_id , s.startup_name
)
select avg_funds from tot_funding;

-- Top 5 startups by total funding
with tot_funding as (
select s.startup_name,sum(f.amount) as tot_funds from funding f
join startups s
on s.startup_id = f.startup_id
group by s.startup_id , s.startup_name
)
select * from tot_funding
order by tot_funds desc limit 5;


-- ===========================================
-- Session 7: Window Functions
-- ===========================================

-- Cumulative funding per startup
select s.startup_name,f.amount,sum(f.amount) 
over(partition by f.startup_id order by f.amount ) as funds from funding f
join startups s
on f.startup_id = s.startup_id;

-- Rank investors by total funding
select i.investor_name,sum(f.amount) as tot_funds,rank() 
over(order by sum(f.amount) desc) as ranks from funding f
join investors i
on i.investor_id = f.investor_id
group by i.investor_name,i.investor_id;

-- Dense rank by equity percentage
select s.startup_name,f.equity_percentage,dense_rank() 
over(order by f.equity_percentage desc) as equity_taken from funding f
join startups s
on f.startup_id = s.startup_id;

-- Previous funding amount per startup
select s.startup_name,f.funding_date,lag(f.amount) 
over(partition by s.startup_name order by f.funding_amount) from funding f
join startups s
on s.startup_id = f.startup_id;

-- Divide startups into 4 funding groups
select s.startup_name,sum(f.amount) as tot_amount,
ntile(4) over(order by sum(f.amount) desc) as Division 
from funding f
join startups s 
on f.startup_id = s.startup_id
group by s.startup_name,s.startup_id;


