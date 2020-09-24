n=int(input("Enter a number: "))
s=0
print(" "*(n-1)*3,"\b1")
for i in range(2,n+1):
    print(end=" "*(n-i)*3)
    for j in range(i,0,-1):
        print(j,end=' ')
    if(i>2):
        s+=2
        print(end=" "*s)
    for j in range(1,i+1):
        print(j,end=" ")
    print()
s-=2
for i in range(n-1,1,-1):
    print(end=" "*(n-i)*3)
    for j in range(i,0,-1):
        print(j,end=' ')
    if(i>2):
        print(end=" "*s)
        s-=2
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print(" "*(n-1)*3,"\b1")
