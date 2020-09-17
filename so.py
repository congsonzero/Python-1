so=1
chuoi=''
while so<=100:
    if so%2 ==0:
        if so%3==0:
            chuoi=chuoi+str(so)+'\n'
        else :
            chuoi=chuoi+str(so)
        if so<100:
            chuoi=chuoi+","
    so+=1       
print(chuoi)        
print("Gia tri bat dau "+str(batdau))
print("Gia tri bat dau "+str(ketthuc))
