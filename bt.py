a="hOcPython Aptech.aaa.zip.png"
#b=a.split(".")
#c=b[len(b)-1]
#print(c)
b=a.rfind('.')+1
c=a[b:]
print(c)
image=["jpg","png","gif","jpeg"]
if len(a)<=0:
    print("please enter file name")
else:
    if c in image:
        print("File Image")
        a=a.lower()
        a=a.replace(" ", "_")
        chuoi="file:{}"
        print(chuoi.format(a))
    else :
        print("File wrong")
#Hôm nay là Quốc Khánh 2/9 Bác hồ đọc tuyên ngôn độc lập
while i<=len(x):
    if x[i] ==" ":
        break
    i=i+1
y=x[:i]
vanban="{}..."
print(vanban.format(y))
z=y.replace(" ","")
