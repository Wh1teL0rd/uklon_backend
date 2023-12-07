USE iot_db;

-- Drop the trigger if it already exists
DROP TRIGGER IF EXISTS `before_insert_Additional_Details`;

-- Trigger to ensure referential integrity
DELIMITER //
CREATE TRIGGER `before_insert_AdditionalDetails`
BEFORE INSERT ON `Additional_Details`
FOR EACH ROW
BEGIN
  DECLARE car_count INT;

  -- Check if the referenced carID exists in the Cars table
  SELECT COUNT(*) INTO car_count FROM Cars WHERE carID = NEW.carID;

  -- If the carID doesn't exist, prevent the insert
  IF car_count = 0 THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Cannot insert into AdditionalDetails. Invalid carID.';
  END IF;
END //
DELIMITER ;
