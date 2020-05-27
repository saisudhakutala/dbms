Q1="SELECT COUNT(id) FROM Movie WHERE year<2000;"

Q2="SELECT AVG(rank) FROM Movie WHERE year=1991;"

Q3="SELECT MIN(rank) FROM Movie WHERE year=1991;"

Q4="SELECT fname,lname FROM Actor INNER JOIN CAST ON Actor.id==pid WHERE mid=27;"

Q5="SELECT COUNT(mid) FROM Cast INNER JOIN Actor ON pid==Actor.id WHERE fname='Jon' AND lname='Dough';"

Q6="SELECT name FROM Movie where (year BETWEEN 2003 AND 2006) AND (name LIKE 'Young Latin Girls%');"

Q7="SELECT fname,lname FROM Director INNER JOIN MovieDirector INNER JOIN Movie ON mid==Movie.id AND did==Director.id WHERE Movie.name LIKE 'Star Trek%'; "

Q8="""select m.name from actor a
inner join cast c
inner join movie m
inner join director d
inner join moviedirector md
on a.id==c.pid and m.id==c.mid and m.id==md.mid and
d.id==md.did where d.fname='Jackie (I)' and d.lname='Chan' and a.fname='Jackie (I)' and a.lname='Chan'
order by m.name asc;
"""

Q9="""SELECT Director.fname, Director.lname
FROM Director 
INNER JOIN MovieDirector 
INNER JOIN Movie ON Movie.id==mid and Director.id=did 
where movie.year=2001
group by did having count(did)>=4
order by fname asc,lname desc; """

Q10="select gender,count(id) from actor group by gender;"


Q11="""select distinct m1.name,m2.name,m1.rank,m1.year 
from movie m1 cross join movie m2 
on m1.year == m2.year and 
m1.rank == m2.rank and 
m1.name!=m2.name
order by m1.name asc limit 100;
"""

Q12="""
select a.fname,m.year,m.rank from movie m
inner join cast c
inner join actor a on
a.id==c.pid and m.id==c.mid
group by a.id,year
order by a.fname asc,m.year desc
limit 100;
"""

'''

Rank of an actor for a given year is the average of ranks of 
all the movies he/she is casted in and released in that year. 
Your query should result fname, year and the rank of the actors. 
Your query should result in only 100 entries 
when ordered as following [10 points]

ascending order on actor fname and then
descending order on year
'''
       

Q13="""
select a.fname,d.fname,avg(m.rank) from actor a
inner join cast c on a.id==c.pid
inner join movie m on m.id==c.mid
inner join moviedirector md on md.mid==m.id
inner join director d on d.id==md.did
group by md.did,c.pid having count(m.id)>=5
order by avg(m.rank) desc,d.fname asc,a.fname desc limit 100;


"""


'''

select a.fname,d.fname,avg(m.rank) from movie m
inner join cast c
inner join actor a
inner join director d
inner join moviedirector md
on m.id==c.mid and 
c.pid==a.id and 
d.id==md.did and
m.id==md.mid
group by md.did,c.pid
having count(md.mid)>=5
order by avg(m.rank) desc,d.fname asc,a.fname desc limit 100;

Find the top Actor - Directors pair.
The score for an Actor - Director pair is the average of ranks of 
movies which the director has directed and which the actor has acted.
Consider only Actor - Director pair if they have worked together 
for at least 5 movies. [10 points]

Your query should return fname of the actor, 
fname of the director and the score.

Your query should return first 100 such pairs when ordered in

descending order of score and then
ascending order of director fname and then
descending order of actor fname
'''

