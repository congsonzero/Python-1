import random
print("Menu\n1.Thêm món ăn\n2.Chọn ngẩu nhiên ")
i=int(input('Lựa chọn của bạn là:'))
j=0
if i==1:
    f=open("monan.txt","a")
    f.write(input("Nhập món ăn bạn yêu cầu:")+"\n")
    f.close()
elif i==2:
    f=open("monan.txt","r")
    L=f.readlines()
    print("Menu")
    while j<len(L):
        print(str(j+1)+"."+L[j])
        j+=1    
    f.close()
    print("Món ăn của bạn là "+random.choice(L))
else:
    print("Lựa chọn không hợp lệ")