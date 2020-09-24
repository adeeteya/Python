#Sorting in Python
def bubblesort(l):#maximum number is found and put in the end.(items are bubbled through the array)
   n=len(l)
   for i in range(0,n):
   	  for j in range(0,n-i-1):#n-i-1 is put instead of n-1 to avoid index error.
   	     if(l[j]>l[j+1]):
   	     	l[j],l[j+1]=l[j+1],l[j]#swaps two elements
   return(l)
def selectionsort(l):#minimum number is found and put in the start.(items are selected and put in the start)
	n=len(l)
	for i in range(n):
		min_index=i
		for j in range(i+1,n):
			if(l[j]<l[min_index]):
				min_index=j
		l[i],l[min_index]=l[min_index],l[i]#swapping two element
	return(l)
def insertionsort(l):#items are inserted at the right spots in the array.always compare it to previous items.
	n=len(l)
	for i in range(1,n):
		key=l[i]
		j=i-1
		while(j>=0 and key<l[j]):
			l[j+1]=l[j]#moving an element to it's next position
			j-=1
		l[j+1]=key
	return(l)
def merge(l,first,middle,last):
	L=l[first:middle+1]
	R=l[middle+1:last+1]
	L.append(9999999999999)
	R.append(9999999999999)
	i=j=0
	for k in range(first,last+1):
	   if(L[i]<=R[j]):
	   	    l[k]=L[i]
	   	    i+=1
	   else:
	    	l[k]=R[j]
	    	j+=1
def mergesort(l,first,last):
	if first<last:#checks whether one element is present
	    middle=(first+last)//2
	    mergesort(l,first,middle)#seperating first half
	    mergesort(l,middle+1,last)#seperating second half
	    merge(l,first,middle,last)#merging them back
def quicksort(l):
	if(len(l)<2):
		return l
	else:
		pivot=l.pop()
	items_greater=[]
	items_lesser=[]
	for item in l:
		if(item<=pivot):
			items_lesser.append(item)
		else:
		    items_greater.append(item)
	return quicksort(items_lesser)+[pivot]+quicksort(items_greater)
l=[2,6,2,4,7,8,4,1,6,7,5,3]
print(quicksort(l))