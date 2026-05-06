-- Creating Table --
CREATE TABLE Jobs(
job_category varchar(20) not null,
job_title varchar(150) not null,
company varchar(150) not null,
location varchar(200) not null,
experience varchar(20),
experience_level varchar(20),
salary varchar(20),
salary_category varchar(20) not null,
skills varchar(300) not null,
skill_count int,
posted_time varchar(30) not null,
job_description varchar(15000),
job_link varchar(300),
source varchar(50)
);

-- Total Jobs --
select count(*) as total_jobs from Jobs;

-- Top Job Categories --
select job_category,count(*) as total_jobs from Jobs
group by job_category order by total_jobs desc;

-- Top 10 Hiring Companies --
select company,count(*) as total_jobs from Jobs
group by company order by total_jobs desc limit 10;

-- Jobs by Location --
select location,count(*) as total_jobs from Jobs
group by location order by total_jobs desc limit 8;

-- Experience Level --
select experience_level,count(*) as total_jobs from Jobs
group by experience_level;

-- Salary Distribution --
select salary_category,count(*) as total_jobs from Jobs
group by salary_category order by total_jobs desc;

-- Salary according to Experience --
select experience_level,salary_category,count(*) as total_jobs from jobs
group by experience_level,salary_category
order by experience_level,salary_category desc;