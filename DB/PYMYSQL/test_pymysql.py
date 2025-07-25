import pymysql

# (1) db connection
connection = pymysql.connect(
    host='localhost', # = 127.0.0.1
    user='root',
    password='0000',
    db='classicmodels', # 데이터베이스 지정
    charset='utf8mb4', # emoji 등 호환
    
    cursorclass=pymysql.cursors.DictCursor 
    
    # 커서값의 기본형(DefaultCursor)은 튜플
    # => 심플하고 빠름. but json으로 받거나 데이터 변경불가 등 제한많음
    # 데이터 실사용을 위해 DictCursor 사용
)

cursor = connection.cursor()

sql = 'SELECT * FROM customers'
cursor.execute(sql) # 실행시키기


customers = cursor.fetchone() # 가져오기
print('customers:',customers)
print('customers:',customers['customerNumber'])
print('customers:',customers['country'])
print('customers:',customers['customerName'])


# {'key':'value'} => json => {'key':'value'}

# (1,'name','country') => X