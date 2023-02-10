import pymysql
y=input("do you want to update: ")
if y=="yes":
    db=pymysql.connect(host="localhost",user="root",password="Python@1234",database="nov_test")
    id=int(input("enter the id: "))
    na=input("enter the name: ")
    ag=int(input("enter the age: "))
    c=db.cursor()
    sql="update t1 set name='%s', age='%d' where id='%d'"%(na,ag,id)
    c.execute(sql)
    db.commit()
    print("table updated")
elif y=="no":
    print("exit")

