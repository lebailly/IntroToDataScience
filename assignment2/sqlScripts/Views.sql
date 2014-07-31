-- Queries to create views

CREATE VIEW SimSubset AS 
SELECT * FROM Frequency 
WHERE docid = '10080_txt_crude' or docid = '17035_txt_earn';

CREATE VIEW query AS
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;