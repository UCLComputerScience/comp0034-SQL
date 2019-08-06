--Write queries to answer the following questions:

--1. What are the names of all teachers Bart has had?
SELECT DISTINCT t.name
FROM teachers t
         JOIN courses c ON c.teacher_id = t.id
         JOIN grades g ON g.course_id = c.id
         JOIN students s ON s.id = g.student_id
WHERE s.name = 'Bart';

--2. How many total students has Ms. Krabappel taught, and what are their names?
SELECT DISTINCT s.name
FROM students s
         JOIN grades g ON s.id = g.student_id
         JOIN courses c ON g.course_id = c.id
         JOIN teachers t ON t.id = c.teacher_id
WHERE t.name = 'Krabappel';

