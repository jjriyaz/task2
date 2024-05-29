def remove_vowels(input_str):
    vowels = "aeiouAEIOU"
    result = ""
    
    for char in input_str:
        # Check if the character is not a vowel
        if char not in vowels:
            result += char
    
    return result

input_string = input("Enter a string: ")
result_string = remove_vowels(input_string)
print("String with vowels removed:", result_string)
