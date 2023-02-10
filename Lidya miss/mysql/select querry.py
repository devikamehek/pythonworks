import pymysql
id=int(input("enter the id: "))
db=pymysql.connect(host="localhost",user="root",password="Python@1234",database="nov_test")
con=db.cursor()
sql='select * from t1 where id=%d'%id
con.execute(sql)
i=con.fetchone() #1 data fetching
id=i[0]
na=i[1]
ag=i[2]
print(f'id={i[0]},  name={na},  age={ag}')

