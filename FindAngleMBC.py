import math
ab=int(input())
bc=int(input())
mbc=math.degrees(math.atan(ab/bc))
if mbc<(int(mbc)+0.5):
    print(str(int(mbc))+"°")
else :
    print(str(int(mbc)+1)+"°")
