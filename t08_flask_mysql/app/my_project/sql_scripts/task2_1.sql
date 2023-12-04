use iot_db;

DELIMITER //

CREATE PROCEDURE insert_additional_details_sp(
    IN p_detail_info VARCHAR(255),
    IN p_carID INT
)
BEGIN
    INSERT INTO AdditionalDetails (detail_info, carID)
    VALUES (p_detail_info, p_carID);
END //

DELIMITER ;