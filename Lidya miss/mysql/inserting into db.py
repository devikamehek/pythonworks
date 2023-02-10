import pymysql
id=int(input("enter id: "))
na=input("enter name: ")
ag=int(input("enter age: "))
db1=pymysql.connect(host="localhost",user="root",password="Python@1234",database="nov_test")
mycursor=db1.cursor()
sql="insert into t1 values(%s,%s,%s)"
val=(id,na,ag)
mycursor.execute(sql,val)
db1.commit()
print("inserted successfully")