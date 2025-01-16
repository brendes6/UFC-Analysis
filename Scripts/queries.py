import pandas as pd
import mysql.connector as sql

# Fill in with your mysql user/password
my_user = ""
my_password = ""

def query_data(query):
    connection = sql.connect(host="localhost", user=my_user, password=my_password, 
                         database="ufc_matchup_database", connection_timeout=300)
    df = pd.read_sql(query, connection)
    connection.close()
    return df
