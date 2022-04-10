def selection_sort(array):
    # Traverse through all array elements
    for i in range(len(array)):
        
        # Find the minimum element in remaining 
        # unsorted array
        lowest__number_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[lowest__number_index]:
                lowest__number_index = j
                
        # Swap the found minimum element with 
        # the first element        
        array[i], array[lowest__number_index] = array[lowest__number_index], array[i]

    return array

print(selection_sort([64, 25, 12, 22, 11]))