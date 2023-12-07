USE iot_db;

DELIMITER //

CREATE TRIGGER check_rating_value
BEFORE INSERT ON driver_ratings
FOR EACH ROW
BEGIN
    IF NEW.rating IS NULL OR
       NEW.rating < 1 OR
       NEW.rating > 5 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid value for rating. Must be between 1 and 5.';
    END IF;
END //

DELIMITER ;
