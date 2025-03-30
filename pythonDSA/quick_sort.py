my_array = [ 11, 9, 12, 7, 3]
firstIndex = 0
lastIndex = len(my_array)-1

def quickSort(array, lastIndex, firstIndex):
    pivotIndex = lastIndex
    j = firstIndex - 1
    temp = None
    for i in range(firstIndex, lastIndex + 1):
        if array[i] < array[pivotIndex]:
            j = j + 1
            array[j], array[i] = array[i], array[j]

    array[j+1], array[pivotIndex] = array[pivotIndex], array[j+1]

    if ((j+1)-firstIndex) > 1:
        quickSort(array, lastIndex, firstIndex)
        lastIndex = j+1
    elif (lastIndex-(j+1)) > 1:
        quickSort(array, lastIndex, firstIndex)
        firstIndex = j+2
    
    print(array)

quickSort(my_array, firstIndex, lastIndex)