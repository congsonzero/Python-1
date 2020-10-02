import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="hoc_sinh"
)
mycursor = mydb.cursor()
print("""Menu
1.Them hoc sinh
2.Danh sach hoc sinh
3 Xoa hoc sinh""")
choice=int(input("Lua chon cua ban:"))
if choice ==1:
    hoten=input()
    Hoten=hoten.split(" ")
    tucam=['Ho Chi Minh','Nguyen Cong Son','A B C D']
    if hoten=="" or hoten.isspace() == True or any(i.isalpha()==False for i in Hoten):
        print("Vui long nhap lai")
    else:
        if hoten in tucam:
            for i in range(len(Hoten)):
                hoten=hoten.replace(Hoten[i],"***")
        age=int(input())
        if age<6 or age>18:
            print("Ban qua tuoi")
        else:
            phone=input()
            f=open("nhamang.txt","r")
            daumangVN=f.read()
            f.close()
            if phone[0]=="+":
                phone="0"+phone[3:]
            elif phone[0]=="8":
                phone="0"+phone[2:]
            if len(phone)>10 or phone.isdigit()==False:
                print("So dt khong hop le")
            else:
                if phone[0:3] in daumangVN:
                    sql = "INSERT INTO sinhvien (Name,Age,Phone) VALUES (%s, %s,%s)"
                    val = (hoten,age,phone)
                    mycursor.execute(sql, val) 
                    mydb.commit()   
                else :
                    print("So dt khong hop le")
elif choice ==2:
    mycursor.execute("SELECT * FROM sinhvien")
    myresult = mycursor.fetchall()    
    for x in myresult:
        print(str(x[0])+"--"+x[1]+"--"+str(x[2])+"--"+x[3])    
elif choice ==3:
    ID=int(input("Nhap so thu tu can xoa"))
    sql="Delete FROM sinhvien WHERE id=ID"
    mycursor.execute(sql)
    mydb.commit()
else:
    print("Lua chon khong hop le")