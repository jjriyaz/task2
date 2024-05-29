#check the string is palindrome or not

def is_palindrome(input_str):
    # Convert the input string to lowercase and remove non-alphanumeric characters
    input_str = ''.join(char.lower() for char in input_str if char.isalnum())
    
    # Check if the string is equal to its reverse
    return input_str == input_str[::-1]

# Example usage
input_string = input("Enter a string: ")
result = is_palindrome(input_string)

if result:
    print("yes,The string is a palindrome.")
else:
    print("The string is not a palindrome.")
