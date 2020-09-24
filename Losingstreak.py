def processArray(l2):
  loss=[];mloss=0
  for i in range(0,len(l2)):
       loss.append(l2[i][0]-l2[i][len(l2[i])-1])
  if(len(loss)>0):
    mloss=loss.index(max(loss))
  print(len(l2[mloss]))
l=[]
while True:
    a=int(input())
    if(a<0):
        break
    l.append(a)
ans=[]
i=0
while(i<len(l)):
    k=l[i]
    tmp=[]
    tmp.append(l[i])
    for j in range(i+1,len(l)):
        if(l[j]>k):
            break
        else:
            tmp.append(l[j])
            k=l[j]
    i=j+1
    print(tmp)
    if(len(tmp)>1):
      ans.append(tmp)
processArray(ans)
