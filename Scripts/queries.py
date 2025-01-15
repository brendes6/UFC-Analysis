import pandas as pd
import mysql.connector as sql

def query_data(query):
    connection = sql.connect(host="localhost", user="root", password="Daisydog1200$", 
                         database="ufc_matchup_database", connection_timeout=300)
    df = pd.read_sql(query, connection)
    connection.close()
    return df
