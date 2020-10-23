bai1
chuoi=[]
for i in range(2000,3201):
    if (i%7 ==0)&(i%5!=0):
        chuoi.append(str(i))
print(",".join(chuoi))
n=int(input("nhap n "))
bai2
gaithua=1
for i in range(1,n+1):
    gaithua=gaithua*i
print(gaithua)
def fact(n):
    if n==0:
        return 1
    return fact(n-1)*n
print(fact(n))
bai3
n=int(input("Nhap n "))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)
bai4
chuoi=map(str,input().split(","))
L=list(chuoi)
T=tuple(L)
print(L)
print(T)
bai5
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Nhapchuoi:")

    def printString(self):
        print(self.s.upper())


strObj = InputOutString()
strObj.getString()
strObj.printString()
bai6
def binhphuong(n):
    return n*n
print(binhphuong(int(input())))
bai7
print(abs.__doc__)
print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)
Sử dụng __doc__
bai8
class Person:
    name = "Person"

    def __init__(self, name=None):
        self.name = name


jeffrey = Person("Jeffrey")
print("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print("%s name is %s" % (Person.name, nico.name))
bai9
import math
d=list(map(int,input().split(",")))
C=50
H=30
Q=0
chuoi=[]
for D in d:
    chuoi.append(str(int(math.sqrt(2*C*float(D)/H))))
print(",".join(chuoi))
bai10
X,Y=input("Nhap gia tri X va Y ").split(",")
rownum=int(X)
colnum=int(Y)
multilist = [[0 for col in range(colnum)] for row in range(rownum)]
for row in range(rownum):
    for col in range(colnum):
        multilist[row][col]=col*row
print(multilist)
bai 11
chuoi=list(input("Nhap chuoi:").split(","))
chuoi.sort()
print(",".join(chuoi))
bai 12
lines = []
while True:
    s = input()
    if s:
            lines.append(s.upper())
    else:
        break
Bài Python 12, Code by Quantrimang.com
for sentence in lines:
    print(sentence)
bai 13
s=input("Nhap chuoi ")
n=sorted(set(s.split()))
print(" ".join(n))
bai 14
value = []
items = [x for x in input("Nhập các số nhị phân: ").split(',')]
for p in items:
    intp = int(p, 2) #Chuyen str(so nhi phan) sang int
    if  intp % 5 ==0:
        value.append(p)
    # Bài tập Python 14, viết bởi Quantrimang.com
print(','.join(value))
bai 15
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
 # Bài tập Python 15, Code by Quantrimang.com
print (",".join(values))
bai 16
s=input("Nhap cau cua ban ")
chu=0
so=0
for i in s:
    if i.isalpha() == True:
        chu+=1
    elif i.isdigit() == True:
        so+=1
print(chu)
print(so)
s = input("Nhập câu của bạn: ")
 # Bài tập Python 16, Code by Quantrimang.com
 d={"DIGITS":0, "LETTERS":0}
 for c in s:
     if c.isdigit():
         d["DIGITS"]+=1
     elif c.isalpha():
         d["LETTERS"]+=1
     else:
         pass
 print ("Số chữ cái là:", d["LETTERS"])
 print ("Số chữ số là:", d["DIGITS"])
bai 17
s=input("Nhap cau cua ban ")
d={"upper":0,"lower":0}
for i in s :
    if i.isupper()==True:
        d["upper"]+=1
    elif i.islower()==True:
        d["lower"]+=1
    else:
        pass
print(d["upper"])
print(d["lower"])
bai 18
a = input("Nhập số a: ")
n1 = int("%s" % a)
n2 = int("%s%s" % (a, a))
n3 = int("%s%s%s" % (a, a, a))
n4 = int("%s%s%s%s" % (a, a, a, a))
print("Tổng cần tính là: ", n1+n2+n3+n4)
bai 19
n=list(map(int,input("Nhap day so ").split(",")))
l=[str(x) for x in n if x%2!=0]
# for i in n:
#     if i%2!=0:
#         l.append(str(i))
print(",".join(l))
bai 20
tien=0
while True:
    s=input().split()
    if s:
        if s[0]=="D":
            tien+=int(s[1])
        elif s[0]=="W":
            tien-=int(s[1])
    else :
        break
print(tien)
    
        