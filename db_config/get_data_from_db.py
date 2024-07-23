
from mysql_creds import credentials
from sqlalchemy import create_engine, text as sql_text
import pandas as pd

def connection(database : str):
      return f"mysql+mysqlconnector://root:{credentials['password']}@localhost:3306/{database}"


def get_data(database : str, table : str):
     engine =  create_engine(connection(database)).connect()
     query = "SELECT * FROM " + table
     df = pd.read_sql_query(con = engine, sql = sql_text(query))
     return df


