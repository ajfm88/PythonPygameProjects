# numbers to be sorted (try changing them!)
numbers = [6,5.5,4,0,7,-5,3,2,5.3,1]

comparisons = 0
swaps = 0
print("Original:",numbers)

# use a to count for first to penultimate value
for a in range(len(numbers)-1):

    # use b to count from value after a to end of list
    for b in range(a+1,len(numbers)):

        # if left value is greater than right value...
        comparisons += 1

        if numbers[a] > numbers[b]:
            # ...swap them around
            numbers[a], numbers[b] = numbers[b], numbers[a]
            swaps += 1
            
# print the sorted list
print("Sorted:",numbers)
print("Sorting required",comparisons,"comparisons and",swaps,"swaps.")