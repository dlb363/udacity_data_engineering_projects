# README
## Purpose of sparkifydb 
The purpose is to keep track of the attributes of both our users and artists
Artists
- name and location
Songs
- every song we have, the year it came out, duration, etc.
Users
- gender, location, etc.

As well as how our users interact with our sounds
Songplays
- Each play for each user with location and level

In our to gain business insights

## How to run the Python scripts
As new files get uploaded to our system, there will be a cronjob that runs the etl.py job daily to automatically run all the python scrtips

## An explanation of the files in the repository
sql_queries.py - defines the delete, create table, and insertion queries for all the tables
create_tables.py - creates connection to the db and runs the queries in sql_queries.pu
etl.py = main function that runs create_tables.py, then loops through our files and inserts them into the database. 
test.ipynb/etl.ipynb - internal tool for testing
 
## Schema explanation
I'm using a STAR type schema. We have a central Fact table `songplays` table that records each time a user plays a song. Then we have connecting Dimensional tables `users`, `artists`, `songs` that record the attributes of the users, artists and songs referrenced in `songplays`. 

## ETL explanation
First we process the Dimensional tables, looping through the song_data files. We do some datetime transformations to convert UNIX time into various time attributes. Then we use the data we created in the previous step to make a detailed Fact table `songplays`, combining both the attribute data from the tables and fact data from the log_data JSON files. 



