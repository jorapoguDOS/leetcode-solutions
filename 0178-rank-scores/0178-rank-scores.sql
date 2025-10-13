SELECT score, 
       DENSE_RANK() OVER (ORDER BY score DESC)  AS "rank"
FROM Scores
ORDER BY score DESC;


-- SELECT main.score,
--         (SELECT COUNT(DISTINCT r.score)
--          FROM Scores AS r
--          WHERE r.score >= main.score
--         ) AS "rank"
-- FROM Scores AS main
-- ORDER BY main.score DESC;