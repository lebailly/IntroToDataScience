-- Write a SQL statement to count the number of unique documents that contain 
-- both the word 'transactions' and the word 'world'.

SELECT count(*) FROM
(
	SELECT docid
	FROM frequency
	WHERE term='transactions'
		INTERSECT
	SELECT docid
	FROM frequency
	WHERE term='world'
);

-- A join on docid between the two filtered lists.

SELECT count(*) FROM
(
	(SELECT docid
	FROM frequency
	WHERE term='transactions') x
		JOIN
	(SELECT docid
	FROM frequency
	WHERE term='world') y
	ON x.docid=y.docid
);