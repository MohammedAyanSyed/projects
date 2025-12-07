-- =========================================== 
-- Session 1: Filtering & Basic WHERE Clauses 
-- =========================================== 
-- Shows only those patients who are older than 40.
select * from patients
where age > 40;

-- Shows all doctors except General Physicians.
select * from doctors
where specialization!='General Physician';

-- Sorts patients A to Z.
select * from patients order by name;

-- Shows appointments happening on 8 Jan 2025.
select * from appointments
where appointment_date = '2025-01-08';

-- Shows all unpaid bills.
select * from bills
where payment_status = 'Pending';
-- Shows all patients whose names start with letter A (case-insensitive).
select * from patients
where name ilike 'a%';

-- Filters doctors whose phone number ends with “XX”.
select * from doctors
where phone ilike '%XX';


-- =========================================== 
-- Session 2: DISTINCT, LIKE, ALIASES
-- =========================================== 

-- Removes duplicates and shows only unique doctor specializations.
select distinct(specialization) from doctors;

-- Shows all different types of payment statuses in the bills table
select distinct(payment_status) from bills;

-- Renames columns to make output more readable.
select name as patient_name, age as patient_age from patients;

-- Shows all doctors whose names include “an” anywhere (case-insensitive).
select name from doctors
where name ilike '%an%';

-- Find patients whose phone number includes “XXX”.
select phone from patients
where phone ilike '%XXX%';

-- Shows appointments where the visit reason includes “pain”
select * from appointments
where reason like '%pain%';

-- Lists each appointment date only once.
select distinct(appointment_date) from appointments;


-- =========================================== 
-- Session 3: GROUP BY + AGGREGATION
-- =========================================== 

-- Counts total number of rows in the patients table
select count(*) as tot_patients from patients;

-- Groups appointments doctor-wise and counts how many each doctor has.
select doctor_id,count(*) as tot_appointments from appointments
group by doctor_id;

-- Shows total amount collected only for 'Paid' bills.
select payment_status,sum(amount) as paid_bills from bills
group by payment_status
having payment_status = 'Paid';

-- Displays only those doctors whose appointment count is above 2.
select doctor_id,count(*) from appointments
group by doctor_id
having count(*)>2; 

-- Finds the smallest and largest bill amount
select min(amount) as min_bill,
max(amount) as max_bill
from bills;

-- Shows each health issue/reason and how many appointments came for it.
select reason,count(*) as app_reason from appointments
group by reason;


-- =========================================== 
-- Session 4: JOINS
-- =========================================== 

-- Shows each appointment with the patient’s name and doctor’s name.
select p.name,d.name,a.appointment_date from appointments a
join patients p
on a.patient_id = p.patient_id
join doctors d
on a.doctor_id = d.doctor_id;

-- Displays patients and bill amount; shows NULL if bill not available.
select p.name as patient_name,b.amount from appointments a
left join patients p
on p.patient_id = a.patient_id
left join bills b
on a.appointment_id = b.appointment_id;

-- Counts how many appointments each doctor has , 0 if none.
select d.name,count(a.appointment_id) as all_appointments 
from appointments a
left join doctors d
on a.doctor_id = d.doctor_id
group by d.name;

-- Full appointment details including patient & doctor information.
select * from appointments a
join patients p
on p.patient_id = a.patient_id
join doctors d
on d.doctor_id = a.doctor_id;

-- Shows bill amounts along with doctor specialization except General Physician.
select d.specialization,b.amount from appointments a
join doctors d
on d.doctor_id = a.doctor_id
join bills b
on b.appointment_id = a.appointment_id
where specialization != 'General Physician';

-- Shows patients whose appointment table has no matching entry.
select p.name 
from patients p
left join appointments a
on p.patient_id = a.patient_id
where a.appointment_id is null;

-- Lists appointments that still don’t have any bill generated.
select a.* from appointments a
left join bills b
on a.appointment_id = b.appointment_id
where b.bill_id is null;


-- =========================================== 
-- Session 5: SUBQUERIES
-- =========================================== 

-- Shows patients whose bill amount is higher than the average bill.
select p.name from appointments a
join patients p
on p.patient_id = a.patient_id
join bills b
on b.appointment_id = a.appointment_id
where b.amount > (select avg(amount) from bills);

-- Finds the doctor with maximum total appointments.
select d.name,count(a.appointment_id) tot_app from appointments a
join doctors d
on d.doctor_id = a.doctor_id
group by d.name
order by tot_app desc
limit 1;

-- Lists patients who still have unpaid (pending) bills.
select p.name from appointments a
join patients p
on p.patient_id = a.patient_id
join bills b
on b.appointment_id = a.appointment_id
where b.payment_status = 'Pending';

-- Shows appointments where the patient is older than average age.
select p.name,p.age from appointments a
join patients p
on p.patient_id = a.patient_id
where p.age > (select avg(age) from patients);

-- Returns the three largest bill amounts
select amount from bills order by amount desc limit 3;

-- Finds the busiest doctor and shows their appointments.
select a.* from appointments a
where a.doctor_id = (select doctor_id from appointments
group by doctor_id order by count(*) desc limit 1);


-- Shows patients whose combined bill value exceeds 2000
select p.name,sum(b.amount) as total_bill from appointments a
join patients p
on p.patient_id = a.patient_id
join bills b
on b.appointment_id = a.appointment_id
group by p.name
having sum(b.amount) > 2000;


-- =========================================== 
-- Session 6: CTEs
-- =========================================== 

-- Calculates each doctor’s appointment count and shows doctors with more than 5 appointments.
with tot_appointment as(
select d.name,count(appointment_id) tot_appoint from appointments a
join doctors d
on d.doctor_id = a.doctor_id
group by d.name
)
select * from tot_appointment 
where tot_appoint > 5;

-- Finds all bill amounts that are higher than the overall average.
with avg_bills as (
select amount from bills
where amount > (select avg(amount) from bills)
)
select * from avg_bills;

-- Filters bills for the given date using a CTE.
with on_7th as(
select * from bills b
where bill_date = '2025-01-07'
)
select * from on_7th;

-- Combines all three tables and shows complete appointment details.
with details as (
select a.*,d.name,b.* from appointments a
join doctors d
on d.doctor_id = a.doctor_id
join bills b
on b.appointment_id = a.appointment_id
)
select * from details;

-- Shows patients who consulted multiple different doctors.
with p_d as (
select p.name, count(distinct d.doctor_id) as doc_count
from appointments a
join patients p on p.patient_id = a.patient_id
join doctors d on d.doctor_id = a.doctor_id
group by p.name
having count(distinct d.doctor_id) > 1
)
select * from p_d;


-- =========================================== 
-- Session 7: WINDOW FUNCTIONS
-- =========================================== 

-- Gives each patient a sequence number based on name order.
select name,rank() over(order by name) as sequence from patients;

-- Numbers each patient's appointments starting from 1.
select p.name,a.appointment_id,
row_number() over(partition by p.patient_id order by a.appointment_date) rn
from appointments a
join patients p on p.patient_id = a.patient_id;

-- Shows previous bill value for comparison.
select amount,LAG(amount) over(order by amount) as prev_amount from bills;

-- Shows the upcoming appointment date for each entry.
select appointment_date,lead(appointment_date)
over(order by appointment_date) as next_date from appointments;

-- Divides patients into 5 Divisions.
select *,ntile(5) over(order by patient_id) as groups from patients;

-- Shows cumulative sum of bills sorted by date + bill id.
select amount,sum(amount) over(order by bill_date,bill_id) from bills;


-- =========================================== 
-- Session 8:  VIEW + PROCEDURE + ALTER
-- =========================================== 

-- Add a new column 'email' to the patients table.
ALTER TABLE patients
add column email varchar(40) default 'xyz@example.com';

-- Create view for patient, doctor, appointment, and bill – Combines patient name, doctor name, 
-- appointment date, and bill amount in a view.
create or replace view details as 
select p.name as pateint_name,d.name as docor_name,
a.appointment_date,b.amount
from appointments a
join patients p
on p.patient_id = a.patient_id
join doctors d
on d.doctor_id = a.doctor_id
join bills b
on b.appointment_id = a.appointment_id;

-- Stored procedure to insert a new doctor – 
-- Inserts a new doctor into the doctors table with given ID, name, specialization, and phone.
create or replace procedure new_doctor(
para1 int,para2 varchar(30),para3 varchar(40),para4 varchar(20)
)
language plpgsql
as $$
begin
insert into doctors(doctor_id,name,specialization,phone)
values(para1,para2,para3,para4);
end;
$$;
call new_doctor(31,'Dr.Rahul Mehta','Cardiologist','8945XX1056');

-- Create view for unpaid bills with patient details – Shows all patients who have bills with Pending status.
create or replace view patients_unpaid as 
select p.* from appointments a
join patients p
on p.patient_id = a.patient_id
join bills b
on b.appointment_id = a.appointment_id
where b.payment_status = 'Pending';

-- Alter doctors table to increase specialization length – 
-- Changes the specialization column to allow up to 80 characters.
alter table doctors
alter column specialization type varchar(80);

