CREATE TABLE doctors(
doctor_id serial primary key,
name varchar(40) not null,
specialization varchar(80) not null,
phone varchar(20) check(length(phone)=10)
);

insert into doctors(doctor_id,name,specialization,phone)
values
(1, 'Dr. Arvind Kapoor', 'Cardiologist', '98764XXX01'),
(2, 'Dr. Meera Nambiar', 'Dermatologist', '98764XXX02'),
(3, 'Dr. Rohan Khanna', 'Neurologist', '98764XXX03'),
(4, 'Dr. Priya Subramaniam', 'Pediatrician', '98764XXX04'),
(5, 'Dr. Siddharth Rao', 'Orthopedic', '98764XXX05'),
(6, 'Dr. Anjali Mathur', 'Gynecologist', '98764XXX06'),
(7, 'Dr. Harshvardhan Singh', 'General Physician', '98764XXX07'),
(8, 'Dr. Kavita Sharma', 'Dentist', '98764XXX08'),
(9, 'Dr. Manish Kulkarni', 'Urologist', '98764XXX09'),
(10, 'Dr. Nisha Paul', 'ENT Specialist', '98764XXX10'),
(11, 'Dr. Arjun Thakur', 'Cardiologist', '98764XXX11'),
(12, 'Dr. Ritu Menon', 'Dermatologist', '98764XXX12'),
(13, 'Dr. Karan Behl', 'Neurologist', '98764XXX13'),
(14, 'Dr. Poonam Kaur', 'Pediatrician', '98764XXX14'),
(15, 'Dr. Nishant Arora', 'Orthopedic', '98764XXX15'),
(16, 'Dr. Sneha Bedi', 'Gynecologist', '98764XXX16'),
(17, 'Dr. Uday Pratap', 'General Physician', '98764XXX17'),
(18, 'Dr. Tanya Pillai', 'Dentist', '98764XXX18'),
(19, 'Dr. Mohan Shetty', 'Urologist', '98764XXX19'),
(20, 'Dr. Sujata Rathod', 'ENT Specialist', '98764XXX20'),
(21, 'Dr. Vipul Mehta', 'Cardiologist', '98764XXX21'),
(22, 'Dr. Garima Sethi', 'Dermatologist', '98764XXX22'),
(23, 'Dr. Rohit Suri', 'Neurologist', '98764XXX23'),
(24, 'Dr. Aastha Jain', 'Pediatrician', '98764XXX24'),
(25, 'Dr. Virat Verma', 'Orthopedic', '98764XXX25'),
(26, 'Dr. Shruti Kulkarni', 'Gynecologist', '98764XXX26'),
(27, 'Dr. Sameer Desai', 'General Physician', '98764XXX27'),
(28, 'Dr. Radhika Kapoor', 'Dentist', '98764XXX28'),
(29, 'Dr. Dhruv Nanda', 'Urologist', '98764XXX29'),
(30, 'Dr. Shilpa Chawla', 'ENT Specialist', '98764XXX30');
