select * from state where country_id = 1;

-- To create an index
CREATE INDEX con_id ON state(country_id);

-- To see the indexes of a table
SHOW INDEX FROM state;

-- To drop an existing index from a table
DROP INDEX con_id ON  state;