##find the word is anagram or not

def is_anagram(str1, str2):
    # Removing spaces and converting to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Checking if lengths are equal
    if len(str1) != len(str2):
        return False
    
    # Sorting both strings and comparing
    return sorted(str1) == sorted(str2)

string1 = input("enter the str1:")
string2 = input("enter the str2:")

print(is_anagram(string1, string2))
