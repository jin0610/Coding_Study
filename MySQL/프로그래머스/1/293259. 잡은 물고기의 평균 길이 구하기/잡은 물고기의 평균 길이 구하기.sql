-- 코드를 작성해주세요
SELECT ROUND(AVG(CASE
                    WHEN LENGTH <= 10
                    THEN 10
                    WHEN LENGTH IS NULL
                    THEN 10
                    ELSE LENGTH
                END),2) AS AVERAGE_LENGTH
FROM FISH_INFO
