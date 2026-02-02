
WITH tb_rn AS (
    SELECT *,

    row_number() OVER (PARTITION BY funcao ORDER BY vida_total DESC) AS vidarank
    FROM hero_info
)

SELECT *

FROM tb_rn

WHERE vidarank = 1




