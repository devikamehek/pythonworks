"""inserting into db"""
import pymysql
db=pymysql.connect(host="localhost",user="root",password="Python@1234",database="nov_test")
con=db.cursor()
sqlquerry="insert into t1 values(%s,%s,%s)"
val=(13,"anjalii",24)
con.execute(sqlquerry,val)
db.commit()
print("inserted")
