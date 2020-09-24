#Unit Matrice check
l=list()
m=int(input("Enter the lenght of the array"))
n=int(input("Enter the breadth of the array"))
print("Enter the Values")
for i in range(m):
  l.append([])
  for j in range(n):
    l[i].append(int(input()))
z=0
for i in range(m):
  for j in range(n):
    if(i==j):
      if(l[i][j]==1):
        z=1
      else:
        z=0
        break
    else:
       if(l[i][j]==0):
         z=1
       else:
         z=0
         break
if(z==1):
  print("It is a Unit Matrice")
else:
  print("It is not a Unit Matrice")
