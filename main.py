
def permutFunc(myList):
    if len(myList) == 0:
        return []
    if len(myList) == 1:
        return [myList]
    k = []
    for i in range(len(myList)):
        m = myList[i]
        res = myList[:i] + myList[i+1:]
        for p in permutFunc(res):
            k.append([m] + p)
    return k
def order(myList):
    result = []
    for a in myList:
        #print(a)
        a = list(a)

        for b in range(1, len(a)):
            #if statement to check if the box behind the current box will catch up.
            if a[b] > a[b-1]:
                a.pop(b-1)
                break

        result.append(a)
    return result
from itertools import permutations

x=6
myList = list(permutations(range(1, x + 1)))
#print(myList)
z=0
for x in range(0, x-1):
    #just run the function x-1 times.
    myList = order(myList)
z=0
for t in myList:
    z += (len(t))
z= z/(len(myList))
print(z)