SELECT B.BOOK_ID, A.AUTHOR_NAME, DATE_FORMAT(B.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK AS B
INNER JOIN AUTHOR AS A ON A.AUTHOR_ID = B.AUTHOR_ID
WHERE B.CATEGORY LIKE ('%경제%')
ORDER BY B.PUBLISHED_DATE;