import psycopg2
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import polars as pl

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

# write_db() really only for initial push
def write_db(df):
    df.write_database(
        table_name='rolling_sales',
        connection=os.getenv('uri'),
        if_table_exists='replace'
    )
    return

def pull_db(query, connection):
    cursor = connection.cursor()
    cursor.execute(query)
    record = cursor.fetchall()
    return(record)