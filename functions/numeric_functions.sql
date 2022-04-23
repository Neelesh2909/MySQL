-- It returns the absolute value
SELECT ABS(-40);
SELECT ABS(40);

-- It returns the square root of the value
SELECT SQRT(25);

-- It returns the remainder 
SELECT MOD(10,3);

-- It returns the a to power of b
SELECT POWER(2,5);

-- It truncates a number to the specified number of decimal places
SELECT TRUNCATE(40.1234,3);
SELECT TRUNCATE(40.1234,2);
SELECT TRUNCATE(6876,-1);
SELECT TRUNCATE(6876,-2);
SELECT TRUNCATE(68763456,-5);

-- It returns the greatest value in the provided values
SELECT GREATEST(300,250,500,100,400);

-- It returns the least value in the provided values
SELECT LEAST(300,250,500,100,400);

-- 	Return the smallest integer value not less than the argument
SELECT CEILING(1.23);
SELECT CEILING(-1.23);

-- 	Returns the value of e (the base of natural logarithms) raised to the power of X
SELECT EXP(2);

-- Return the largest integer value not greater than the argument
SELECT FLOOR(1.23);

-- 	Return the natural logarithm of the first argument
SELECT LOG(2);

-- 	Return the base-10 logarithm of the argument
SELECT LOG10(2);

-- Return the base-2 logarithm of the argument
SELECT LOG2(65536);

-- Return the value of pi
SELECT PI();

-- 	Return a random floating-point value
SELECT RAND();

-- Return the cosine
SELECT COS(PI());

-- 	Return the cotangent
SELECT COT(12);

-- 	Return the sine of the argument
SELECT SIN(PI());

-- 	Return the tangent of the argument
SELECT TAN(PI());