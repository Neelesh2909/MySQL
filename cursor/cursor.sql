delimiter //
create procedure spEmp()
begin
	-- variable to store the employee name and salary
	declare v_name varchar(50);
    declare v_salary int;
    -- variable to used to set the not found status
    declare v_finished integer default 0;
    -- declaring a cursor
	declare c1 cursor  for select emp_Name,emp_salary from tbl_employee;
    -- declare NOT FOUND handler to handle the situation when cursor could not find any row
    declare continue handler for NOT FOUND set v_finished=1;
	open c1;
    get_emp : loop
		-- fetch statement to retrieve the row pointed by cursor
		fetch c1 into v_name, v_salary;
        if v_finished = 1 then
			leave get_emp;
		end if;
        select concat(v_name,concat('-',v_salary));
	end loop get_emp;
    -- closing the cursor
    close c1;
end //

delimiter ;

call spEmp();

drop procedure spEmp;