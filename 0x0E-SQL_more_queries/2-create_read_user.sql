-- a script that creates the database hbtn_0d_2 and the user user_0d_2
-- assigns password "user_0d_2_pwd" to user user_0d_2
-- gives select privilege to user on hbtn_0d_2 database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost'
