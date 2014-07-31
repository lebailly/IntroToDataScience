SELECT MAX(Similarity) FROM (
	SELECT a.docid, sum(a.count * b.count) as Similarity
	FROM query a, query b
	WHERE a.term = b.term AND b.docid='q' AND a.docid !='q'
GROUP BY a.docid, b.docid );