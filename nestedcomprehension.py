#nested list comprehension
#By Aditya.R 19S0604
#1/11/19
l=[i for i in range(1,1001) if 'k' in['k' for j in range(2,10) if(i%j==0)]]
print(l)