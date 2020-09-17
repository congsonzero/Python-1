x="""Tàu sân bay Mỹ USS Ronald Reagan cùng các tàu tấn công đổ bộ USS America, USS New Orleans và USS Germantown tham gia cuộc tập trận quy mô lớn mang tên Valiant Shield 2020 (Lá chắn dũng cảm 2020) từ ngày 14 - 25.9 tại Guam, theo thông báo của Hạm đội Thái Bình Dương.
Chuẩn Đô đốc Michael Boyle, phụ trách các chiến dịch hải quân thuộc  Hạm đội Thái Bình Dương, cho biết Valiant Shield 2020 bao gồm những cuộc diễn tập phối hợp trên bộ, trên biển và trên không quanh đảo Guam nằm ở trung tâm Thái Bình Dương nhằm tăng cường năng lực phối hợp tác chiến của các lực lượng.
“Điều tối quan trọng là phải chứng minh cho các đồng minh và đối tác rằng Mỹ giữ vững cam kết đối với một khu vực Ấn Độ Dương - Thái Bình Dương tự do và rộng mở”, ông Boyle nhấn mạnh trong một tuyên bố ngày 11.9. """
y="abc decf hcadjh vdahajfdhj hfahhkjfag"
a=x.split(" ")
i=0
tong=0
j=0
while i<= (len(a)-1):
    if tong<=100:
        tong=tong+len(a[i])
    else: break
    i=i+1
print(i)
chuoi=""
while j<i:
    chuoi=chuoi+" "+a[j]
    j=j+1
vanban="{}..."
print(vanban.format(chuoi))
f=open("tucam.txt","r")
L=f.readlines()
t=0
while t<len(L):
    if L[t] in chuoi:
        chuoi=chuoi.replace(L[t],"***")
    t=t+1
print(chuoi)








    
