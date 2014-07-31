SELECT count(*) FROM 
(
	SELECT DISTINCT term
	FROM frequency
	WHERE docid='10398_txt_earn' and count=1
);