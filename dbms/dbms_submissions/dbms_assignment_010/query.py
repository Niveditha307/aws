Q1 = '''select mc.captain,mc.team_id,p.jersey_no,p.name,p.date_of_birth,p.age from player p inner join matchcaptain mc on 
    p.player_id = mc.captain where exists(select captain from matchcaptain where p.player_id = mc.captain) AND not exists
    (select goaldetails.goal_id from  goaldetails where  goaldetails.player_id = p.player_id );'''
            

Q2 = '''select team_id ,count(match_no) as no_of_games from matchteamdetails  group by team_id ;'''


Q3 = '''select team_id,(select count(goal_id)/ 23.0 ) as average from goaldetails group by team_id;'''

Q4 = '''select captain,count(match_no) from matchcaptain group by captain;'''

Q5 ='''select count( distinct matchcaptain.captain) as no_players  from match inner join player on 
    match.player_of_match = player.player_id inner join matchcaptain on matchcaptain.captain = player.player_id
    where  match.match_no = matchcaptain.match_no;'''



Q7 ='''SELECT distinct strftime('%m', play_date) as m,count(match_no) FROM match group by m ;'''

Q6 = '''select distinct captain from matchcaptain inner join 
    player where player.player_id = matchcaptain.captain and player.player_id not in (select player_of_match from match);'''
    
Q8 = '''select jersey_no,count(captain) as no_captains from player inner join matchcaptain on matchcaptain.captain = player.player_id 
    group by jersey_no order by no_captains desc,jersey_no desc;'''

Q10 = ''' select team_id,avg(age) from player group by team_id;'''


Q11 = '''select avg(age) from matchcaptain inner join player on player.player_id = matchcaptain.captain;'''



Q12 = '''SELECT distinct strftime('%m', date_of_birth) as m,count(player_id) as no_of_players FROM player group by m order by no_of_players desc,m desc;'''

Q13 = ''' select matchcaptain.captain, count(matchteamdetails.win_lose) as no_of_wins from matchcaptain inner join matchteamdetails on matchcaptain.match_no = matchteamdetails.match_no
    matchcaptain.team_id = matchteamdetails.team_id where matchteamdetails.win_lose == 'W'   group by matchcaptain.captain  order by no_of_wins desc;''' 
    
    
Q9 = '''select player.player_id ,avg(match.audience) as average_audience from player inner join matchteamdetails on player.team_id= matchteamdetails.team_id
        inner join match on match.match_no = matchteamdetails.match_no group by player.player_id
        order by average_audience desc,player.player_id desc;'''
        
    
    
    
    


    
    
    
    
    
    