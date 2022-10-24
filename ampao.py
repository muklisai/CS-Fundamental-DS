import psycopg2 as ps
import pandas as pd

param={
    "host":"localhost",
    "database":"postgres",
    "user":"postgres",
    "password":"postgres",
    "port":5432
}

conn=ps.connect(**param)
cursor=conn.cursor()

pelukis_squery='SELECT * FROM pelukis'
cursor.execute(pelukis_squery)
pelukis=cursor.fetchall()

cursor.close()
conn.close()

df=pd.DataFrame(pelukis)
df.columns=['id_pelukis','nama_pelukis']

df.to_csv(r'C:\Users\N I T R O\OneDrive\Documents\Data Engineering\CS-Fundamental-DS\Gama_Ariefsadya.csv', index=False)
