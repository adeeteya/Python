import time
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


def merge_sort(arr):
    if(len(arr)<=1):
        return arr
    middle_index=len(arr)//2
    left_sorted=merge_sort(arr[:middle_index])
    right_sorted=merge_sort(arr[middle_index:])
    return merge(left_sorted,right_sorted)
def merge(left,right):
    result=[]
    while(left and right):
        if(left[0]<right[0]):
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    if(left):
        result+=left
    if(right):
        result+=right
    return result

def quick_sort(arr):
    if(len(arr)<=1):
        return arr
    pivot=len(arr)//2     #taking middle element as the pivot.
    pivot_element=arr[pivot]
    arr[0],arr[pivot]=arr[pivot],arr[0] #swap
    greater_than_arr,lesser_than_arr=[],[]
    for element in range(1,len(arr)):
        if(arr[element]>pivot_element):
            greater_than_arr.append(arr[element])
        else:
            lesser_than_arr.append(arr[element])
    return quick_sort(lesser_than_arr)+[pivot_element]+quick_sort(greater_than_arr)


from random import randrange,shuffle
def memoryoptimisedquick_sort(arr,start,end):
    if(start>=end):
        return
    pivot=randrange(start,end+1)
    pivot_element=arr[pivot]
    arr[end],arr[pivot]=arr[pivot],arr[end]
    lesser_than_idx=start
    for idx in range(start,end):
        if(arr[idx]<=pivot_element):
            arr[idx],arr[lesser_than_idx]=arr[lesser_than_idx],arr[idx]
            lesser_than_idx+=1
    arr[lesser_than_idx],arr[end]=arr[end],arr[lesser_than_idx]
    memoryoptimisedquick_sort(arr,start,lesser_than_idx-1)
    memoryoptimisedquick_sort(arr,lesser_than_idx+1,end)
    return arr


def radix_sort(arr):#LSD radix sort
    maximum_exponent=len(str(max(arr)))
    number_list=arr[:]
    for exponent in range(maximum_exponent):
        index=-(exponent+1)
        digits_bucket=[[] for x in range(10)]
        for number in number_list:
            str_of_number=str(number)
            try:
                digit=str_of_number[index]
            except IndexError:
                digit=0
            digit=int(digit)
            digits_bucket[digit].append(number)
        number_list=[]
        for numeral in digits_bucket:
            number_list.extend(numeral)
    return number_list


f=open('sortingresults.txt','a+')




unsorted_list=[x for x in range(1000000,0,-1)]
shuffle(unsorted_list)
f.write("Input size :"+str(len(unsorted_list)))
f.write("\n")

#start=time.process_time()
#bubble_sort(unsorted_list)#O(n^2) runtime
#end=time.process_time()
f.write("Time elapsed by bubble_sort : Out of Competition")
f.write("\n")

start=time.process_time()
merge_sort(unsorted_list)#O(nlog(n)) runtime
end=time.process_time()
f.write("Time elapsed by merge_sort : "+str(end-start))
f.write("\n")

start=time.process_time()
quick_sort(unsorted_list)#O(nlog(n)) average runtime
end=time.process_time()
f.write("Time elapsed by quick_sort : "+str(end-start))
f.write("\n")

start=time.process_time()
memoryoptimisedquick_sort(unsorted_list,0,len(unsorted_list)-1)#O(nlog(n)) average runtime
end=time.process_time()
f.write("Time elapsed by memoryoptimisedquick_sort : "+str(end-start))
f.write("\n")

start=time.process_time()
radix_sort(unsorted_list)#O(wn) runtime, where w is constant
end=time.process_time()
f.write("Time elapsed by radix_sort : "+str(end-start))
f.write("\n\n\n")
f.close()
