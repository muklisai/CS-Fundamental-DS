import psycopg2
import pandas as pd 

try:
    # Connect to a database
    conn = psycopg2.connect(host="localhost",
                            database="postgres",
                            password="Test123",
                            user="postgres",
                            port=5432,
    )

    # Create a cursor 
    cursor = conn.cursor()
    
    # === Create table pelukis ===
    create_table_pelukis = ''' CREATE TABLE IF NOT EXISTS pelukis (
                                pelukis_id SERIAL PRIMARY key,
                                nama_pelukis VARCHAR(255));
                            '''
    # Execute command
    cursor.execute(create_table_pelukis)
    conn.commit()
    print("Table created successfully")
    
    # === Insert data into table pelukis === 
    insert_query = ''' INSERT INTO pelukis (pelukis_id, nama_pelukis)
                        VALUES(1, 'Edward'),
                        (2, 'Chris'),
                        (3, 'Adam'),
                        (4, 'Stone'),
                        (5, 'Tim');
                    '''
    cursor.execute(insert_query)
    conn.commit()
    print("Data has been inserted")
    
    
    # === Get data from database & convert to DataFrame ===
    cursor.execute("SELECT * FROM pelukis")
    records = cursor.fetchall()
    df = pd.DataFrame(records, columns=['pelukis_id', 'nama_pelukis'])
    df
    
finally:
    # closing database connection
    if conn:
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")

# convert file to csv
df.to_csv(r'C:\Users\valou\Desktop\CS-Fundamental-DS\Pelukis_result.csv', index=False)