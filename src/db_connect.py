from configparser import ConfigParser
from dotenv import load_dotenv
import polars as pl
import psycopg2
import os

load_dotenv()

def start_conn():
    connection = psycopg2.connect(
        database=os.getenv('database'),
        user=os.getenv('username'),
        host=os.getenv('host'),
        password=os.getenv('password'),
        port=os.getenv('port')
    )
    return(connection)

# write_db() really only for initial push to create tables
def write_db(df, table_name):
    df.write_database(
        table_name=table_name,
        connection=os.getenv('uri'),
        if_table_exists='replace'
    )
    return

def pull_db(query, connection):
    cursor = connection.cursor()
    cursor.execute(query)
    record = cursor.fetchall()
    return(record)

def check_table_exists(table_name, connection):
    cursor = connection.cursor()
    cursor.execute("""
    SELECT EXISTS (
        SELECT FROM information_schema.tables 
        WHERE table_name = %s
    );""",
    (table_name,))
    exists = cursor.fetchone()[0]
    return exists