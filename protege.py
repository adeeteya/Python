import math,sys
N=int(input())
A=input().split()
for i in range(N):
    A[i]=int(A[i])
    if not(1<=A[i]<=1000):
        print("invalid input")
        sys.exit()
Q=int(input())
if not((1<=N<=1000)and(1<=Q<=10**5)):
    print('invalid input')
    sys.exit()
for j in range(Q):
    tmp=input().split()
    K=int(tmp[0])#tags
    M=int(tmp[1])#probs
    if not((1<=K<=N)and(1<=M<=K)):
        print('invalid input')
        sys.exit()
    count=0
    for i in range(N):
        if(i<=K):
            if(M>A[i]):
                count+=K
            else:
                count+=(math.factorial(A[i])//math.factorial(A[i]-M))
        else:
            break
    print(count)
