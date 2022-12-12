# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id serial PRIMARY KEY, start_time timestamp NOT NULL, user_id bigint NOT NULL, level text, song_id text, artist_id text, session_id bigint, location text, user_agent text);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id bigint PRIMARY KEY, first_name text, last_name text, gender text, level text);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id text PRIMARY KEY, title text NOT NULL, artist_id text, year int, duration int NOT NULL);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id text PRIMARY KEY, name text NOT NULL, location text, latitude double precision, longitude double precision);
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS time (start_time timestamp PRIMARY KEY, hour smallint, day smallint, week smallint, month smallint, year smallint, weekday int); 
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays VALUES (DEFAULT, %s, %s, %s, %s, %s ,%s , %s, %s) ON CONFLICT (songplay_id) DO NOTHING
""")

user_table_insert = (""" INSERT INTO users VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO NOTHING
""")

song_table_insert = (""" INSERT INTO songs VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = (""" INSERT INTO artists VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = (""" INSERT INTO time VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = (""" SELECT song_id, artist_id FROM songs JOIN artists using(artist_id) WHERE title = %s AND name = %s and duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]