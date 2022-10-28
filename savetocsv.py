import psycopg2
import pandas as pd
import pandas.io.sql as sqlio

host = 'localhost'
port = 5432
dbname = 'belajar'
username = 'postgres'
pwd = 'postgre'

conn = psycopg2.connect("host='{}' port={} dbname='{}' user={} password={}".format(host, port, dbname, username, pwd))

cursor = conn.cursor()

cursor.execute("Select * From pelukis")
data = pd.DataFrame(cursor.fetchall())
data

data.to_csv('pelukis.csv')