def count_unique_characters(input_str):
    unique_chars = set(input_str)
    return len(unique_chars)
input_string = input("Enter a string: ")
unique_count = count_unique_characters(input_string)
print("Number of unique characters:", unique_count)
