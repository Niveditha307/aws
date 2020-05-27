Q1 = '''select director.id,director.fname from director 
    where not exists (select mid from moviedirector inner join movie on mid = movie.id where
    director.id = did and movie.year < 2000) and exists (select mid from moviedirector inner join movie
    on mid = movie.id  where did = director.id and movie.year > 2000) order by director.id asc ;'''
    
    
Q2 =    '''select di.fname,(select movie.name from movie inner join moviedirector on movie.id = mid 
            inner join director on director.id = did where director.id =di.id 
            order by rank desc ,movie.name asc limit 1)  from director as di limit 100 ;'''
   
Q3 = '''select * from actor where not exists (select mid from cast inner join movie on 
        mid = movie.id where actor.id = pid and  movie.year between 1990 and 2000) order by actor.id desc limit 100;'''
        
        