CREATE DATABASE triggers;
USE triggers;
Show Tables;


create table customers
(cust_id int, age int, name varchar(30));


-- before insert trigger
delimiter // 
create trigger age_verify
before insert on customers
for each row
if new.age < 0 then set new.age = 0;
end if;//

insert into customers
values (101,27,'Neelesh'),
(102,-40,'Mayank'),
(103,32,'Jitesh'),
(104,-32,'Shikha');

select * from customers;




drop table customers;

-- after insert trigger 

create table customer1(
id int auto_increment primary key,
name varchar(40) not null,
email varchar(30),
birthdate date);

create table message(
id int auto_increment,
messageId int,
message varchar(300) not null,
primary key(id,messageId));

Delimiter //
create trigger check_null_dob
after insert on customer1
for each row
begin 
if new.birthdate is null then
insert into message (messageId, message)
values(new.id, concat('Hi ', new.name, ', please update your date of birth.'));
end if;
end //
delimiter ;

insert into customer1(name,email,birthdate)
values("Nancy","nancy@abc.com",NULL),
("James","james@xyz.com","1998-11-16"),
("Javed","javed@qwe.com","1997-08-20"),
("Ankit","ankyy@rty.com",NULL);

SELECT * FROM message;

drop table customer1;
drop table message;

create table employees
(emp_id int primary key,
emp_name varchar(25),
age int,
salary float);

insert into employees
values(101,'Neelesh',26,70000),
(102,'Mayank',29,55000),
(103,'Nischal',30,62000),
(104,'Vartika',22,57000),
(105,'Ahmed',31,80000),
(106,'Sid',40,100000);


-- before update trigger
delimiter //
create trigger update_trigger
before update
on employees
for each row
begin
if new.salary = 10000 then 
set new.salary = 70000;
elseif new.salary < 10000 then
set new.salary = 72000;
end if;
end //
delimiter ;


update employees
set salary = 8000;

select * from employees;
drop table employees;


-- before delete trigger
create table salary(
eid int primary key,
validfrom date not null,
amount float not null);

insert into salary(eid, validfrom, amount)
values (101, '2005-05-01', 55000),
(102, '2007-08-01', 68000),
(103, '2006-09-01', 75000);

select * from salary;

create table salarydel(
id int primary key auto_increment,
eid int,
validfrom date not null,
amount float not null,
deletedat timestamp default now());

delimiter $$
create trigger salary_delete
before delete
on salary
for each row
begin
insert into salarydel(eid, validfrom, amount)
values (old.eid, old.validfrom, old.amount);
end $$

delimiter ;

delete from salary
where eid = 103;

select * from salarydel;

drop table salary;
drop table salarydel;
