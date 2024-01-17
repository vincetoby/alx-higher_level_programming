# READ ME

## Getting started with your SQL
**Install MySQL 8.0 on Ubuntu 20.04 LTS**

<pre><code>
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
</pre></code>


**Connect to your MySQL server:**
<pre><code>
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.
Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
</pre></code>

**Use “container-on-demand” to run MySQL**

In the container, credentials are root/root

    * Ask for container Ubuntu 20.04
    * Connect via SSH
    * OR connect via the Web terminal
    * In the container, you should start MySQL before playing with it:
<pre><code>
$ service mysql start
 * Starting MySQL database server mysqld
$
$ cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema
sys
$
</pre></code>

## RUNNING THE FILES
<pre><code>cat file.sql | mysql -hlocalhost -uroot -p hbtn_0c_0</pre></code>
where file.sql is the file(script) and hbtn_0c_0 is the database

## FILES CONTAINING IMPORTANT CODES RELATED TO mySQL

### 0-list_databases.sql:
a script that lists all databases of your MySQL server

### 1-create_database_if_missing.sql:
a script that creates the database hbtn_0c_0 in your MySQL server.

    * If the database hbtn_0c_0 already exists, your script should not fail
    *You are not allowed to use the SELECT or SHOW statements

### 2-remove_database.sql:
a script that deletes the database hbtn_0c_0 in your MySQL server.

    * If the database hbtn_0c_0 doesn’t exist, your script should not fail
    * You are not allowed to use the SELECT or SHOW statements

### 3-list_tables.sql:
a script that lists all the tables of a database in your MySQL server.

    * The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)

### 4-first_table.sql:
a script that creates a table called first_table in the current database in your MySQL server.

    * first_table description:
        * id INT
        * name VARCHAR(256)
    * The database name will be passed as an argument of the mysql command
    * If the table first_table already exists, your script should not fail
    * You are not allowed to use the SELECT or SHOW statements

### 5-full_table.sql:
a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

    * The database name will be passed as an argument of the mysql command
    * You are not allowed to use the DESCRIBE or EXPLAIN statements

### 6-list_values.sql:
a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

    * All fields should be printed
    * The database name will be passed as an argument of the mysql command

### 7-insert_value.sql:
 a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
 
    * New row:
        * id = 89
        * name = Best School
    * The database name will be passed as an argument of the mysql command

### 8-count_89.sql:
a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

    * The database name will be passed as an argument of the mysql command
 
### 9-full_creation.sql:
a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

    * second_table description:
        id INT
        name VARCHAR(256)
        score INT
    * The database name will be passed as an argument to the mysql command
    * If the table second_table already exists, your script should not fail
    * You are not allowed to use the SELECT and SHOW statements
    * Your script should create these records:
        id = 1, name = “John”, score = 10
        id = 2, name = “Alex”, score = 3
        id = 3, name = “Bob”, score = 14
        id = 4, name = “George”, score = 8

### 10-top_score.sql:
a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

    * Results should display both the score and the name (in this order)
    * Records should be ordered by score (top first)
    * The database name will be passed as an argument of the mysql command

### 11-best_score.sql:
a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

    * Results should display both the score and the name (in this order)
    * Records should be ordered by score (top first)
    * The database name will be passed as an argument of the mysql command

### 12-no_cheating.sql:
a script that updates the score of Bob to 10 in the table second_table.

    * You are not allowed to use Bob’s id value, only the name field
    * The database name will be passed as an argument of the mysql command

### 13-change_class.sql:
a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

    * The database name will be passed as an argument of the mysql command
<pre><code>
guillaume@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
guillaume@ubuntu:~/$ 
</pre></code>

### 14-average.sql:
a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

    * The result column name should be average
    * The database name will be passed as an argument of the mysql command
<pre><code>
guillaume@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
average
9.3333
guillaume@ubuntu:~/$ 
</pre></code>

### 15-groups.sql:
a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

    * The result should display:
        * the score
        * the number of records for this score with the label number
    * The list should be sorted by the number of records (descending)
    * The database name will be passed as an argument to the mysql command
<pre><code>
guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   number
10  2
8   1
guillaume@ubuntu:~/$ 
</pre></code>

### 16-no_link.sql:
a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

    * Don’t list rows without a name value
    * Results should display the score and the name (in this order)
    * Records should be listed by descending score
    * The database name will be passed as an argument to the mysql command

In this example, new data have been added to the table second_table.

<pre><code>
guillaume@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
18  Aria
12  Aria
10  John
10  Bob
guillaume@ubuntu:~/$ 
</pre></code>

### 100-move_to_utf8.sql:
a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

You need to convert all of the following to UTF8:

    * Database hbtn_0c_0
    * Table first_table
    * Field name in first_table
<pre><code>
guillaume@ubuntu:~/$ cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p 
Enter password: 
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table
first_table CREATE TABLE `first_table` (\n  `id` int(11) DEFAULT NULL,\n  `name` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
guillaume@ubuntu:~/$ 
</pre></code>

### 101-avg_temperatures.sql:
Import in hbtn_0c_0 database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql)

a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
<pre><code>
guillaume@ubuntu:~/$ cat 101-avg_temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
city    avg_temp
Chandler    72.8627
Gilbert 71.8088
Pismo beach 71.5147
San Francisco   71.4804
Sedona  70.7696
Phoenix 70.5882
Oakland 70.5637
Sunnyvale   70.5245
Chicago 70.4461
San Diego   70.1373
Glendale    70.1225
Sonoma  70.0392
Yuma    69.3873
San Jose    69.2990
Tucson  69.0245
Joliet  68.6716
Naperville  68.1029
Tempe   67.0441
Peoria  66.5392
guillaume@ubuntu:~/$ 
</pre></code>

### 102-top_city.sql:
a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
<pre><code>
guillaume@ubuntu:~/$ cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
city    avg_temp
Naperville  76.9412
San Diego   73.7941
Sunnyvale   73.2353
guillaume@ubuntu:~/$ 
</pre></code>

### 103-max_state.sql:
a script that displays the max temperature of each state (ordered by State name).

</pre></code>
guillaume@ubuntu:~/$ cat 103-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
state   max_temp
AZ  110
CA  110
IL  110
guillaume@ubuntu:~/$ 
</pre></code> 
