-- USE oz_assignment;
-- SET SQL_SAFE_UPDATES = 0; -- 세이프모드 끄기

-- -- 민혁 사원의 데이터를 삭제하세요
-- DELETE FROM employees WHERE name = '민혁';
-- -- employees 테이블을 삭제하세요.
-- DROP TABLE employees;

UPDATE users
SET name = 'SENIOR'
WHERE age = 25;
SELECT ROW_COUNT();
