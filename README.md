READ ME FILE 
Log analysis project #3 
Udacity Full Stack Nanodegree 

###OVERVIEW 
The purpose of this project is to connect to the News database and to obtain results of 3 specific questions, listed below: 
•	What are the most popular articles of all time? 
•	Who are the most popular authors of all time?
•	 Which days did more than 1% of request lead to errors? 
INSTRUCTIONS 
In order to run this project you need to make sure you have downloaded the following software’s in your computer:
•	Python 3  
•	Vagrant  
•	Virtual box  

###LAUNCHING THE VIRTUAL MACHINE:  
1.	Download the database file  https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/n  ewsdata.zip  
2.	Unzip the file  
3.	Vagrant up  
4.	Vagrant ssh  
5.	Cd /vagrant  
6.	Psql –d news -f newsdata.sql  
7.	\dt (view of all the tables and data)  
Name of the file: logs.py in order to run the queries  

###CREATE VIEW COMANDS
QUERY 1  
SELECT articles.title, COUNT(*) as views FROM articles JOIN log on articles.slug = substring(log.path,10) WHERE path != '/'GROUP by substring(log.path, 10),articles.title ORDER BY views desc LIMIT 3; 

QUERY 2
SELECT authors.name, count(log.path) as views FROM authors left join articles on authors.id = articles.author left JOIN log on log.path like concat('%', articles.slug) GROUP BY authors.name ORDER BY views desc;  
QUERY 3 
Create view 
a1 as SELECT to_date(time,'FMMonth FMDD, YYYY'), COUNT(status) as total FROM log WHERE status = '404 NOT FOUND' GROUP BY to_date(time,'FMMonth FMDD, YYYY; 
Create view 
r2 as SELECT to_date(time,'FMMonth FMDD, YYYY'), COUNT(status) as total FROM log GROUP BY to_date (time,'FMMonth FMDD, YYYY; 
Create view 
rate_val as SELECT r2.to_date, cast(a1.total*100 as float)/ cast(r2.total as float) as val FROM a1,r2 WHERE a1.to_date = r2.to_date; 
Create view 
SELECT * FROM rate_val WHERE val > 1; 

###EXPECTED VIEW RESULTS 
#Query1 What are the most popular articles of all time? 
#Query2 Who are the most popular authors of all time? 
#Query3 Which days did more than 1% of request lead to errors? 
DBNAME= “news” 
      
###REFERENCES 
I used this websites as additional resources to complete this project: 
https://www.youtube.com/watch?v=8LnWXxYYB_4 
https://docs.python.org/2/library/functions.html#int https://www.vagrantup.com/docs/cli/ 
https://stackoverflow.com/questions/1108742/sql-round-function 
https://stackoverflow.com/questions/5420789/how-to-install-psycopg2-with-pip-on- python 
https://stackoverflow.com/questions/28677670/why-isnt-pycharms-autocomplete- working-for-libraries-i-install 
https://discussions.udacity.com 

