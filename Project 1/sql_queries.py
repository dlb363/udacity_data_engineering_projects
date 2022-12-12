# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id serial, start_time timestamp, user_id bigint, level text, song_id text,  artist_id text, session_id bigint, location text, user_agent text);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id bigint, first_name text, last_name text, gender text, level text);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id text, title text, artist_id text, year int, duration int);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id text, name text, location text, latitude double precision, longitude double precision);
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS time (start_time timestamp, hour smallint, day smallint, week smallint, month smallint, year smallint, weekday int); 
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays VALUES (%s, %s, %s, %s, %s, %s ,%s , %s, %s)
""")

user_table_insert = (""" INSERT INTO users VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = (""" INSERT INTO songs VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = (""" INSERT INTO artists VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = (""" INSERT INTO time VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = (""" SELECT song_id, artist_id FROM songs JOIN artists using(artist_id) WHERE title = %s AND name = %s and duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]