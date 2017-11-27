myList = [10]
for i in range(10):
    myList.append(i)
k = 5
if len(myList)>2:
    seen=set()
    output=set()
    for num in myList:
        target=k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add( (min(num, target), max(num, target)) )
    print ('\n'.join( map(str, list(output)) ))
else:
    print ('invalid input')
