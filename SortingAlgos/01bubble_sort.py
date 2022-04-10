def bubble_sort(list):
    unsorted_until_index = len(list) - 1
    sorted = False

    while not sorted: #While True
        sorted = True
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
        
        unsorted_until_index -= 1

    return list

print(bubble_sort([5, 8, 3, 10, 2, 6, 13, 1, 20]))