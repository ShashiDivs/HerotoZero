lis = [1,2,3]
lis1 = [4,5,6]

addlis = []
for i in range(len(lis)):
    addlis.append(lis[i]+lis1[i])
print(addlis)


liscom = [x+y for x,y in zip(lis,lis1)]
print(liscom)