WITH tb_rankvida AS (
    SELECT *,
           RANK() OVER (PARTITION BY funcao ORDER BY vida_total DESC) AS vidarank
    FROM hero_info
)

SELECT *
FROM tb_rankvida

WHERE vidarank = 1;

