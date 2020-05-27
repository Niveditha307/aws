Q1 = "select count(id) from movie where year < 2000 ;"

Q2 = "select avg(rank) from movie where year == 1991 ;"

Q3 = "select min(rank) from movie where year == 1991 ;"

Q4 = "select moviewithcast.fname,moviewithcast.lname from(actor inner join cast on id == pid) as moviewithcast where moviewithcast.mid == 27;"

Q5 = "select count(moviewithcast.mid) from (actor inner join cast on id == pid) as moviewithcast where moviewithcast.fname == 'Jon' and moviewithcast.lname == 'Dough';"

Q6 = "select name from movie where name like 'Young Latin Girls%' and year between 2003 and 2006;"

Q7 = "select fname,lname from moviedirector inner join director on did == director.id inner join movie on mid == movie.id where name like 'Star Trek%';"

Q8 = "select name from cast inner join actor on pid = actor.id inner join moviedirector on 'cast'.mid = 'MovieDirector'.mid inner join movie on 'moviedirector'.mid = 'movie'.id inner join director on 'moviedirector'.did = 'director'.id  where actor.fname like 'Jackie (I)' and actor.lname like 'Chan' and director.fname like 'Jackie (I)' and director.lname like 'Chan';"

Q9 = "select fname,lname from moviedirector inner join director on did == director.id inner join movie on mid == movie.id where year == 2001 group by did having count(did)>=4 order by fname asc,lname desc;"

Q10 = "select gender,count(gender) from actor group by gender order by gender asc;"

Q12= "select fname,year,rank from cast inner join movie on mid = movie.id inner join actor on pid = actor.id order by fname asc,year desc limit 100;"


Q13 = "select actor.fname,director.fname,avg(rank) from actor inner join cast on pid = actor.id inner join movie on 'cast'.mid = 'Movie'.id inner join moviedirector on 'moviedirector'.mid = 'movie'.id inner join director on 'moviedirector'.did = 'director'.id group by  'moviedirector'.did,'actor'.id having count(movie.id) >=5 order by avg(rank) desc,director.fname asc,actor.fname desc limit 100;"

Q11 = "select distinct (a.name),b.name,a.rank,a.year from (movie as a inner join movie as b on a.rank == b.rank and a.year == b.year and a.name <> b.name) order by a.name asc limit 100;" 