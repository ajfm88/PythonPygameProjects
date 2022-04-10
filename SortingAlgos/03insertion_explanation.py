# put input into a list of integers
number = [eval(i) for i in input("Enter a comma-separated list of numbers to sort:\n").split(",")]
print("\nSorting list:",number,"\n")

# loop through the list forward
for pos in range(1,len(number)):
    if number[pos] < number[pos - 1]:

        # insert is the insertion point
        insert = pos - 1

        # value is the number we're trying to place
        value = number.pop(pos)

        # loop back until we find a number smaller than the one we're looking to place
        while insert >= 0 and number[insert] > value:
            insert -= 1

        # insert it after that one
        insert += 1
        print("The",value,"is out of place... insert before the",str(number[insert])+":")
        number.insert(insert, value)
        print(number,"\n")

# print the sorted list
print("Sorted list:",number)