-- Use the database
USE hbtn_0d_usa;

-- Create table cities if it does not exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT cities_ibfk_1 FOREIGN KEY (state_id) REFERENCES states(id)
);
