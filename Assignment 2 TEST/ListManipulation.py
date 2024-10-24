myList = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

myList.sort()

while 1 in myList:
    myList.remove(1)

myList.extend([7,8])

print(myList)
