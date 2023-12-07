INSERT INTO Users (first_name, last_name, email, password, credit_card_number, current_location)
VALUES
    ('John', 'Doe', 'johndoe@example.com', 'password123', '1234567890123456', 'New York'),
    ('Alice', 'Smith', 'alicesmith@example.com', 'passw0rd', '9876543210987654', 'Los Angeles'),
    ('Michael', 'Johnson', 'michael@example.com', 'securepass', '1111222233334444', 'Chicago'),
    ('Emily', 'Davis', 'emily@example.com', 'letmein', '5555666677778888', 'San Francisco'),
    ('David', 'Brown', 'david@example.com', 'myp@ss', '9999888877776666', 'Houston'),
    ('Sarah', 'Wilson', 'sarah@example.com', 'p@ssw0rd', '1234432112344321', 'Miami'),
    ('Robert', 'Lee', 'robert@example.com', '123456', '1010101010101010', 'Boston'),
    ('Jennifer', 'White', 'jennifer@example.com', 'qwerty', '5555555555555555', 'Seattle'),
    ('William', 'Anderson', 'william@example.com', 'letmein123', '7777666655554444', 'Phoenix'),
    ('Linda', 'Martinez', 'linda@example.com', 'password1234', '1212121212121212', 'Denver');

INSERT INTO Cars (model, year, licence_plate, car_type)
VALUES
    ('Toyota Camry', 2022, 'ABC123', 'Sedan'),
    ('Honda Civic', 2021, 'XYZ789', 'Sedan'),
    ('Ford Explorer', 2023, 'DEF456', 'SUV'),
    ('Chevrolet Malibu', 2022, 'GHI789', 'Sedan'),
    ('Jeep Wrangler', 2020, 'JKL012', 'SUV'),
    ('Nissan Altima', 2021, 'MNO345', 'Sedan'),
    ('BMW X5', 2022, 'PQR678', 'SUV'),
    ('Hyundai Elantra', 2023, 'STU901', 'Sedan'),
    ('Mercedes-Benz E-Class', 2021, 'VWX234', 'Sedan'),
    ('Audi Q7', 2023, 'YZA567', 'SUV');

INSERT INTO Drivers (first_name, last_name, contact_number, car_id)
VALUES
    ('Michael', 'Johnson', '+1234567890', 1),
    ('Emily', 'Davis', '+9876543210', 2),
    ('David', 'Brown', '+1112223333', 3),
    ('Sarah', 'Wilson', '+4445556666', 4),
    ('Robert', 'Lee', '+7778889999', 5),
    ('Jennifer', 'White', '+5555555555', 6),
    ('William', 'Anderson', '+9999888777', 7),
    ('Linda', 'Martinez', '+1212121212', 8),
    ('Thomas', 'Harris', '+3333444455', 9),
    ('Karen', 'Moore', '+6666777888', 10);

INSERT INTO Orders (user_id, drivers_id, car_id, date, start_point, end_point)
VALUES
    (1, 1, 1, '2023-09-25 10:00:00', '123 Main St', '456 Elm St'),
    (2, 2, 2, '2023-09-26 15:30:00', '789 Oak St', '321 Pine St'),
    (3, 3, 3, '2023-09-27 14:15:00', '567 Maple St', '789 Birch St'),
    (4, 4, 4, '2023-09-28 11:45:00', '222 Oak St', '333 Pine St'),
    (5, 5, 5, '2023-09-29 09:30:00', '111 Elm St', '444 Cedar St'),
    (6, 6, 6, '2023-09-30 12:30:00', '777 Willow St', '888 Palm St'),
    (7, 7, 7, '2023-10-01 16:00:00', '555 Pine St', '666 Oak St'),
    (8, 8, 8, '2023-10-02 08:45:00', '123 Maple St', '999 Birch St'),
    (9, 9, 9, '2023-10-03 13:20:00', '444 Oak St', '111 Elm St'),
    (10, 10, 10, '2023-10-04 17:30:00', '222 Willow St', '555 Cedar St');

INSERT INTO DriverRatings (rating, Orders_ordersID)
VALUES
    (5, 1),
    (4, 2),
    (4, 3),
    (5, 4),
    (3, 5),
    (4, 6),
    (5, 7),
    (3, 8),
    (4, 9),
    (5, 10);

INSERT INTO UserRatings (rating, Orders_ordersID)
VALUES
    (4, 1),
    (5, 2),
    (4, 3),
    (5, 4),
    (3, 5),
    (4, 6),
    (5, 7),
    (3, 8),
    (4, 9),
    (5, 10);

INSERT INTO ExtraOrderDetails (details, Orders_ordersID)
VALUES
    ('Additional luggage required', 1),
    ('Child seat needed', 2),
    ('Pet-friendly driver required', 3),
    ('Non-smoking vehicle needed', 4),
    ('Special dietary requests for snacks', 5),
    ('Multiple stops along the way', 6),
    ('Driver should speak Spanish', 7),
    ('Driver should be punctual', 8),
    ('Driver should have a good knowledge of local attractions', 9),
    ('Music preferences for the ride', 10);