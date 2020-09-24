#generating a random number and storing it in a list and sorting the list
import random as rn
l=list()
for i in range(10):
  l.append(rn.randint(0,100))
print(l)
print("The sorted list is ")
for i in range(10):
  for j in range(i+1,10):
    if(l[i]>l[j]):
      l[i],l[j]=l[j],l[i]
print(l)
print("Descending Sort using a function and a parameter")
l.sort(reverse=True)
#l.reverse()
print(l)
