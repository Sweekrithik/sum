def remove_duplicates(input_string):
    # Create an empty list to store unique characters
    unique_chars = []
    # Loop through the input string
    for char in input_string:
        # If the character is not already in the list, add it
        if char not in unique_chars:
            unique_chars.append(char)
    # Join the unique characters together into a string and return it
    return ''.join(unique_chars)

# Example usage
input_string = "hello world"
output_string = remove_duplicates(input_string)
print(output_string)