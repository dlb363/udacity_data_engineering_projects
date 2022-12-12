# DROP TABLES

songplay_table_drop = "DROP table songplays"
user_table_drop = "DROP table users"
song_table_drop = "DROP table songs"
artist_table_drop = "DROP table artists"
time_table_drop = "DROP table time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id bigint, start_time bigint, user_id bigint, level text, song_id bigint,  artist_id bigint, session_id bigint, location text, user_agent text);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id bigint, first_name text, last_name text, gender text, level text);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id bigint, title text, artist_id bigint, year int, duration int);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id bigint, name text, location text, latitude double precision, longitude double precision);
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS time (start_time bigint, hour smallint, day smallint, week smallint, month smallint, year smallint, weekday boolean); 
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays VALUES (%s, %s, %s, %s, %s, %s ,%s , %s, %s)
""")

user_table_insert = (""" INSERT INTO users VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = (""" INSERT INTO songs VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = (""" INSERT INTO artists VALUES (%s, %s, %s, %s, %s, %s)
""")


time_table_insert = (""" INSERT INTO time VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]