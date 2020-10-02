# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="python"
# )
# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM sinhvien")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print('-'.join(x[i] for i in range(x)))

# sql = "INSERT INTO sinhvien (name, phone) VALUES (%s, %s)"
# val = ("ABCD", "0975676512")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")
# sql="Delete FROM sinhvien WHERE id=10"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")
A=(1, 'Cong Son', 15, '0975676512')
print(str(A[0])+"--"+A[1]+"--"+str(A[2])+"--"+A[3])



