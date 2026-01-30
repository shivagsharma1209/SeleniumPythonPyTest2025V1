#inser, update, delete commands

insert_query = "inser into student values(1001,'shiva')"
update_query = "update student set sname = 'rama' where sid = 101"
delete_query = "delete from student where sid = 101;"

import mysql.connector

try:
    cont = mysql.connector.connect(host="localhost",port=8080, user="root",password="root",database="mydb")
cursor = cont.cursor() # cursor, temp momory
cursor.execute(insert_query)
# cursor.execute(update_query)
# cursor.execute(delete_query)
cont.commit()   #commit the transaction..
cont.close()    # close the connection

except:
    print("Connection error")

print("Inserted new record to the database")





