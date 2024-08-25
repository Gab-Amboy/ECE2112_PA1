# Declares a list for the inputs of the user.
writeyourcodehere = []

# Get the number of elements for the list.
list_n = int(input("How many numbers to unpack? "))

# Loops to populate the list by how many elements the user specified.
for i in range(list_n):
    num = int(input("Number " + str(i+1) + ": "))
    writeyourcodehere.append(num)

# Prints the list specified by the user.
print("List:", writeyourcodehere)

# Prints the first, middle and last number of the list using the corresponding indexes.
print("First:", writeyourcodehere[0], 
      "\tMiddle:", writeyourcodehere[1:-1], 
      "\t\tLast:", writeyourcodehere[-1])

