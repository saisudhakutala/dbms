Q1='''
select avg(age) from player;
'''

Q2='''
select match_no,play_date
from match where audience>50000
order by match_no asc;
'''
Q3='''

select team_id,count(win_lose) as win_matches from matchteamdetails 
where win_lose='W'
group by team_id 
order by win_matches desc,team_id asc;

'''

'''
Q3=
select t.team_id,count(mtd.match_no) as count_win_match from team t
inner join match m inner join matchteamdetails mtd
on t.team_id=mtd.team_id and m.match_no=mtd.match_no
where mtd.win_lose='W' 
group by mtd.team_id
order by count_win_match desc,t.team_id asc;
'''

Q4='''
select match_no,play_date from match 
where stop1_sec > (select avg(stop1_sec) from match)
order by match_no desc;
'''
Q5='''
select mc.match_no,t.name,p.name from matchcaptain mc
inner join team t inner join player p
on mc.captain=p.player_id 
where t.team_id==mc.team_id 
order by mc.match_no,t.name;
'''
Q6='''
select m.match_no,p.name,p.jersey_no from match m
inner join player p on
p.player_id=m.player_of_match
order by m.match_no asc;
'''

Q7='''
select t.name,avg(p.age) from team t
inner join player p on
t.team_id==p.team_id
group by p.team_id having avg(p.age)>26
order by t.name asc;
'''

Q8='''
select p.name,p.jersey_no,p.age,count(gd.player_id) as no_goals from player p
inner join goaldetails gd on
p.player_id==gd.player_id
where p.age<=27
group by gd.player_id
order by no_goals desc,p.name asc;
'''

Q9='''
select gd.team_id,
(count(gd.goal_id)*100.0/(select count(goal_id) from goaldetails))
as percentage
from goaldetails gd group by gd.team_id;
'''

Q10='''
select avg(goals) from(select count(goal_id) 
as goals from goaldetails group by team_id);
'''

Q11='''
select p.player_id,p.name,p.date_of_birth from player p
where not exists( select gd.player_id from goaldetails gd
where p.player_id==gd.player_id);
'''

Q12='''
select t.name,m.match_no,m.audience,
m.audience - (select avg(m.audience) 
from match m inner join matchteamdetails
mtd on m.match_no==mtd.match_no
where t.team_id==mtd.team_id
group by mtd.team_id) as difference from team t
inner join match m 
inner join matchteamdetails md on
m.match_no==md.match_no 
where t.team_id==md.team_id 
order by m.match_no asc;
'''


'''
select t.name,m.match_no,m.audience,
m.audience - (select avg(m.audience) 
from match m inner join matchteamdetails
mtd on m.match_no==mtd.match_no and 
t.team_id==mtd.team_id
group by mtd.team_id) as difference from team t
inner join match m 
inner join matchteamdetails md on
m.match_no==md.match_no 
and t.team_id==md.team_id 
order by m.match_no asc;

Get the audience count and the difference between 
the audience count and the teams average audience count 
for all matches in the database. - [7 Points]
Your query should return team_name, match_no, 
audience and the difference beteween the audience and 
the average audience across all matches played 
by that team in the ascending order of match_no




'''
