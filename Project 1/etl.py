import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    This function takes a filepath, converts the JSON file into a dataframe, selects desired columns, 
    and then inserts the columns into the tables
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0].tolist()
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']].values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    This function takes a filepath, converts the JSON file into a dataframe, selects desired columns, 
    then it transforms the UNIXTIME foudn in the JSON file to various datetime formats,
    and then inserts the columns into the tables
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df.page=='NextSong'].copy()

    # Convert unixtime to datetime and formatted cols
    df['start_time'] = pd.to_datetime(df['ts'], unit='ms')
    df['hour'] = df.start_time.dt.strftime('%H')
    df['day'] = df.start_time.dt.strftime('%d')
    df['week'] = df.start_time.dt.strftime('%U')
    df['month'] = df.start_time.dt.strftime('%m')
    df['year'] = df.start_time.dt.strftime('%Y')
    df['weekday'] = df.start_time.dt.strftime('%w')

    # # convert timestamp column to datetime
    # t = 
    
    # # insert time data records
    # time_data = 
    # column_labels = 
    time_df = df[['start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday']].copy()

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']].copy()

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.start_time, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    This function generates a list of the JSON files by looping through all the directories looking for JSON files. 
    Then for each file it calls the previous functions to transform them and insert them into the tables. 
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        print('one')
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """
    This is the main function that connects with the database and calls the process_data functions.
    """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='Project 1/data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='Project 1/data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()