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

### Task 2. Best band ever!
<Details>
Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

Requirements:

* Import this table dump: metal_bands.sql.zip
* Column names must be: origin and nb_fans
* Your script can be executed on any database
Context: Calculate/compute something is always power intensive… better to distribute the load!

```
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# cat 2-fans.sql | mysql -uroot -p holberton > tmp_res ; head tmp_res
Enter password: 
origin  nb_fans
USA     99349
Sweden  47169
Finland 32878
United Kingdom  32518
Germany 29486
Norway  22405
Canada  8874
The Netherlands 8819
Italy   7178
```
</Details>

### Task 3. Old school band
<Details>
Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

Requirements:

* Import this table dump: metal_bands.sql.zip
* Column names must be: band_name and lifespan (in years until 2022 - please use 2022 instead of YEAR(CURDATE()))
* You should use attributes formed and split for computing the lifespan
* Your script can be executed on any database

```
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# cat 3-glam_rock.sql | mysql -uroot -p holberton 
Enter password: 
band_name       lifespan
Alice Cooper    58
M�tley Cr�e     34
Marilyn Manson  33
The 69 Eyes     32
Hardcore Superstar      25
Nasty Idols     0
Hanoi Rocks     0
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# 
```
</Details>

### Task 4. Buy buy buy
<Details>
Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

Quantity in the table items can be negative.

Context: Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!

```
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# cat 4-init.sql | mysql -uroot -p holberton 
Enter password: 
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# cat 4-store.sql | mysql -uroot -p holberton 
Enter password: 
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# cat 4-main.sql | mysql -uroot -p holberton 
Enter password: 
name    quantity
apple   10
pineapple       10
pear    10
--
--
name    quantity
apple   6
pineapple       10
pear    8
item_name       number
apple   1
apple   3
pear    2
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# 

```
</Details>

### Task 5. Email validation to sent
<Details>
Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

Context: Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!

```
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# cat 5-init.sql | mysql -uroot -p holberton 
Enter password: 
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# cat 5-valid_email.sql | mysql -uroot -p holberton 
Enter password: 
ERROR 1064 (42000) at line 11: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'DELIMETER' at line 1
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# cat 5-valid_email.sql | mysql -uroot -p holberton 
Enter password: 
ERROR 1359 (HY000) at line 4: Trigger already exists
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# cat 5-main.sql | mysql -uroot -p holberton 
Enter password: 
id      email   name    valid_email
1       bob@dylan.com   Bob     0
2       sylvie@dylan.com        Sylvie  1
3       jeanne@dylan.com        Jeanne  1
--
--
id      email   name    valid_email
1       bob@dylan.com   Bob     1
2       sylvie+new@dylan.com    Sylvie  0
3       jeanne@dylan.com        Jannis  1
--
--
id      email   name    valid_email
1       bob@dylan.com   Bob     1
2       sylvie+new@dylan.com    Sylvie  0
3       jeanne@dylan.com        Jannis  1
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# 
```
</Details>

### Task 6. Add bonus
<Details>
Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

Requirements:

Procedure AddBonus is taking 3 inputs (in this order):
user_id, a users.id value (you can assume user_id is linked to an existing users)
project_name, a new or already exists projects - if no projects.name found in the table, you should create it
score, the score value for the correction
Context: Write code in SQL is a nice level up!

```
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# cat 6-bonus.sql | mysql -uroot -p holberton 
Enter password: 
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# cat 6-main.sql | mysql -uroot -p holberton 
Enter password: 
id      name
1       C is fun
2       Python is cool
user_id project_id      score
1       1       80
1       2       96
2       1       91
2       2       73
--
--
--
--
id      name
1       C is fun
2       Python is cool
3       Bonus project
4       New bonus
user_id project_id      score
1       1       80
1       2       96
2       1       91
2       2       73
2       2       100
2       3       100
1       3       10
2       4       90
root@2c462bd13a86:~/alx-backend-storage/0x00-MySQL_Advanced# 
```
</Details>