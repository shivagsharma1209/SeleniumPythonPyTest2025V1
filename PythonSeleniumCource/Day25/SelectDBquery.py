import mysql.connector

try:
    cont = mysql.connector.connect(host='localhost',port=3306,user='root',passwd='',database='python')
    cursor = cont.cursor()
    cursor.execute('select * from employee')
    results = cursor.fetchall()
    for row in results:
        print(row[0],row[1])
    cont.close()
except mysql.connector.Error as error:
    print("Connection error")

