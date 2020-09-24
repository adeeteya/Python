import sys
N=int(input())
A=input().split()
for i in range(N):
    A[i]=int(A[i])
    if not(0<=A[i]<=10**5):
        print("invalid input")
        sys.exit()
H=int(input())
tmp=input().split()
X=int(tmp[0])
K=int(tmp[1])
if not((1<=N<=10**5)and(0<=H<=10**5)and(0<=X<=10**5)and(0<=K<=10**5)):
    print("invalid input")
    sys.exit()
for i in range(N):
    while(A[i]>H)and(K!=0):
        K-=1
        H+=X
    H-=A[i]
    if(H<0):
        print("Retire")
        sys.exit()
print('Fight')
