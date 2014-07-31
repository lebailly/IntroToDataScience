# Write a SQL statement to count the number of documents containing the word "parliament"

SELECT count(*)
FROM frequency
WHERE term = 'parliament';