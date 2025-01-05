def string_to_hex_with_spaces(input_string):

    hex_representation = input_string.encode('utf-8').hex()  # Convert to hex
    spaced_hex = ' '.join(hex_representation[i:i+2].upper() for i in range(0, len(hex_representation), 2))  # Add spaces
    return spaced_hex



input_string = "Hello World"
hex_output = string_to_hex_with_spaces(input_string)
print(f"Original String: {input_string}")
print(f"Hexadecimal Representation: {hex_output}")

