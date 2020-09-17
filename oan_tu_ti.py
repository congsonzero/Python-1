import random
print("Trò chơi oẳn tù tì")
i=input("Nước đi của bạn:")
may= ['bua','keo','bao']
value=random.choice(may)
print("Nước đi của máy:"+value)
if i==value:
    print("Kết quả hòa")
else:
    if i=="bua":
        if value=="keo":
            print("Bạn thắng")
        else: 
            print("Bạn thua")
    elif i=="keo":
        if value=="bao":
            print("Bạn thắng")
        else: 
            print("Bạn thua")
    elif i=="bao":
        if value=="bua":
            print("Bạn thắng")
        else: 
            print("Bạn thua")
    else:
        print("Nước đi không hợp lê")