SELECT Similarity FROM (
	SELECT a.docid AS DOC1, b.docid AS DOC2, sum(a.count * b.count) as Similarity
	FROM SimSubset a, SimSubset b
	WHERE a.term = b.term
	GROUP BY a.docid, b.docid)
WHERE DOC1 = '10080_txt_crude' AND DOC2 = '17035_txt_earn';