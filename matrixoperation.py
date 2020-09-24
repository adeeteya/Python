#Matrix Operations
#By Aditya R 19S0604
#1/11/19
import sys
def accept(m,n):
   print("Enter The Values of the matrices ")
   l=[]
   for i in range(m):
      l.append([])
      for j in range(n):
         l[i].append(int(input()))
   return l
def addition():
   r=[]
   for i in range(m1):
      r.append([])
      for j in range(n1):
         r[i].append(a[i][j]+b[i][j])
   for z in r:
      print(z)
def multiplication():
   r=[]
   for i in range(m1):
      r.append([])
      for j in range(n2):
        r[i].append(0)
   for i in range(len(a)):
      for j in range(len(b[0])):
        for k in range(len(b)):
           r[i][j]+=a[i][k]*b[k][j]
   for z in r:
      print(z)
m1=int(input("Enter no of rows of mat1 "))
n1=int(input("Enter no of columns of mat1 "))
a=accept(m1,n1)
m2=int(input("Enter no of rows of mat2 "))
n2=int(input("Enter no of columns of mat2 "))
b=accept(m2,n2)
chk=int(input("Enter 0 for addition or 1 for multiplication "))
if(chk==0):
  if(m1==m2)and(n1==n2):
     addition()
  else:
     print("Addition not possible")
     sys.exit()
elif(chk==1):
  if(n1==m2):
    multiplication()
  else:
    print("Multiplication not possible")
    sys.exit()
else:
    print("Invalid Input")
    sys.exit()


