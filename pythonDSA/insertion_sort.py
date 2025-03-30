
my_array = [64, 34, 25, 12, 22, 11, 90, 5]

for start_index_of_unsorted_part in range(1, len(my_array)):
    value_from_unsorted_part = my_array[start_index_of_unsorted_part]
    for index_of_sorted_part in range(0, start_index_of_unsorted_part):
        if my_array[index_of_sorted_part] > value_from_unsorted_part:
            for index in range(start_index_of_unsorted_part,index_of_sorted_part, -1):
                my_array[index] = my_array[index-1]
            my_array[index_of_sorted_part] = value_from_unsorted_part
            break


print(my_array)
