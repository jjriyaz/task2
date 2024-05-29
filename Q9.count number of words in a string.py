def count_words(string):

    # Split the string by spaces to get a list of words
    words = string.split()

    # Return the length of the list, which represents the number of words
    return len(words)

string = input("enter the string:")
print(count_words(string))
