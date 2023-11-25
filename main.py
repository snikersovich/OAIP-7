#Линейный поиск
def LinearSearch(lys, element):
    for i in range (len(lys)):
        if lys[i] == element:
            return i
    return -1
    print(LinearSearch([1,2,3,4,5,2,1]

#Бинарный поиск
def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index
    BinarySearch([10,20,30,40,50]
                 
#Экспонециальный поиск
def ExponentialSearch(lys, val):
    if lys[0] == val:
        return 0
    index = 1
    while index < len(lys) and lys[index] <= val:
        index = index * 2
    return BinarySearch( lys[:min(index, len(lys))], val)
    print(ExponentialSearch([1,2,3,4,5,6,7,8],3))

