import mysql.connector as conn
mydb=conn.connect(host='localhost',database="information",user='root')
print(mydb)
print("Connection Done Success !!")