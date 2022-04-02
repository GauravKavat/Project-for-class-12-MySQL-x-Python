The user must have MySQL installed on the system for this program to successfully run without any errors and troubles. The preferred version is version 8 of MySQL available on the website (https://dev.mysq.com) It is free to download.
After the MySQL is installed on the system the user must make sure that the database named main is created in the system.

Finally, the user needs to setup a table named manager for all the information to be saved in it.

If the user finds any difficulty in doing so the user can just use these commands:


TO CREATE DATABASE:

create database main;


TO USE DATABASE:

use main;


TO CREATE TABLE:

create table manager
 (ID varchar(240) PRIMARY KEY,
  Name char(240),
  email varchar(240),
  psd varchar(240),
  contact_info varchar(240),
  bck_up_wrd char(5) ) ;


With this user is good to go and use the program as needed. 

