#Searching in python
def linearsearch(l,x):
   for i in range(len(l)):
   	  if(l[i]==x):
   	  	print("The index is ",i)
   	  	break
def functionsearch(l,x):
	if(x in l):
		print("Index:",l.index(x))
def binarysearch(l,start,end,x):
	if(start<=end):
		middle=start+(end-start)//2
		if(l[middle]==x):
			return middle
		elif(l[middle]>x):
			return binarysearch(l,start,middle-1,x)
		else:
		    return binarysearch(l,middle+1,end,x)
	else:
		return -1

l=[1,2,3,4,5,6,7,8,9,10,11,22,33,44,55]
linearsearch(l,6)
functionsearch(l,6)
print(binarysearch(l,0,len(l)-1,6)) 