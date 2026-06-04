import pymysql
conn=pymysql.connect(user='root', password='vishal@21',port=3306,charset='utf8',host='localhost')
print("db connected")
conn.close()
print("db disconnected")

