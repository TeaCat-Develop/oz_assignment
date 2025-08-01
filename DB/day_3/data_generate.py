#terminal>>> pip install mysql-connector-python faker

import mysql.connector
from faker import Faker
import random #python 기본모듈

#(1)mysql 연결설정
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0000',
    database='oz_assignment'
)

# (2) mysql 연결
cursor = db_connection.cursor()
faker = Faker()

# useers 데이터 생성
for _ in range(100):
    username = faker.user_name()
    # print(username)
    email = faker.email()
    
    sql = 'INSERT INTO users(username, email) VALUES(%s, %s)'
    values = (username,email)
    
    cursor.execute(sql, values)

# user_id 불러오기
cursor.execute('SELECT user_id FROM users')
valid_user_id = [row[0] for row in cursor.fetchall()]

# 100개의 주문 더미 데이터 생성
for _ in range(100):
    user_id = random.choice(valid_user_id)
    product_name = faker.word()
    quantity = random.randint(1,10)

    try:
        sql = 'INSERT INTO orders(user_id, product_name, quantity) VALUES(%s,%s, %s)'
        values = (user_id, product_name, quantity) # 컬럼명=변수 쓰는게 좋음 
    
        cursor.execute(sql, values)
    except:
        pass

db_connection.commit()
cursor.close()
db_connection.close()