-- Create database onlinemovie;
use onlinemovie;
-- create table if not exists userdata(
-- 								username varchar(50) primary key,
--                                 firstname varchar(50),
--                                 lastname varchar(50),
--                                 mobilenumber varchar(50),
--                                 confirmpassword varchar(50)
--                                 );
-- select * from userdata;
-- create table if not exists admindata( username varchar(50) primary key,
-- 										firstname varchar(50),
--                                         lastname varchar(50),
--                                         mobilenumber varchar(50),
--                                         confirmpassword varchar(50))

-- select * from admindata; 
-- drop table moviedetail;
-- create table if not exists moviedetail(registration_num int auto_increment primary key,
-- 										movie_name varchar(50) unique,
--                                         movie_genre varchar(50),
--                                         date_available varchar(50),
--                                         time_shift varchar(50));

-- insert into moviedetail(movie_name,movie_genre,date_available,time_shift) values ('The Big Lebowski','Comedy',current_date(),current_time());									
-- select * from moviedetail; 
-- drop table bookedmovie;                                      
-- create table if not exists bookedmovie(registrationN varchar(50) primary key,
-- 										movie_name varchar(50) ,
--                                         date_booked varchar(50),
--                                         time_booked varchar(50),
--                                         tickets varchar(50),
--                                         price varchar(50));
--                                        
                                        
-- insert into bookedmovie values('20200827201734415605','Lion King','Aug/28/2020','07:00-10:30','3','300')
select * from admindata;
-- alter table moviedetail
-- drop column date_available,
-- drop column time_shift
