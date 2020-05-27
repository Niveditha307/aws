Q1 = "SELECT pid,COUNT(mid) FROM cast GROUP BY pid;"

Q2 = "SELECT year,count(id) FROM movie GROUP BY year ORDER BY year asc;"

Q3 = "SELECT year,AVG(rank) as avg_rank FROM movie GROUP BY year  HAVING COUNT(id) >=10 ORDER BY year desc;"

Q4 = "SELECT year,MAX(rank) FROM movie GROUP BY year ORDER BY year asc;"

Q5 = "SELECT rank,count(name) FROM movie where name like 'a%' group by rank ;"