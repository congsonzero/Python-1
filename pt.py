from math import sqrt

print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
#Nhập hệ số phương trính
a=float(input('Nhập hệ số a = '))
b=float(input('Nhập hệ số b = '))
c=float(input('Nhập hệ số c = '))
if a==0:
    if b==0:
        if c==0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x=-c/b
        print("Phương trình có nghiệm duy nhất",x)
else:
        #Tính giá trị delta
        delta=b*b-4*a*c
        if delta < 0:
            print("Phương trình vô nghiệm")
        elif delta==0:
            x=-b/(2*a)
            print("Phương trình nghiệm duy nhất",x)
        else:
            x1=(-b+ sqrt(delta))/(2*a)
            x2=(-b- sqrt(delta))/(2*a)
            print("phương trình có 2 nghiệm ",x1,x2)



