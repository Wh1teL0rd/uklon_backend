USE iot_db;

DELIMITER //

CREATE TRIGGER check_year_value
BEFORE INSERT ON cars
FOR EACH ROW
BEGIN
    IF NEW.year IS NULL OR
       NEW.year < 1000 OR
       NEW.year >= 10000 OR
       NEW.year = 0 OR
       NEW.year > 2024 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid value for year';
    END IF;
END //

DELIMITER ;
