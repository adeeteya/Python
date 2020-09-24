import sys
T=int(input())
for j in range(T):
    tmp=input().split()
    N=int(tmp[0])
    K=int(tmp[1])
    A=list(map(int,input().split()))
    m=1
    for i in A:
        m*=i
    i=0
    while(True):
        if(N*i==m):
            print(i)
            break
        i+=1
