-- Drop existing tables (if needed)
DROP TABLE Tourists CASCADE CONSTRAINTS;
DROP TABLE Destinations CASCADE CONSTRAINTS;
DROP TABLE Bookings CASCADE CONSTRAINTS;

-- Create Tourists Table
CREATE TABLE Tourists (
    tourist_id varchar(10) ,
    name VARCHAR2(100),
    email VARCHAR2(100),
    phone_number VARCHAR2(20),
    nationality VARCHAR2(50),
    address VARCHAR2(255)
);
 
-- Create Destinations Table
CREATE TABLE Destinations (
    destination_id VARCHAR2(20),
    name VARCHAR2(100),
    description VARCHAR2(255),
    city VARCHAR2(50),
    country VARCHAR2(50),
    cost_per_day NUMBER(10, 2)
);

-- Create Bookings Table
CREATE TABLE Bookings (
    booking_id varchar(20),
    tourist_id varchar(10),
    destination_id VARCHAR2(20),
    check_in_date DATE,
    check_out_date DATE,
    total_cost DECIMAL(10, 2)
);



-- Add primary key and foreign key constraints using ALTER TABLE
ALTER TABLE Tourists
ADD CONSTRAINT pk_tourist_id PRIMARY KEY (tourist_id);

ALTER TABLE Bookings
ADD CONSTRAINT pk_booking_id PRIMARY KEY (booking_id);

ALTER TABLE Destinations
ADD CONSTRAINT pk_destination_id PRIMARY KEY (destination_id);



ALTER TABLE Bookings
ADD CONSTRAINT fk_tourist_id
FOREIGN KEY (tourist_id) REFERENCES Tourists(tourist_id);


ALTER TABLE Bookings
ADD CONSTRAINT fk_destination
FOREIGN KEY (destination_id) REFERENCES Destinations(destination_id);



-- Inserting into Tourists table
INSERT INTO Tourists (tourist_id, name, email, phone_number, nationality, address, team_id)
VALUES (1, 'John Doe', 'john@example.com', '123-456-7890', 'USA', '123 Main St, Anytown', 101);

INSERT INTO Tourists (tourist_id, name, email, phone_number, nationality, address, team_id)
VALUES (2, 'Jane Smith', 'jane@example.com', '987-654-3210', 'Canada', '456 Elm St, Othertown', 102);

INSERT INTO Tourists (tourist_id, name, email, phone_number, nationality, address, team_id)
VALUES (3, 'Alice Johnson', 'alice@example.com', '555-123-7777', 'UK', '789 Oak St, Differenttown', 103);

INSERT INTO Tourists (tourist_id, name, email, phone_number, nationality, address, team_id)
VALUES (4, 'Bob Brown', 'bob@example.com', '111-222-3333', 'Australia', '999 Pine St, Newtown', 104);

INSERT INTO Tourists (tourist_id, name, email, phone_number, nationality, address, team_id_id)
VALUES (5, 'Eva Garcia', 'eva@example.com', '444-555-6666', 'Spain', '111 Cedar St, Anycity', NULL);

-- Inserting into Destinations table
INSERT INTO Destinations (destination_id, name, description, location, cost_per_day)
VALUES ('D001', 'Beach Resort', 'Beautiful beachside resort', 'Tropical Island', 200.00);

INSERT INTO Destinations (destination_id, name, description, location, cost_per_day)
VALUES ('D002', 'Mountain Lodge', 'Scenic mountain retreat', 'Alpine Region', 150.00);

INSERT INTO Destinations (destination_id, name, description, location, cost_per_day)
VALUES ('D003', 'City View Hotel', 'Cityscape view hotel', 'Metropolitan City', 180.00);

INSERT INTO Destinations (destination_id, name, description, location, cost_per_day)
VALUES ('D004', 'Historical Landmark', 'Ancient historical site', 'Cultural Region', 100.00);

INSERT INTO Destinations (destination_id, name, description, location, cost_per_day)
VALUES ('D005', 'Safari Adventure', 'Wildlife exploration', 'Savanna Plains', 300.00);

-- Inserting into Bookings table
INSERT INTO Bookings (booking_id, tourist_id, destination_id, check_in_date, check_out_date, total_cost)
VALUES (101, 1, 'D001', TO_DATE('2023-12-01', 'YYYY-MM-DD'), TO_DATE('2023-12-07', 'YYYY-MM-DD'), 1200.00);

INSERT INTO Bookings (booking_id, tourist_id, destination_id, check_in_date, check_out_date, total_cost)
VALUES (102, 2, 'D002', TO_DATE('2023-11-25', 'YYYY-MM-DD'), TO_DATE('2023-11-30', 'YYYY-MM-DD'), 750.00);

INSERT INTO Bookings (booking_id, tourist_id, destination_id, check_in_date, check_out_date, total_cost)
VALUES (103, 3, 'D003', TO_DATE('2023-12-10', 'YYYY-MM-DD'), TO_DATE('2023-12-15', 'YYYY-MM-DD'), 900.00);

INSERT INTO Bookings (booking_id, tourist_id, destination_id, check_in_date, check_out_date, total_cost)
VALUES (104, 4, 'D004', TO_DATE('2023-11-20', 'YYYY-MM-DD'), TO_DATE('2023-11-25', 'YYYY-MM-DD'), 500.00);

INSERT INTO Bookings (booking_id, tourist_id, destination_id, check_in_date, check_out_date, total_cost)
VALUES (105, 5, 'D005', TO_DATE('2023-12-05', 'YYYY-MM-DD'), TO_DATE('2023-12-12', 'YYYY-MM-DD'), 2100.00);

-- Inserting into TourGuides table
-- Insert into Bookings Table with corrected date formats for all rows
INSERT INTO Bookings (booking_id, tourist_id, destination_id, check_in_date, check_out_date, total_cost, team_id)
VALUES (1, 1, 'D1', TO_DATE('2023-12-01', 'YYYY-MM-DD'), TO_DATE('2023-12-05', 'YYYY-MM-DD'), 600.00, 'A');

INSERT INTO Bookings (booking_id, tourist_id, destination_id, check_in_date, check_out_date, total_cost, team_id)
VALUES (2, 2, 'D2', TO_DATE('2023-12-10', 'YYYY-MM-DD'), TO_DATE('2023-12-15', 'YYYY-MM-DD'), 1000.00, 'B');

INSERT INTO Bookings (booking_id, tourist_id, destination_id, check_in_date, check_out_date, total_cost, team_id)
VALUES (3, 3, 'D3', TO_DATE('2023-12-20', 'YYYY-MM-DD'), TO_DATE('2023-12-25', 'YYYY-MM-DD'), 900.00, 'C');

INSERT INTO Bookings (booking_id, tourist_id, destination_id, check_in_date, check_out_date, total_cost, team_id)
VALUES (4, 4, 'D4', TO_DATE('2023-12-05', 'YYYY-MM-DD'), TO_DATE('2023-12-10', 'YYYY-MM-DD'), 850.00, 'A');

INSERT INTO Bookings (booking_id, tourist_id, destination_id, check_in_date, check_out_date, total_cost, team_id)
VALUES (5, 5, 'D5', TO_DATE('2023-12-28', 'YYYY-MM-DD'), TO_DATE('2024-01-02', 'YYYY-MM-DD'), 800.00, 'B');

