import pymysql
def db_connect():
    conn=None
    try:
        conn=pymysql.connect(user='root', password='vishal@21',port=3306,database='vishal_db',charset='utf8',host='localhost')
        print("db connected")
    except Exception as e:
        print("db connection failed")
    return conn

def db_disconnect(conn):
    try:
        conn.close
        print('db disconnected')
    except:
        print("db connection failed")
conn=db_connect()
db_disconnect(conn)
    