q= "select s.student_id,s.no_of_course ,c.course_id,c.no_of_students from (select student_id ,count(course_id) as no_of_course from enrollment group by student_id) as s join(select course_id,count(student_id) as no_of_students from enrollment group by course_id) as c where c.no_of_course > 3 "


select director.id,director.fname from director where not exists (select did from moviedirector inner join movie on  mid = movie.id and inner join director on did = director.id where movie.year < 2000) and exists (select did from moviedirector inner join movie on mid = movie.id and inner join director on did = director.id where movie.year > 2000);                              



select director.id,director.fname from director where not exists (select movie.id from movie inner join moviedirector on movie.id = mid where movie.year < 2000 and (select director.id from director where director.id = did group by director.id and count(director.id) == 0)) and exists (select movie.id from movie inner join moviedirector on mid = movie.id  where movie.year > 2000 and (select director.id from director where director.id = did group by director.id  having count(director.id)>=1));             

select director.id,director.fname ,count(director.fname) from director where not exists (select movie.id from movie inner join moviedirector on movie.id = mid where movie.year > 2000 and (select director.id from director where director.id = did group by director.id having count(director.id) == 0)) and exists (select movie.id from movie inner join moviedirector on mid = movie.id  where movie.year > 2000 and (select director.id from director where director.id = did group by director.id  having count(director.id)>=1)); 



select director.id,director.fname from director where not exists (select moviedirector inner join movie on mid = movie.id where movie.year < 2000 and group by director.id having count(director.id)==0





select director.id,director.fname from director where not exists (select mid from moviedirector inner join movie on mid = movie.id where (select director.id from director inner join moviedirector on did = director.id where movie.year <> 2000 )) and exists (select mid from moviedirector inner join movie on mid = movie.id where (select director.id from director inner join moviedirector on did = director.id where movie.year == 2000));




select director.id,director.fname from director where not exists (select mid from moviedirector inner join movie on mid = movie.id where director.id = did) and exists (select mid from moviedirector inner join movie on mid = movie.id  where movie.year == 2000);






select director.id,director.fname from director where not exists (select mid from moviedirector inner join movie on mid = movie.id where director.id = did and movie.year < 2000) and exists (select mid from moviedirector inner join movie on mid = movie.id  where did = director.id and movie.year > 2000);                                                                          
87328|gr|2689



sqlite> select director.id,director.fname,count(director.fname) from director where not exists (select mid from moviedirector inner join movie on mid = movie.id where director.id = did and  movie.year != 2000) and exists (select mid from moviedirector inner join movie on mid = movie.id  where director.id = did and movie.year == 2000);                                                   
1466|lvaro|462