Q1="""
select d.id,d.fname from director d
where exists (
select md.did from moviedirector md.id==md.mid where
m.year>2000) and not exists(
select md.did from moviedirector md inner join
movie m on m.id==md.mid where
m.year<2000
);

select d.id,d.fname from director d
where exists(select md.did from moviedirector
inner join movie where d.id==md.did and m.year>2000);
"""