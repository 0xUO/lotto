CREATE TABLE IF NOT EXISTS results (
    pk INT PRIMARY KEY AUTO_INCREMENT,
    magicNumber VARCHAR(10) NOT NULL,
    lottoDraw VARCHAR(20) NOT NULL,
    prize INT(10) NOT NULL
);