Q1='''
select a.id,a.fname,a.lname,a.gender from actor a
inner join cast c inner join movie m
on a.id=c.pid and m.id=c.mid
where m.name like "Annie%";
'''

Q2='''
select m.id,m.name,m.rank,m.year from movie m
inner join moviedirector md
inner join director d
on m.id=md.mid and d.id=md.did
where d.fname="Biff" and d.lname="Malibu"
and m.year in(1999,1994,2003)
order by m.rank desc,m.year asc;
'''

Q3='''
select m.year,count(m.id) as no_of_movies from movie m
group by m.year having avg(m.rank)>(select avg(mv.rank) from movie mv) 
order by m.year asc;
'''

Q4='''
select * from movie m
where m.year=2001 and m.rank<(select avg(mv.rank) from movie mv 
where mv.year=2001)
order by m.rank desc limit 10;
'''

Q6='''
select distinct c.pid from cast c
inner join movie m
where m.id=c.mid
group by c.mid,c.pid having count(distinct c.role)>1
order by c.pid
limit 100;
'''

Q7='''
select fname,count(fname) from director
group by fname having count(fname)>1;
'''

Q8='''
select d.id,d.fname,d.lname
from director d where exists(
select md.did from moviedirector md inner join cast c
on md.mid=c.mid and d.id=md.did group by c.mid having count(pid)>=100)
and not exists(
select md.did from moviedirector md inner join cast c
on md.mid=c.mid and d.id=md.did group by c.mid having count(pid)<100);
'''

Q5='''
select m.id,
(select count(a.id) from actor a inner join
cast c on a.id=c.pid and c.mid=m.id where a.gender='F')
as count_of_females,
(select count(a.id) from actor a inner join
cast c on a.id=c.pid and c.mid=m.id where a.gender='M')
as count_of_males
from movie m 
order by m.id limit 100;


select c.mid,female,male from(select count(a.id) from actor a 
inner join cast c on a.id=c.pid and where a.gender='F' group by c.mid);
as female
inner join ()
'''