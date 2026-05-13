-- Write your query below
SELECT
    student_id,
    MIN(exam_id) AS exam_id,
    score
FROM exam_results er
WHERE score = (
    SELECT MAX(score) from exam_results WHERE student_id = er.student_id
)
GROUP BY student_id, score
ORDER BY student_id