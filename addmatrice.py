#Matrice addition
l1=list()
m1=int(input("Enter the length of the array"))
n1=int(input("Enter the breadth of the array"))
print("Enter the Values for the first list")
for i in range(m1):
  l1.append([])
  for j in range(n1):
    l1[i].append(int(input()))
l2=list()
m2=int(input("Enter the length of the array"))
n2=int(input("Enter the breadth of the array"))
print("Enter the Values for the second list")
for i in range(m2):
  l2.append([])
  for j in range(n2):
    l2[i].append(int(input()))
if(m1!=m2) or (n1!=n2):
  print("Matrice Addition is not possible")
  exit()
l3=list()
for i in range(m2):
  l3.append([])
  for j in range(n2):
    l3[i].append(l1[i][j]+l2[i][j])
print("The Sum of two Arrays are")
print(l3)
