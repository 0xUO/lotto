CREATE DATABASE IF NOT EXISTS lotto;
USE lotto;
CREATE TABLE IF NOT EXISTS results (
    pk INT PRIMARY KEY AUTO_INCREMENT,
    lottoDraw INT(10) NOT NULL,
    prize VARCHAR(10) NOT NULL
);