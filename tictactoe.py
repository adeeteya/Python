import sys,os
def display(arr):
    for element in arr[:3]:
        if(element==0):
            print(end=" |")
        else:
            print(element,end='|')
    print()
    print("------")
    for element in arr[3:6]:
        if(element==0):
            print(end=" |")
        else:
            print(element,end='|')
    print()
    print("------")
    for element in arr[6:]:
        if(element==0):
            print(end=" |")
        else:
            print(element,end='|')
    print("\n")
print("Let's Play")
print("Input position from 1-9")
arr=[0 for i in range(9)]
display(arr)
for i in range(9):
    pos=int(input())
    while(arr[pos-1]!=0):
        print("Invalid Position Enter again\n")
        pos=int(input())
    arr[pos-1]='x' if(i%2==0) else 'o'
    os.system('cls')
    display(arr)
    if((arr[0]==arr[1]==arr[2])or(arr[0]==arr[3]==arr[6])or(arr[0]==arr[4]==arr[8]))and(arr[0]!=0):
        print(arr[0]," has won")
        sys.exit()
    if(arr[1]==arr[4]==arr[7])and(arr[1]!=0):
        print(arr[1]," has won")
        sys.exit()
    if((arr[2]==arr[5]==arr[8])or(arr[2]==arr[4]==arr[6]))and(arr[2]!=0):
        print(arr[2]," has won")
        sys.exit()
    if(arr[3]==arr[4]==arr[5])and(arr[3]!=0):
        print(arr[3]," has won")
        sys.exit()
    if(arr[6]==arr[7]==arr[8])and(arr[6]!=0):
        print(arr[6]," has won")
        sys.exit()
else:
    print("It's a tie")
