CREATE TABLE IF NOT EXISTS results (
    pk INT PRIMARY KEY AUTO_INCREMENT,
    magicNumber INT(10) NOT NULL,
    lottoDraw INT(10) NOT NULL,
    prize VARCHAR(10) NOT NULL
);