import sys
T=int(input())
for j in range(T):
    tmp=input().split()
    N=int(tmp[0])
    P=int(tmp[1])
    Q=int(tmp[2])
    while(True):
        if((N*i)%(P*Q)==0):
            print(i)
            break
