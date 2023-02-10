import pymysql
id=int(input("enter id: "))
db1=pymysql.connect(host="localhost",user="root",password="Python@1234",database="nov_test")
mycursor=db1.cursor()
sql="delete from t1 where id='%d'"%(id)
mycursor.execute(sql)
db1.commit()
print("deleted successfully")