-- Creates the table unique_id on the MySQL server.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256),
    UNIQUE id
);