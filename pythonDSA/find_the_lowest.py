my_array = [7, 12, 9, 4, 11]

lowestNum = None

for index in range(len(my_array)-1):
    lowestNum = my_array[index]
    if my_array[index+1] < lowestNum:
        lowestNum = my_array[index+1]

print(lowestNum)