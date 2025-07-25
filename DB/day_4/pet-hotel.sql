CREATE DATABASE day_4;
USE day_4;

-- 반려동물 호텔 예약 시스템 DB를 설계해봅시다 !!! 
-- 문제 1. 각 테이블에 어떤 정보가 필요할지 먼저 생각해보고, 아래 요구사항을 확인하여 ERD 를 그려주세요.

-- 반려동물 주인
CREATE TABLE PetOwners(
	ownerID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    contact INT
    );
    
-- 반려동물
CREATE TABLE Pets(
	petID INT PRIMARY KEY AUTO_INCREMENT,
	ownerID INT,
    species VARCHAR(100),
    breed VARCHAR(100),
    FOREIGN KEY (ownerID) REFERENCES PetOwners (ownerID)
    );
    
    -- 객실
CREATE TABLE Rooms(
	roomID INT PRIMARY KEY AUTO_INCREMENT,
	roomNumber INT,
    roomType ENUM('standard','double','dyrux','sweet'),
	pricePerNight INT
    );
    
-- 예약
CREATE TABLE Reservations(
	reservationID INT PRIMARY KEY AUTO_INCREMENT,
    petID INT,
    roomID INT,
    startDate DATETIME,
    endDate DATETIME,
    FOREIGN KEY (petID) REFERENCES Pets(petID),
    FOREIGN KEY (roomID) REFERENCES Rooms(roomID)
    );
    
-- 서비스
CREATE TABLE Services(
	serviceID INT PRIMARY KEY AUTO_INCREMENT,
    reservationID INT,
    serviceName VARCHAR(100),
    servicePrice INT,
    FOREIGN KEY (reservationID) REFERENCES Reservations(reservationID)
    );