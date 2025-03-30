my_array = [1, 2, 3, 4, 5]

lngth = len(my_array) - 1
index = 0

for outerIndex in range(lngth):
    isSwapped = False
    for innerIndex in range(lngth-index):
        if my_array[innerIndex] > my_array[innerIndex+1]:
            tempVal = my_array[innerIndex]
            my_array[innerIndex] = my_array[innerIndex+1]
            my_array[innerIndex+1] = tempVal
            isSwapped = True
        print(my_array)
    if (isSwapped != True):
        break
    index = index + 1