snt=0
so=int(input('Nhap so '))
i=2
while i<so:
    if so%i==0:
        print(so,"khong la so nguyen to") 
        break
    else :
         print(so," la so nguyen to") 
         break
    i=i+1
