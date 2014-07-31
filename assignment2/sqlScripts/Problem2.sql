
SELECT value
FROM (
	SELECT a.row_num, b.col_num, sum(a.value*b.value) AS value 
	FROM a, b 
	WHERE a.col_num = b.row_num 
	GROUP BY a.row_num, b.col_num
) WHERE row_num = 2 AND col_num = 3;

-- That's it!  Join columns to rows, group by rows and columns, 
-- then filter to get the cell you want.

SELECT value
FROM (
	SELECT a.row_num, b.col_num, sum(a.value*b.value) AS value 
	FROM a JOIN b 
	ON a.col_num = b.row_num 
	GROUP BY a.row_num, b.col_num
) WHERE row_num = 2 AND col_num = 3;