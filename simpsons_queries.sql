SELECT *
FROM students
         JOIN grades ON id = student_id;

--table.column can be used to disambiguate column names:
SELECT *
FROM students
         JOIN grades ON students.id = grades.student_id

--Filtering columns in a join
SELECT name, course_id, grade
FROM students
         JOIN grades ON id = student_id;

--Filtered join (JOIN with WHERE)
SELECT name, course_id, grade
FROM students
         JOIN grades ON id = student_id
WHERE name = 'Bart';

--Poor query design
SELECT name, id, course_id, grade
FROM students
         JOIN grades ON id = 123
WHERE id = student_id;
--Improved query design - filter on WHERE not ON
SELECT name, id, course_id, grade
FROM students
         JOIN grades ON id = student_id
WHERE id = 123;

--Giving names to tables
SELECT s.name, g.*
FROM students s
         JOIN grades g ON s.id = g.student_id
WHERE g.grade <= 'C';

--Multi-table join
SELECT c.name
FROM courses c
         JOIN grades g ON g.course_id = c.id
         JOIN students bart ON g.student_id = bart.id
WHERE bart.name = 'Bart'
  AND g.grade <= 'B-';

--Courses taken by Bart and Lisa?
-- suboptimal solution: requires us to know Bart/Lisa's Student IDs, and only returns course IDs, not names
SELECT bart.course_id
FROM grades bart
         JOIN grades lisa ON lisa.course_id = bart.course_id
WHERE bart.student_id = 123
  AND lisa.student_id = 888;

--improved solution
SELECT DISTINCT c.name
FROM courses c
         JOIN grades g1 ON g1.course_id = c.id
         JOIN students bart ON g1.student_id = bart.id
         JOIN grades g2 ON g2.course_id = c.id
         JOIN students lisa ON g2.student_id = lisa.id
WHERE bart.name = 'Bart'
  AND lisa.name = 'Lisa';


--Write queries to answer the following questions:

--1. What are the names of all teachers Bart has had?

--2. How many total students has Ms. Krabappel taught, and what are their names?

