CREATE TABLE suppliers(
supplier_id serial primary key,
name varchar(40) not null,
contact_email varchar(40) unique not null,
city varchar(30) not null
);

INSERT INTO suppliers(name,contact_email,city)
values
('Fresh Farms', 'freshfarms@example.com', 'Seattle'),
('Healthy Foods', 'healthyfoods@mail.com', 'Austin'),
('Organic Supplies', 'organic@xyz.com', 'Denver'),
('Natures Basket', 'naturesbasket@gmail.com', 'San Francisco'),
('Green Valley', 'greenvalley@mail.com', 'Portland'),
('Sunshine Produce', 'sunshine@example.com', 'Los Angeles'),
('Farm Fresh', 'farmfresh@mail.com', 'Chicago'),
('Pure Organics', 'pureorganics@gmail.com', 'New York'),
('Eco Farms', 'ecofarms@example.com', 'Miami'),
('Good Harvest', 'goodharvest@mail.com', 'Houston'),
('Healthy Choice', 'healthychoice@gmail.com', 'Boston'),
('Natural Picks', 'naturalpicks@example.com', 'San Diego'),
('Fresh & Organic', 'freshorganic@mail.com', 'Phoenix'),
('Green Fields', 'greenfields@gmail.com', 'Denver'),
('Harvest Time', 'harvesttime@example.com', 'Seattle'),
('Organic Roots', 'organicroots@mail.com', 'Austin'),
('SunFarm', 'sunfarm@gmail.com', 'Los Angeles'),
('Nature Select', 'natureselect@example.com', 'Chicago'),
('Vital Farms', 'vitalfarms@mail.com', 'New York'),
('Earths Best', 'earthsbest@gmail.com', 'Portland');