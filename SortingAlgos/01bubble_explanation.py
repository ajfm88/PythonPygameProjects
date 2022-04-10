from random import randint

unsorted = input("Enter a comma-separated list of numbers to sort:\n").split(",")

# split into separate lists
numbers = [eval(i) for i in unsorted]

# how many numbers in the list?
nums = len(numbers)

print("\nOriginal list:")
print(numbers)

# records whether a swap has taken place (this needs to be set
# to True to ensure that the loops executes the first time)
swap = True

while swap == True:
    swap = False # assume no swap unless we actual do one

    for n in range(nums-1):
        # are the two adjacent items the wrong way round?
        if numbers[n] > numbers[n+1]:
            print("\nSwap",numbers[n], "and", str(numbers[n+1])+":")

            # swap the two values (in Python a, b = b, a swaps a and b)
            numbers[n], numbers[n+1] = numbers[n+1], numbers[n]

            # record that a swap has taken place
            swap = True
            print(numbers)

# output the sorted list
print("\nSorted list:")
print(numbers)