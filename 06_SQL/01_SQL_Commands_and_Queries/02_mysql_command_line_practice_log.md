# MySQL Command Line Practice Log

Hands-on practice of core SQL commands using the MySQL Command Line Client. Everything below was run against a database named `nit` with two tables, `student` and `emp`.

## Topics Covered

1. [Databases and Tables](#1-databases-and-tables)
2. [Inserting Data](#2-inserting-data)
3. [Selecting Data](#3-selecting-data)
4. [Updating Data](#4-updating-data)
5. [Altering a Table](#5-altering-a-table)
6. [Aggregate Functions](#6-aggregate-functions)
7. [Sorting with ORDER BY](#7-sorting-with-order-by)
8. [Pattern Matching with LIKE](#8-pattern-matching-with-like)
9. [Creating a Second Table](#9-creating-a-second-table)
10. [Joins](#10-joins)
11. [Errors I Hit and How I Fixed Them](#11-errors-i-hit-and-how-i-fixed-them)

---

## 1. Databases and Tables

List the existing databases, create a new one, and switch to it:

```sql
SHOW DATABASES;
CREATE DATABASE nit;
USE nit;
```

Create the `student` table with a primary key:

```sql
CREATE TABLE student(
    name VARCHAR(30),
    id INT NOT NULL PRIMARY KEY,
    address VARCHAR(50),
    marks INT
);
```

Inspect the table structure:

```sql
DESC student;
```

```text
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| name    | varchar(30) | YES  |     | NULL    |       |
| id      | int         | NO   | PRI | NULL    |       |
| address | varchar(50) | YES  |     | NULL    |       |
| marks   | int         | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+
```

## 2. Inserting Data

**With explicit column names** (the order can differ from the table definition):

```sql
INSERT INTO student(marks, id, name, address)
VALUES(78, 12, 'shoaib', 'hyd');
```

**Without column names** (values must follow the table's column order):

```sql
INSERT INTO student
VALUES('moiz', 40, 'bng', 88);
```

**Multiple rows in one statement:**

```sql
INSERT INTO student
VALUES
('alex', 45, 'hyd', 79),
('cathy', 17, 'delhi', 90),
('dolly', 48, 'pune', 67),
('cherry', 78, 'mumbai', 34);
```

## 3. Selecting Data

```sql
SELECT * FROM student;
SELECT name FROM student;
SELECT name, id FROM student;
SELECT * FROM student WHERE id = 12;
```

Result of `SELECT * FROM student;`:

```text
+--------+----+---------+-------+
| name   | id | address | marks |
+--------+----+---------+-------+
| shoaib | 12 | hyd     |    78 |
| cathy  | 17 | delhi   |    90 |
| moiz   | 40 | bng     |    88 |
| alex   | 45 | hyd     |    79 |
| dolly  | 48 | pune    |    67 |
| cherry | 78 | mumbai  |    34 |
+--------+----+---------+-------+
```

## 4. Updating Data

Update a single row using `WHERE`:

```sql
UPDATE student
SET address = 'chennai'
WHERE id = 45;
```

> **Note:** an `UPDATE` without a `WHERE` clause changes **every** row in the table. See section 5, where `SET phoneNo = 123` updated all 6 rows.

## 5. Altering a Table

**Add a column:**

```sql
ALTER TABLE student ADD phoneNo INT;
```

Fill it for all rows, then for one specific row:

```sql
UPDATE student SET phoneNo = 123;                  -- all 6 rows
UPDATE student SET phoneNo = 456 WHERE id = 12;    -- only id 12
```

```text
+--------+----+---------+-------+---------+
| name   | id | address | marks | phoneNo |
+--------+----+---------+-------+---------+
| shoaib | 12 | hyd     |    78 |     456 |
| cathy  | 17 | delhi   |    90 |     123 |
| moiz   | 40 | bng     |    88 |     123 |
| alex   | 45 | chennai |    79 |     123 |
| dolly  | 48 | pune    |    67 |     123 |
| cherry | 78 | mumbai  |    34 |     123 |
+--------+----+---------+-------+---------+
```

**Modify a column's data type or size:**

```sql
ALTER TABLE student MODIFY COLUMN name VARCHAR(60);
```

**Drop a column:**

```sql
ALTER TABLE student DROP COLUMN phoneNo;
```

## 6. Aggregate Functions

```sql
SELECT SUM(marks) FROM student;     -- 436
SELECT AVG(marks) FROM student;     -- 72.6667
SELECT COUNT(name) FROM student;    -- 6
SELECT MAX(marks) FROM student;     -- 90
SELECT MIN(marks) FROM student;     -- 34
```

## 7. Sorting with ORDER BY

Ascending (default) and descending:

```sql
SELECT * FROM student ORDER BY marks;
SELECT * FROM student ORDER BY marks DESC;
```

```text
-- ORDER BY marks DESC
+--------+----+---------+-------+
| name   | id | address | marks |
+--------+----+---------+-------+
| cathy  | 17 | delhi   |    90 |
| moiz   | 40 | bng     |    88 |
| alex   | 45 | chennai |    79 |
| shoaib | 12 | hyd     |    78 |
| dolly  | 48 | pune    |    67 |
| cherry | 78 | mumbai  |    34 |
+--------+----+---------+-------+
```

## 8. Pattern Matching with LIKE

| Wildcard | Meaning |
|----------|---------|
| `%` | Any number of characters (including none) |
| `_` | Exactly one character |

```sql
SELECT * FROM student WHERE name LIKE 'a%';     -- starts with 'a'        -> alex
SELECT * FROM student WHERE name LIKE '%y';     -- ends with 'y'          -> cathy, dolly, cherry
SELECT * FROM student WHERE name LIKE '_a%';    -- 'a' is the 2nd letter  -> cathy
SELECT * FROM student WHERE name LIKE '%i_';    -- 'i' is 2nd from last   -> shoaib, moiz
SELECT * FROM student WHERE name LIKE '%s_';    -- 's' is 2nd from last   -> empty set
```

## 9. Creating a Second Table

Created an `emp` table and inserted four rows to practise joins:

```sql
CREATE TABLE emp(
    id INT NOT NULL PRIMARY KEY,
    salary INT,
    empcode INT,
    name VARCHAR(30)
);

INSERT INTO emp VALUES
(12, 20000, 102, 'aman'),
(78, 30000, 105, 'max'),
(80, 25000, 103, 'ram'),
(34, 90000, 106, 'sam');
```

```text
+----+--------+---------+------+
| id | salary | empcode | name |
+----+--------+---------+------+
| 12 |  20000 |     102 | aman |
| 34 |  90000 |     106 | sam  |
| 78 |  30000 |     105 | max  |
| 80 |  25000 |     103 | ram  |
+----+--------+---------+------+
```

## 10. Joins

The two tables are joined on `id`. Only ids **12** and **78** exist in both tables. The names differ between tables, so the join is only to demonstrate how each join type behaves.

### INNER JOIN

Returns only the rows that match in both tables.

```sql
SELECT * FROM student INNER JOIN emp ON student.id = emp.id;
```

```text
+--------+----+---------+-------+----+--------+---------+------+
| name   | id | address | marks | id | salary | empcode | name |
+--------+----+---------+-------+----+--------+---------+------+
| shoaib | 12 | hyd     |    78 | 12 |  20000 |     102 | aman |
| cherry | 78 | mumbai  |    34 | 78 |  30000 |     105 | max  |
+--------+----+---------+-------+----+--------+---------+------+
```

### LEFT JOIN

Returns every row from the left table, plus matching rows from the right table (`NULL` where there is no match).

```sql
SELECT * FROM student LEFT JOIN emp ON student.id = emp.id;
```

```text
+--------+----+---------+-------+------+--------+---------+------+
| name   | id | address | marks | id   | salary | empcode | name |
+--------+----+---------+-------+------+--------+---------+------+
| shoaib | 12 | hyd     |    78 |   12 |  20000 |     102 | aman |
| cathy  | 17 | delhi   |    90 | NULL |   NULL |    NULL | NULL |
| moiz   | 40 | bng     |    88 | NULL |   NULL |    NULL | NULL |
| alex   | 45 | chennai |    79 | NULL |   NULL |    NULL | NULL |
| dolly  | 48 | pune    |    67 | NULL |   NULL |    NULL | NULL |
| cherry | 78 | mumbai  |    34 |   78 |  30000 |     105 | max  |
+--------+----+---------+-------+------+--------+---------+------+
```

Swapping the table order (`emp LEFT JOIN student`) keeps all 4 `emp` rows instead.

### RIGHT JOIN

Returns every row from the right table, plus matching rows from the left table.

```sql
SELECT * FROM student RIGHT JOIN emp ON student.id = emp.id;
```

```text
+--------+------+---------+-------+----+--------+---------+------+
| name   | id   | address | marks | id | salary | empcode | name |
+--------+------+---------+-------+----+--------+---------+------+
| shoaib |   12 | hyd     |    78 | 12 |  20000 |     102 | aman |
| NULL   | NULL | NULL    |  NULL | 34 |  90000 |     106 | sam  |
| cherry |   78 | mumbai  |    34 | 78 |  30000 |     105 | max  |
| NULL   | NULL | NULL    |  NULL | 80 |  25000 |     103 | ram  |
+--------+------+---------+-------+----+--------+---------+------+
```

### CROSS JOIN

Pairs every row of one table with every row of the other: 6 student rows x 4 emp rows = **24 rows**.

```sql
SELECT * FROM student CROSS JOIN emp;
```

```text
-- first 8 of 24 rows shown
+--------+----+---------+-------+----+--------+---------+------+
| name   | id | address | marks | id | salary | empcode | name |
+--------+----+---------+-------+----+--------+---------+------+
| shoaib | 12 | hyd     |    78 | 80 |  25000 |     103 | ram  |
| shoaib | 12 | hyd     |    78 | 78 |  30000 |     105 | max  |
| shoaib | 12 | hyd     |    78 | 34 |  90000 |     106 | sam  |
| shoaib | 12 | hyd     |    78 | 12 |  20000 |     102 | aman |
| cathy  | 17 | delhi   |    90 | 80 |  25000 |     103 | ram  |
| cathy  | 17 | delhi   |    90 | 78 |  30000 |     105 | max  |
| cathy  | 17 | delhi   |    90 | 34 |  90000 |     106 | sam  |
| cathy  | 17 | delhi   |    90 | 12 |  20000 |     102 | aman |
+--------+----+---------+-------+----+--------+---------+------+
```

## 11. Errors I Hit and How I Fixed Them

Mistakes are part of practice, so here is what went wrong and what fixed it.

| Error | What I ran | Cause | Fix |
|-------|-----------|-------|-----|
| `1062` Duplicate entry | `INSERT INTO student VALUES('sam', 12, 'hyd', 56);` | `id` is the primary key and 12 already exists | Use a unique `id` |
| `1146` Table doesn't exist | `select * from students;` | Typo: the table is `student`, not `students` | Use the correct table name |
| `1064` Syntax error | `update student phoneNo = 456 where id = 12;` | Missing `SET` | `UPDATE student SET phoneNo = 456 WHERE id = 12;` |
| `1064` Syntax error | `alter student drop column phoneNo;` | Missing `TABLE` keyword | `ALTER TABLE student DROP COLUMN phoneNo;` |
| `1630` Function does not exist | `select sum (marks) from student;` | Space between the function name and `(` | `SUM(marks)` with no space |
| `1305` Function does not exist | `select ave(marks) from student;` | Wrong function name | The function is `AVG` |
| `1064` Syntax error | `... where name leke '%s_';` | Typo in `LIKE` | `LIKE '%s_'` |
| `1064` Syntax error | Several attempts at `CREATE TABLE emp(...)` | Missing comma between columns, missing data type on `id`, and an unclosed parenthesis | Every column needs a name and a type, separated by commas, and the whole list must be closed with `)` |
| `1066` Not unique table/alias | `select * from emp inner join emp on student.id = emp.id;` | Joined `emp` with itself instead of with `student` | `emp INNER JOIN student ON student.id = emp.id` |

---

*Practised on MySQL 8.0 using the MySQL Command Line Client.*
