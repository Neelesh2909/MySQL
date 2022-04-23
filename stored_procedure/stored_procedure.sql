DELIMITER //
-- creating a parameterized stored procedure
CREATE PROCEDURE sp_GetStateByCountryId(country_id int)
BEGIN
	SELECT state_name FROM state WHERE FK_country_id = country_id;
END //

DELIMITER ;

CALL sp_GetStateByCountryId(1);


DROP PROCEDURE IF EXISTS sp_GetStateByCountryId;



DELIMITER $$
-- creating a non-parameterized stored procedure
CREATE PROCEDURE sp_GetAllStates()
BEGIN
	SELECT state_name FROM state;
END $$

DELIMITER ;

CALL sp_GetAllStates();


-- To drop a stored procedure
DROP PROCEDURE IF EXISTS sp_GetAllStates;