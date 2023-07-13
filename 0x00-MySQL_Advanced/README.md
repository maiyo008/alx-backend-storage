# 0x00-MySQL_Advanced
----
## Resources
**Read or watch:**

* [MySQL cheatsheet](https://devhints.io/mysql)
* [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.liquidweb.com/kb/mysql-optimization-how-to-leverage-mysql-database-indexing/)
* [Stored Procedure](https://www.w3resource.com/mysql/mysql-procedure.php)
* [Triggers](https://www.w3resource.com/mysql/mysql-triggers.php)
* [Views](https://www.w3resource.com/mysql/mysql-views.php)
* [Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
* [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
* [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
* [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
* [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
* [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
* How to create tables with constraints
* How to optimize queries by adding indexes
* What is and how to implement stored procedures and functions in MySQL
* What is and how to implement views in MySQL
* What is and how to implement triggers in MySQL

## More Info
Comments for your SQL file:
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
Use “container-on-demand” to run MySQL
Ask for container Ubuntu 18.04 - Python 3.7
Connect via SSH
Or via the WebTerminal
In the container, you should start MySQL before playing with it:
```
$ service mysql start
 * MySQL Community Server 5.7.30 is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$
```
In the container, credentials are root/root

How to import a SQL dump
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

## Tasks

### Tasks 0. We are all unique!
<Details>
Write a SQL script that creates a table users following these requirements:

With these attributes:
* id, integer, never null, auto increment and primary key
* email, string (255 characters), never null and unique
* name, string (255 characters)
If the table already exists, your script should not fail
Your script can be executed on any database
Context: Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application

```
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# cat 0-uniq_users.sql | mysql -uroot -p holberton
Enter password: 
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");' | mysql -uroot -p holberton
Enter password: 
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# echo 'INSERT INTO users (email, name) VALUES ("sylvie@dylan.com", "Sylvie");' | mysql -uroot -p holberton
Enter password: 
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# echo 'INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Jean");' | mysql -uroot -p holberton
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry 'bob@dylan.com' for key 'email'
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id      email   name
1       bob@dylan.com   Bob
2       sylvie@dylan.com        Sylvie
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# 
```
</Details>

### Task 1. In and not out
<Details>
Write a SQL script that creates a table users following these requirements:

With these attributes:
* id, integer, never null, auto increment and primary key
* email, string (255 characters), never null and unique
* name, string (255 characters)
* country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
If the table already exists, your script should not fail
Your script can be executed on any database

```
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
ERROR 1146 (42S02) at line 1: Table 'holberton.users' doesn't exist
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# cat 1-country_users.sql | mysql -uroot -p holberton
Enter password: 
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# echo 'INSERT INTO users (email, name, country) VALUES ("bob@dylan.com", "Bob", "US");' | mysql -uroot -p holberton
Enter password: 
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# echo 'INSERT INTO users (email, name, country) VALUES ("sylvie@dylan.com", "Sylvie", "CO");' | mysql -uroot -p holberton
Enter password: 
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# echo 'INSERT INTO users (email, name, country) VALUES ("jean@dylan.com", "Jean", "FR");' | mysql -uroot -p holberton
Enter password: 
ERROR 1265 (01000) at line 1: Data truncated for column 'country' at row 1
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# echo 'INSERT INTO users (email, name) VALUES ("john@dylan.com", "John");' | mysql -uroot -p holberton
Enter password: 
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# echo "SELECT * FROM users;" | mysql -uroot -p holberton
Enter password: 
id      email   name    country
1       bob@dylan.com   Bob     US
2       sylvie@dylan.com        Sylvie  CO
3       john@dylan.com  John    US
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# 
```
</Details>