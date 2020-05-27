Q1="""
select d.id,d.fname from director d
where exists(select md.mid from moviedirector md
inner join movie m 
on m.id==md.mid
where md.did==d.id and m.year>2000)
and not exists(
select md.mid from moviedirector md
inner join movie m
on m.id==md.mid
where d.id==md.did and m.year<2000) 
order by d.id asc;
"""

Q2='''select d.fname,(select m.name from movie m
inner join moviedirector md
on m.id=md.mid 
where md.did=d.id order by m.rank desc,m.name asc limit 1)
from director d limit 100;'''

Q3="""
select * from actor a where not exists(
select m.id from movie m inner join cast c
on m.id=c.mid and a.id==c.pid
where m.year between 1990 and 2000)
order by a.id desc limit 100;
"""
