Q1 = "select moviewithcast.fname,moviewithcast.lname from(actor inner join cast on id == pid) as moviewithcast where moviewithcast.mid == 12148;"
Q2 = "select count(moviewithcast.mid) from (actor inner join cast on id == pid) as moviewithcast where moviewithcast.fname == 'Harrison (I)' and moviewithcast.lname == 'Ford';"
Q3 = "select distinct(moviewithcast.pid) from (movie inner join cast on id == mid) as moviewithcast where moviewithcast.name like 'Young Latin Girls%';"
Q4 = "select count(distinct(m.pid)) from (movie inner join cast on id == mid) as m where m.year between 1990 and 2000 ;"

