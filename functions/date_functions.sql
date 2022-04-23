-- It returns the current date
SELECT CURDATE();
SELECT CURRENT_DATE();

-- It returns the current time
SELECT CURTIME();
SELECT CURRENT_TIME();

-- It returns the current date and time
SELECT NOW();
SELECT SYSDATE();

-- It returns the month part for a give date
SELECT MONTH("2019-04-19");

-- It returns the year part for a give date
SELECT YEAR("2019-04-19");

-- It returns the day part for a give date
SELECT DAY("2019-04-19");

-- 	Add time values (intervals) to a date value
SELECT ADDDATE('2008-01-02', INTERVAL 45 DAY);

-- Add time
SELECT ADDTIME('01:00:00.999999', '02:00:00.999998');

-- 	Extract the date part of a date or datetime expression
SELECT DATE('2003-12-31 01:02:03');

-- Add time values (intervals) to a date value
SELECT DATE_ADD('2018-05-01',INTERVAL 1 DAY);

-- 	Subtract a time value (interval) from a date
SELECT DATE_SUB('2018-05-01',INTERVAL 1 YEAR);

-- Subtract two dates
SELECT DATEDIFF('2007-12-31 23:59:59','2007-12-20');

-- Format date as specified
SELECT DATE_FORMAT('2009-10-04 22:23:00', '%W %M %Y');
SELECT DATE_FORMAT('2007-10-04 22:23:00', '%H:%i:%s');

-- Return the name of the weekday
SELECT DAYNAME('2007-02-03');

-- Return the day of the month (0-31)
SELECT DAYOFMONTH('2007-02-03');

-- Return the weekday index of the argument(1 = Sunday, 2 = Monday, …, 7 = Saturday).
SELECT DAYOFWEEK('2007-02-04');

-- 	Return the day of the year (1-366)
SELECT DAYOFYEAR('2007-02-03');

-- Extract part of a date
SELECT EXTRACT(YEAR FROM '2019-07-02');
SELECT EXTRACT(YEAR_MONTH FROM '2019-07-02 01:02:03');

-- 	Extract the hour
SELECT HOUR('10:05:03');

-- Return the last day of the month for the argument
SELECT LAST_DAY('2003-02-05');

-- Return the name of the month
SELECT MONTHNAME('2008-02-03');

-- 	Extract the time portion of the expression passed
SELECT TIME('2003-12-31 01:02:03');

-- 	Subtract time
SELECT TIMEDIFF('2000:01:01 00:00:00','2000:01:01 00:00:00.000001');

-- 	Return the calendar week of the date (1-53)
SELECT WEEKOFYEAR('2008-02-20');