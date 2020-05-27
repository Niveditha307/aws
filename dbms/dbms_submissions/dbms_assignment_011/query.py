#Q1 = '''select actor.id,actor.fname,actor.lname,actor.gender from actor inner join cast on actor.id = pid 
 #       inner join movie on movie.id = mid where movie.name like 'Annie%';'''
        
#Q2  = ''' select movie.id,movie.name,movie.rank,movie.year from movie inner join moviedirector on
 #           movie.id = mid inner join director on did = director.id where director.fname like 'Biff' and
  #       director.lname like  'Malibu' and movie.year in (1999,1994,2003) Order by movie.rank desc,movie.year asc ;'''
         
#Q3 = ''' select year,count(id) as no_of_movies from movie  group by year having (avg(rank))  > (select avg(rank) from movie) order by year asc;'''


#Q4 = '''select id,name,year,rank from movie where year = 2001 and rank < (select avg(rank) from movie where year = 2001) order by rank desc limit 10;'''



#Q6 = '''select distinct pid from cast inner join actor on 'actor'.id = 'cast'.pid inner join movie on 'movie'.id = 'cast'.mid group by mid,pid having count(distinct role) > 1 order by pid asc limit 100;''' 

#Q7 = '''select fname,count(fname) from director group by fname having count(fname) > 1;'''  


Q5 = '''select movie.id,count(case when 'actor'.gender = 'F' then 1 end) as no_of_female_actors ,count(case when 'actor'.gender = 'M' then 1 end) as no_of_male_actors
from actor inner join cast on 'cast'.pid = 'actor'.id inner join movie on 'movie'.id = 'cast'.mid group by 'movie'.id Order by 'movie'.id asc limit 100;'''

Q5 = '''select count(no_of_female_actors) from (select count(actor.id) from actor inner join cast on 'actor'.id = 'cast'.pid inner join movie on 'movie'.id = 'cast'.mid
        where 'actor'.gender = 'F') as no_of_female_actors ;'''








#Q8 = '''select d.id ,d.fname,d.lname from director d where exists
#(select count(c.pid) from moviedirector mvd inner join cast c on c.mid = mvd.mid where d.id = mvd.did group by mvd.mid having count(distinct c.pid) >= 100) 
#and Not exists(select count(c.pid) from moviedirector mvd inner join cast c on c.mid = mvd.mid where d.id = mvd.did group by mvd.mid having count(distinct c.pid) < 100); '''