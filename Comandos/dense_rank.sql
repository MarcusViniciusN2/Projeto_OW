WITH tb_dense_rank AS (
    SELECT *,
        DENSE_RANK() OVER (PARTITION BY funcao ORDER BY vida_total DESC) AS vidarank
    FROM hero_info
)
SELECT *
FROM tb_dense_rank
WHERE vidarank = 1;
