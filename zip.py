N,X=map(int,input().split())
L=[]
for i in range (X):
    S=list(map(float,input().split()))
    L.append(S)
Y=list(zip(*L))
for i in range(len(Y)):
    arg=sum(Y[i])/ N
