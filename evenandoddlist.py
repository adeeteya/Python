#even and odd list
#By Aditya.R 19S0604
#1/11/19
a,even,odd=[],[],[]
n=int(input("Enter no of elements "))
print("Enter The Elements ")
for i in range(n):
   a.append(int(input()))
for i in a:
   if(i%2==0):
     even.append(i)
   else:
     odd.append(i)
print("Even Elements: ",even)
print("Odd Elements: ",odd)
