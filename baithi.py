hoten=input()
Hoten=hoten.split(" ")
tucam=['Ho Chi Minh','Nguyen Cong Son','A B C D']
if hoten=="":
    print("Vui long nhap lai")
elif hoten.isspace() == True:
    print("Vui long nhap lai")
elif any(i.isalpha()==False for i in Hoten) :
    print("Vui long nhap lai")
else:
    if hoten in tucam:
        for i in range(len(Hoten)):
            hoten=hoten.replace(Hoten[i],"***")
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
            print(hoten)
            print(phone)
        else :
            print("So dt khong hop le")
