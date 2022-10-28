import psycopg2
import pandas as pd
import pandas.io.sql as sqlio

host = 'localhost'
port = 5432
dbname = 'postgres'
username = 'postgres'
pwd = 'Guitarhero7777'

conn = psycopg2.connect("host='{}' port={} dbname='{}' user={} password={}".format(host, port, dbname, username, pwd))

cursor = conn.cursor()

cursor.execute("Select * From pelukis")
data = pd.DataFrame(cursor.fetchall())
data.columns=['pelukis_id','nama_pelukis']

data.to_csv('pelukis.csv',index=False)