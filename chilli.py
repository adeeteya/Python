import sys,math
N=int(input())
A=input().split()
for i in range(N):
    A[i]=int(A[i])
    if not(0<=A[i]<=10**9):
        print("invalid input")
        sys.exit()
M=int(input())
if not((1<=N<=10**6)and(N<=M<=10**9)):
    print("invalid input")
    sys.exit()
K=math.ceil(sum(A)/M)
print(K)
