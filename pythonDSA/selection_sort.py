my_array = [64, 34, 25, 12, 22, 11, 90, 5]

for outerRound in range(len(my_array)-1):
    lowestVal = my_array[outerRound]
    lowestValIndex = outerRound
    for index in range(outerRound, len(my_array)):
        if my_array[index] < lowestVal:
            lowestVal = my_array[index]
            lowestValIndex = index
    my_array[outerRound], my_array[lowestValIndex] = my_array[lowestValIndex], my_array[outerRound] 

print(my_array)   