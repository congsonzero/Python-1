N=int(input())
I=input().split(" ")
print(all(int(i)>0 for i in I) and any(j==j[::-1] for j in I))