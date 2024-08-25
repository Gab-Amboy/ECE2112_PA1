# Defines a function "alphabet_soup" to alphabetically arrange the characters of a string.
def alphabet_soup(string):

    # Sorts the string as a list and turns all the characters into lowercase.
    string = sorted(string.lower())

    # Declares the result as a string.
    result = ""

    # Returns the sorted list back into a string.
    return result.join(string)

# User-input for the string.
string = input("String:")

# Output of the sorting function.
print(f"Sorted string: {alphabet_soup(string)}")
