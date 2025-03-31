my_array = my_array = [7, 12, 9, 4, 11]
firstIndex = 0
lastIndex = len(my_array)-1

def quickSort(array, firstIndex, lastIndex):
    pivotIndex = lastIndex
    j = firstIndex - 1

    for i in range(firstIndex, lastIndex + 1):
        if array[i] < array[pivotIndex]:
            j = j + 1
            array[j], array[i] = array[i], array[j]

    array[j+1], array[pivotIndex] = array[pivotIndex], array[j+1]

    print(array)

    if ((j+1)-firstIndex) > 1:
        lastIndex = j
        quickSort(array, firstIndex, lastIndex)
    elif (lastIndex-(j+1)) > 1:
        firstIndex = j+2
        quickSort(array, firstIndex, lastIndex)
        
    

quickSort(my_array, firstIndex, lastIndex)