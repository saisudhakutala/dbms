Q1='''
select p.player_id,p.team_id,p.jersey_no,
p.name,p.date_of_birth,p.age
from player p inner join matchcaptain mc on p.player_id=mc.captain 
and p.team_id=mc.team_id
left join goaldetails gd on gd.player_id=p.player_id 
where gd.goal_id is null;
'''
Q2='''
select t.team_id,count(mtd.team_id) from team t 
inner join matchteamdetails mtd 
on mtd.team_id==t.team_id group by mtd.team_id;
'''

Q3='''
select p.team_id,count(gd.goal_id)*1.0/(
select count(player_id) from player pl
where pl.team_id==p.team_id
group by pl.team_id) as avg_goal_score
from player p
inner join goaldetails gd on
gd.player_id==p.player_id and
gd.team_id==p.team_id group by p.team_id;
'''

Q4='''
select mc.captain,count(mc.captain) as no_of_times_captain
from matchcaptain mc
group by mc.captain;
'''

Q5='''
select count(distinct m.player_of_match) as no_players
from matchcaptain mc
inner join match m on mc.captain==m.player_of_match
where m.match_no==mc.match_no;
'''

Q6='''
select distinct p.player_id from player p
where exists(select mc.captain from matchcaptain mc
where p.player_id==mc.captain)
and not exists(select m.player_of_match from match m 
where m.player_of_match==p.player_id);
'''
Q7='''
select strftime('%m',play_date) as month,
count(match_no) as no_of_matches from
match group by month order by no_of_matches desc;
'''

Q8='''
select p.jersey_no,count(mc.captain) as no_captains
from player p inner join matchcaptain mc on 
mc.captain==p.player_id 
group by p.jersey_no
order by no_captains desc,p.jersey_no desc;
'''
Q9='''
select p.player_id,avg(m.audience) as avg_audience from player p
inner join matchteamdetails mtd inner join match m
on p.team_id=mtd.team_id
where m.match_no==mtd.match_no
group by p.player_id
order by avg_audience desc ,p.player_id desc;
'''

'''
Find the average of the audience for each player. 
In the descending order of avg_audience and player_id.
'''

Q10='''
select p.team_id,avg(p.age) from player p
group by p.team_id; 
'''

Q11='''
select avg(p.age) from player p inner join matchcaptain mc
on p.player_id==mc.captain;
'''
Q12='''
select strftime('%m',p.date_of_birth) as month,
count(p.player_id) as no_of_players
from player p group by month
order by no_of_players desc, month desc;

'''
Q13='''
select mc.captain,count(mtd.match_no) as no_of_wins
from matchteamdetails mtd inner join matchcaptain mc
on mc.team_id==mtd.team_id and mc.match_no==mtd.match_no
where win_lose='W'
group by mc.captain
order by no_of_wins desc,mc.captain asc;

'''
'''
Find the captain id and the number of matches 
he/she has won(no_of_wins). Your Query should 
return captain and no_of_wins in the descending order of no_of_wins.

'''