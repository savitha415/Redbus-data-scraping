create database redbus_datas;
use redbus_datas;
CREATE TABLE bus_details (
    Route VARCHAR(255),
    Bus_Name VARCHAR(255),
    Bus_Type VARCHAR(255),
    Departing_Time TIME,
    Reaching_Time TIME,
    Duration VARCHAR(255),
    Star_Rating FLOAT,
    Price FLOAT,
    Seats_Availability FLOAT
);
select * from bus_details;
show columns from bus_details;
ALTER TABLE bus_details
ADD COLUMN AC_Type VARCHAR(255),
ADD COLUMN Seat_Type VARCHAR(255);
UPDATE bus_details
SET
    AC_Type = SUBSTRING_INDEX(SUBSTRING_INDEX(Bus_Type, '(', -1), ' ', 1),
    Seat_Type = SUBSTRING_INDEX(SUBSTRING_INDEX(SUBSTRING_INDEX(Bus_Type, '(', -1), ',', -1), ')', 1);
SET SQL_SAFE_UPDATES = 1;
select * from bus_details;
select distinct AC_Type from bus_details;
set sql_safe_updates=0;
UPDATE bus_details
SET
    AC_Type = CASE
        WHEN Bus_Type LIKE '%AC%' AND Bus_Type NOT LIKE '%NON-AC%' THEN 'AC'
        WHEN Bus_Type LIKE '%NON-AC%' THEN 'NON-AC'
        ELSE NULL
    END
WHERE AC_Type IS NULL;  -- Update only if AC_Type is currently NULL or not set
set sql_safe_updates=1;
select distinct AC_Type from bus_details;

select * from bus_details_backups;
set sql_safe_updates=0;

CREATE TABLE temp_table AS
SELECT DISTINCT Link, Route, Bus_Name, Bus_Type, Departing_Time, Reaching_Time, Duration, Star_Rating, Price, Seats_Availability, From_City, To_City
FROM bus_details;

TRUNCATE TABLE bus_details;

INSERT INTO bus_details (Link, Route, Bus_Name, Bus_Type, Departing_Time, Reaching_Time, Duration, Star_Rating, Price, Seats_Availability, From_City, To_City)
SELECT * FROM temp_table;

DROP TABLE temp_table;


select * from bus_details;

select distinct from_city from bus_details where to_city='chennai';







