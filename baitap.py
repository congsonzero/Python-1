# bai1
# chuoi=[]
# for i in range(2000,3201):
#     if (i%7 ==0)&(i%5!=0):
#         chuoi.append(str(i))
# print(",".join(chuoi))
# n=int(input("nhap n "))
# bai2
# gaithua=1
# for i in range(1,n+1):
#     gaithua=gaithua*i
# print(gaithua)
# def fact(n):
#     if n==0:
#         return 1
#     return fact(n-1)*n
# print(fact(n))
# bai3
# n=int(input("Nhap n "))
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)
# bai4
# chuoi=map(str,input().split(","))
# L=list(chuoi)
# T=tuple(L)
# print(L)
# print(T)
# bai5
# class InputOutString(object):
#     def __init__(self):
#         self.s = ""

#     def getString(self):
#         self.s = input("Nhapchuoi:")

#     def printString(self):
#         print(self.s.upper())


# strObj = InputOutString()
# strObj.getString()
# strObj.printString()
# bai6
# def binhphuong(n):
#     return n*n
# print(binhphuong(int(input())))
# bai7
# print(abs.__doc__)
# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)
# Sử dụng __doc__
# bai8
# class Person:
#     name = "Person"

#     def __init__(self, name=None):
#         self.name = name


# jeffrey = Person("Jeffrey")
# print("%s name is %s" % (Person.name, jeffrey.name))

# nico = Person()
# nico.name = "Nico"
# print("%s name is %s" % (Person.name, nico.name))
# bai9
# import math
# d=list(map(int,input().split(",")))
# C=50
# H=30
# Q=0
# chuoi=[]
# for D in d:
#     chuoi.append(str(int(math.sqrt(2*C*float(D)/H))))
# print(",".join(chuoi))
# bai10
# X,Y=input("Nhap gia tri X va Y ").split(",")
# rownum=int(X)
# colnum=int(Y)
# multilist = [[0 for col in range(colnum)] for row in range(rownum)]
# for row in range(rownum):
#     for col in range(colnum):
#         multilist[row][col]=col*row
# print(multilist)
# bai 11
# chuoi=list(input("Nhap chuoi:").split(","))
# chuoi.sort()
# print(",".join(chuoi))
# bai 12
# lines = []
# while True:
#     s = input()
#     if s:
#             lines.append(s.upper())
#     else:
#         break
# Bài Python 12, Code by Quantrimang.com
# for sentence in lines:
#     print(sentence)
# bai 13
# s=input("Nhap chuoi ")
# n=sorted(set(s.split()))
# print(" ".join(n))
# bai 14
# value = []
# items = [x for x in input("Nhập các số nhị phân: ").split(',')]
# for p in items:
#     intp = int(p, 2) #Chuyen str(so nhi phan) sang int
#     if  intp % 5 ==0:
#         value.append(p)
#     # Bài tập Python 14, viết bởi Quantrimang.com
# print(','.join(value))
# bai 15
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
#  # Bài tập Python 15, Code by Quantrimang.com
# print (",".join(values))
# bai 16
# s=input("Nhap cau cua ban ")
# chu=0
# so=0
# for i in s:
#     if i.isalpha() == True:
#         chu+=1
#     elif i.isdigit() == True:
#         so+=1
# print(chu)
# print(so)
# s = input("Nhập câu của bạn: ")
#  # Bài tập Python 16, Code by Quantrimang.com
#  d={"DIGITS":0, "LETTERS":0}
#  for c in s:
#      if c.isdigit():
#          d["DIGITS"]+=1
#      elif c.isalpha():
#          d["LETTERS"]+=1
#      else:
#          pass
#  print ("Số chữ cái là:", d["LETTERS"])
#  print ("Số chữ số là:", d["DIGITS"])
# bai 17
# s=input("Nhap cau cua ban ")
# d={"upper":0,"lower":0}
# for i in s :
#     if i.isupper()==True:
#         d["upper"]+=1
#     elif i.islower()==True:
#         d["lower"]+=1
#     else:
#         pass
# print(d["upper"])
# print(d["lower"])
# bai 18
# a = input("Nhập số a: ")
# n1 = int("%s" % a)
# n2 = int("%s%s" % (a, a))
# n3 = int("%s%s%s" % (a, a, a))
# n4 = int("%s%s%s%s" % (a, a, a, a))
# print("Tổng cần tính là: ", n1+n2+n3+n4)
# bai 19
# n=list(map(int,input("Nhap day so ").split(",")))
# l=[str(x) for x in n if x%2!=0]
# # for i in n:
# #     if i%2!=0:
# #         l.append(str(i))
# print(",".join(l))
# bai 20
# tien=0
# while True:
#     s=input().split()
#     if s:
#         if s[0]=="D":
#             tien+=int(s[1])
#         elif s[0]=="W":
#             tien-=int(s[1])
#     else :
#         break
# print(tien)
# bai21
# import re
# value = []
# name = input("Nhap ten dang nhap:")
# passwd = list(input("Nhap mat khai:") .split(","))
# for i in passwd:
#     if (len(i)<6 or len(i)>12):
#         continue
#     else :
#         pass
#     if  all(j.islower()==False for j in i):
#         break
#     if all(j.isupper()==False for j in i):
#         break
#     if  all(j.isdigit()==False for j in i):
#         break
#     if  all(j not in ["$", "#","@"]  for j in i):
#         break
#     value.append(i)
# for p in passwd:
#     if len(p) < 6 or len(p) > 12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]", p):
#         continue
#     elif not re.search("[0-9]", p):
#         continue
#     elif not re.search("[A-Z]", p):
#         continue
#     elif not re.search("[$#@]", p):
#         continue
#     elif re.search("\s", p):
#         continue
#     else:
#         pass
#     value.append(p)
# print(",".join(value))
# bai22
# from operator import itemgetter, attrgetter
# l=[]
# while True:
#     s=input()
#     if not s :
#         break
#     l.append(tuple(s.split(",")))
# print(sorted(l,key=itemgetter(0,1,2)))
# bai 23
# def putNumbers(n):
    # i = 0
    # while i < n:
    #     j = i
    #     i = i+1
    #     if j % 7 == 0:
    #         yield j


# Bài tập Python 23 Code by Quantrimang.com
# for i in putNumbers(100):
    # print(i)
# Bai 24
# import math
# pos =[0,0]
# while True:
#     s=tuple(input().split())
#     if s :
#         direction=s[0]
#         step=int(s[1])
#         if direction=="UP":
#             pos[0]+=step
#         elif direction=="DOWN":
#             pos[0]-=step
#         elif direction=="LEFT":
#             pos[1]-=step
#         elif direction=="RIGHT":
#             pos[1]+=step
#         else :
#             break
#     else:
#         pass
# print(int(math.sqrt(pow(pos[0],2)+pow(pos[1],2))))
# bai 25
# dictionary = {}
# while True:
#     s = list(input().split())
#     if s:
#         for i in s:
#             if i in dictionary:
#                 dictionary[i] += 1
#             else:
#                 dictionary[i] = 1
#     else:
#         break
# dictionary = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[0])}
# for i in dictionary:
#     print("{}:{}".format(i,dictionary[i]))
# bai 26
# def tong(a,b):
#     return a+b
# a,b=map(int,input().split())
# print(tong(a,b))
# bai 27
# def string(a):
#     print(str(a))
# string(4)
# bai 28
# def num(a,b):
#     print(int(a)+int(b))
# num(str(3),str(4))
# bai 29
# def printvalue(a,b):
#     print(a+b)
# a=input()
# b=input()
# printvalue(a,b)
# bai 30
# def chieudai(a,b):
#     if len(a)>len(b):
#         print(a)
#     elif len(a)==len(b):
#         print(a)
#         print(b)
#     else:
#         print(b)
# chieudai("one","three")
# bai 31
# def checkValue(n): 
#      if n%2 == 0: 
#  print ("Đây là một số chẵn") 
#      else: 
#         print ("Đây là một số lẻ") 
#  checkValue(7)
# bai 32
# def printDict():
#      d=dict() 
#      d[1]=1 
#      d[2]=2**2 
#      d[3]=3**2 
#      print (d) 
#  # Bài tập Python 32, Code by Quantrimang.com
#  printDict()
# bai 33
# def printDict():
#     d=dict()
#     for i in range(1,21):
#         d[i]=i*i
#     print(d)
# printDict()
# bai 34
# L=[1,2,3,4,5,6,7]
# count=0
# i=0
# while i<6:
#     j=i+1
#     while j<7:
#         j+=1
#         count+=1
#     i+=1
# print(count)    
# bai 35
# def printDict():
#     d=dict()
#     for i in range(1,21):
#         d[i]=i*i
#     for k in d.keys():
#         print(k)
# printDict()
# bai 36
# def printList():
#     li=list()
#     for i in range(1,21):
#         li.append(i*i)
#         print(*li)    
# printList()
# bai 37
# def printList():
#     li=list() 
#     for i in range(1,21): 
#         li.append(i**2) 
#     print (li[:5]) 
#  # Bài Python 37, Code by Quantrimang.com
# printList()
# bai 38
# def printList():
#     li=list()
#     for i in range(1,21):
#         li.append(i**2)
#     print (li[-5:]) 
#  # Bài Python 38, Code by Quantrimang.com
# printList()
# bai 39
# def printList():
#     li=list()
#     for i in range(1,21):
#         li.append(i**2) 
#     print (li[5:]) 
# printList()
# bai 40
# def printTuple():
#     li=list()
#     for i in range(1,21):
#         li.append(i**2)
#     print (tuple(li)) 

# printTuple()
# bai 41
# tp=(1,2,3,4,5,6,7,8,9,10)
# print(tp[:5])
# print(tp[5:])
# bai 42
# tp=(1,2,3,4,5,6,7,8,9,10)
# L=[]
# for i in tp :
#     if (i % 2) == 0:
#         L.append(i)
# print(tuple(L))
# bai 44
# s = input ("Nhập chuỗi: ")
# if s == "yes" or s == "YES" or s == "Yes":
#     print ("Yes")
# else:
#     print ("No")

