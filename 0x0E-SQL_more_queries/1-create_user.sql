-- Creates the user user_0d_1 possessing all privileges.
-- FLUSH func does a reload of the privileges from the grant tables in the database.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
