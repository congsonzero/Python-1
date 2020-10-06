import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="index"
)
mycursor = mydb.cursor()
print("""Menu
1.Them hoc sinh
2.Danh sach hoc sinh
3 Xoa hoc sinh""")
choice = int(input("Lua chon cua ban:"))
i = 0
if choice == 1:
    hoten = input("Nhap ten: ")
    Hoten = hoten.split(" ")
    tucam = ['Ho Chi Minh', 'Nguyen Cong Son', 'Vo Nguyen Giap']
    if hoten == "" or hoten.isspace() == True:
        print("Vui long nhap lai")
    else:
        for j in range(len(tucam)):
            Tcam = tucam[j].split(" ")
            if all(Tcam[k] in hoten for k in range(len(Tcam))):
                for i in range(len(Tcam)):
                    hoten = hoten.replace(Tcam[i], "***")
        age = int(input("Nhap tuoi:"))
        if age < 6 or age > 18:
            print("Ban qua tuoi")
        else:
            phone = input("Nhap so dt: ")
            f = open("nhamang.txt", "r")
            daumangVN = f.read()
            f.close()
            if phone[0] == "+":
                phone = "0"+phone[3:]
            elif phone[0] == "8":
                phone = "0"+phone[2:]
            if len(phone) > 10:
                print("So dt khong hop le")
            else:
                if phone[0:3] in daumangVN:
                    sql = "INSERT INTO sinhvien (Name,Age,Phone) VALUES (%s, %s,%s)"
                    val = (hoten, age, phone)
                    mycursor.execute(sql, val)
                    mydb.commit()
                else:
                    print("So dt khong hop le")
elif choice == 2:
    mycursor.execute("SELECT * FROM sinhvien")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(str(x[0])+"--"+x[1]+"--"+str(x[2])+"--"+x[3])
elif choice == 3:
    ID = int(input("Nhap so thu tu can xoa: "))
    mycursor.execute("SELECT * FROM sinhvien")
    myresult = mycursor.fetchall()
    for x in myresult:
        if ID == x[0]:
            sql = "DELETE FROM sinhvien WHERE id = %s"
            adr = (ID, )
            mycursor.execute(sql, adr)
            mydb.commit()
            i = 1
    if i == 0:
        print("ID ko hop le")
else:
    print("Lua chon khong hop le")
