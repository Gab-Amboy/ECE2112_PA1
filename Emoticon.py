# Defines a function "emotify" that reads the user input word-by-word 
# and changes word instances of emoticons to symbol emoticons.
def emotify(phrase):
    
    # Declares a dictionary of words with its corresponding emoticon.
    emoticons = {"smile" : ":)", "grin" : ":D", "sad" : ":((","mad" : ">:("}
    
    # Split the phrase string into a list of words.
    words = phrase.split()

    # Loops through the phrase to convert word instances to emoticons.
    words = [emoticons.get(word.lower(), word) for word in words]

    # Appends the words and emoticons back into a string.
    return " ".join(words)

# User-input for the emotify function.
phrase = input("Enter phrase to emotify: ")

# Outputs the result of the emotify function.
print(f"Converted phrase: {emotify(phrase)}")
        