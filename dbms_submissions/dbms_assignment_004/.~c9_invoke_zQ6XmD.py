Q1="SELECT COUNT(id) FROM Movie WHERE year=2002 and rank>2 and name LIKE 'Ha%';"
Q2="SELECT MAX(rank) FROM Movie WHERE name LIKE 'Autom%' AND (year=1983 or year=1994);"
Q3="SELECT COUNT(id) FROM Actor WHERE gender=='M' AND (fname LIKE '%ei' or lname LIKE 'ei%');"
Q4="SELECT AVG(rank) AS average_rank_of_movies FROM Movie WHERE (year=1993 or year=1995 or year=2000) AND rank>=4.2;"
Q5="SELECT SUM(rank) FROM Movie WHERE (name LIKE '%Hary%') AND (year BETWEEN 1981 AND 1984) AND(rank<9);"
Q6="SELECT year FROM Movie WHERE rank=5 l;"
Q7="SELECT COUNT(id) FROM Actor WHERE gender='F' AND fname=(SELECT lname FROM Actor);"
Q8="SELECT DISTINCT fname FROM Actor WHERE lname LIKE '%ei' ORDER BY fname ASC LIMIT 100;"
Q9="SELECT name as movie_title FROM Movie WHERE year IN (2001,2002,2005,2006) LIMIT 25 OFFSET 10;"
Q10="SELECT DISTINCT lname "
'''
10=Get the first 5 distinct lnames of directors whose 
fname is not in ("Yeud", "Wolf", "Vicky). 
The result should be in the descending order of director's lname

9=Skip the first 10 rows and get 25 movies that are released
in the year (2001, 2002, 2005, 2006) 
and the output should have column movie_title instead of name.

7=Count the total number of female actors in the database and 
also include the actors which have same first and last names.'''
