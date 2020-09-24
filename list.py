#Doubledim array
l=list()
m=int(input("Enter the length of the array"))
n=int(input("Enter the Breadth of the array"))
print("Enter the array elements")
for i in range(m):
	l.append([])
	for j in range(n):
		l[i].append(int(input()))
print("The array Elements are")
for i in range(m):
	for j in range(n):
		print(l[i][j],end='   ')
	print()

