Q1="SELECT actor.fname,actor.lname from actor inner join cast on (actor.id==pid and mid=12148);"
Q2="SELECT COUNT(actor.id) from actor inner join cast on actor.id=pid and actor.fname='Harrison (I)' and actor.lname='Ford'"
Q3="SELECT distinct pid from cast inner join movie on movie.id==mid and movie.name like 'Young Latin Girls %';"
Q4="SELECT COUNT(DISTINCT pid) FROM cast INNER JOIN Movie on Movie.id==mid AND Movie.year BETWEEN 1990 AND 2000; "
