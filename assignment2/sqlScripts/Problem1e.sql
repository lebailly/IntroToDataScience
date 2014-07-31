-- Write a SQL statement to find all documents that have more than 300 total 
-- terms, including duplicate terms. (Hint: You can use the HAVING clause, or 
-- you can use a nested query. Another hint: Remember that the count column 
-- contains the term frequencies, and you want to consider duplicates.) 
-- (docid, term_count)

SELECT count(*) FROM
(
	SELECT docid, COUNT(term) AS term_count, SUM(count) AS word_count
	FROM frequency
	GROUP BY docid
	HAVING word_count>300
);

-- term_count is not needed.