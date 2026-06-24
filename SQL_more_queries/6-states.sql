-- States table                                         
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa
AND IN hbtn_0d_usa CREATE TABLES IF NOT EXISTS states (
    id INT NOT NULL UNIQUE PRIMARY,
    name VARCHAR(256) NOT NULL
);
