Q1="SELECT COUNT(id) FROM Movie WHERE year=2002 and rank>2 and name LIKE 'Ha%';"
Q2="SELECT MAX(rank) FROM Movie WHERE name LIKE 'Autom%' AND (year=1983 or year=1994);"
Q3="SELECT COUNT(id) FROM Actor WHERE gender=='M' AND (fname LIKE '%ei' or lname LIKE 'ei%');"
Q4="SELECT AVG(rank) AS average_rank_of_movies FROM Movie WHERE (year=1993 or year=1995 or year=2000) AND rank>=4.2;"
Q5="SELECT SUM(rank) FROM Movie WHERE (name LIKE '%Hary%') AND (year BETWEEN 1981 AND 1984) AND(rank<9);"
Q6="SELECT year FROM Movie WHERE rank=5 ORDER BY year ASC LIMIT 1;"
Q7="SELECT COUNT(id) FROM Actor WHERE gender='F' or fname==lname"
Q8="SELECT DISTINCT fname FROM Actor WHERE lname LIKE '%ei' ORDER BY fname ASC LIMIT 100;"
Q9="SELECT id,name as movie_title,year FROM Movie WHERE year IN (2001,2002,2005,2006) LIMIT 25 OFFSET 10;"
Q10="""SELECT DISTINCT lname FROM Director
WHERE fname in('Yeud','Wolf','Vicky')
ORDER BY lname ASC LIMIT 5;
"""