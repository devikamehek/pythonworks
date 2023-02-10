import pymysql
db=pymysql.connect(host="localhost",user="root",password="Python@1234",database="nov_test")
con=db.cursor()
sql='select * from t1 '
con.execute(sql)
data=con.fetchall()
for i in data:
    id=i[0]
    na=i[1]
    ag=i[2]
    print(f'id={id},  name={na},  age={ag}')