import pymysql
import db_connect2 as dbc
def create_db():
    query='create database if not exist kota_db'
    try:
        conn=dbc.db_connect()
        print("connected sucessfully")
        cursor=conn.cursor()
        result=cursor.execute(query)
        conn.commit()
        cursor.close()
        dbc.db_disconnect(conn)
        if result == 1:
            print("database created successfully")
        else:
            print("db alresady existed")
    except Exception as e:
        print("error while creating database")
create=create_db()
        


              
        