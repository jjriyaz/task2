def longest_common_substring(str1, str2):
    # Initialize variables to store the length and ending index of the longest common substring
    max_length = 0
    end_index = 0
    
    # Initialize a 2D table to store the lengths of common substrings
    table = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    
    # Fill the table with the lengths of common substrings
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > max_length:
                    max_length = table[i][j]
                    end_index = i
            else:
                table[i][j] = 0
    
    # Return the longest common substring
    return str1[end_index - max_length:end_index]

# Example usage
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
result = longest_common_substring(string1, string2)
print("Longest common substring:", result)
