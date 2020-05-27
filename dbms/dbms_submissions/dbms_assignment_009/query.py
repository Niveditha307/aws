Q1 = "select avg(age) from player;"

Q2 = "select match_no,play_date from match where audience > 50000 order by match_no asc;"

Q3 = '''select team_id,count(team_id) from matchteamdetails where win_lose = 'W' group by team_id order by count(team_id) desc,team_id asc;'''

Q4 ='''select match_no,play_date from match where stop1_sec > (select avg(stop1_sec) from match) order by match_no desc;'''

Q5 = '''select matchcaptain.match_no,team.name,player.name from matchcaptain inner join team 
    on matchcaptain.team_id = team.team_id inner join player on matchcaptain.captain = player.player_id 
    order by matchcaptain.match_no asc,team.name asc;  '''
    
Q6 =''' select match.match_no,player.name,player.jersey_no from match inner join player on player.player_id = match.player_of_match order by match_no asc;'''

Q7 = '''select name ,(select avg(age) from player where player.team_id = team.team_id) 
    as avg_age from team where avg_age > 26 order by name asc;'''
    
Q8 = '''select player.name,player.jersey_no,player.age, count(goaldetails.goal_id) as no_of_goals from goaldetails
        inner join player on  goaldetails.player_id= player.player_id 
        where player.age <= 27  group by goaldetails.player_id order by no_of_goals desc, player.name asc ;'''
        
        
Q11 = '''select player.player_id,player.name,player.date_of_birth from player where not exists (select goaldetails.match_no from
            goaldetails inner join match on  goaldetails.match_no = match.match_no where goaldetails.player_id = player.player_id
            group by goaldetails.player_id,goaldetails.match_no having count(goaldetails.goal_id) != 0 ) order by player.player_id ;'''

    
Q10 =''' select avg(goals) from (select count(goaldetails.goal_id) as goals from goaldetails inner join team on team.team_id = goaldetails.team_id group by goaldetails.team_id);'''  
    
    
Q9 = '''select team_id,count(goaldetails.goal_id) * 100.0 / (select count(goaldetails.goal_id) from goaldetails) from goaldetails group by goaldetails.team_id'''


Q12 = '''select t.name,m.match_no,m.audience , m.audience - (select avg( m.audience)  from match  m inner join matchteamdetails md on md.match_no = m.match_no
         where t.team_id =  md.team_id group by md.team_id) 
    as difference from team t inner join matchteamdetails md  on t.team_id = md.team_id
         inner join match m on m.match_no = md.match_no order by m.match_no asc;'''
         
         
         
         