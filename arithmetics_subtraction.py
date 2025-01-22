def get_sign(hex_num, width):
    # Convert hex to integer
    num = hex_num

    # Check MSB (sign bit)
    sign_bit = (num >> (width - 1)) & 1  # Extract the MSB
    if sign_bit == 0:
        return "Positive"
    else:
        return "Negative"


def calculate_flags(result, num1, num2, width):
    # Mask result to fit the width (4-bit, 8-bit, or 16-bit)
    result &= (1 << width) - 1

    # Borrow flag (B): Set if a borrow occurs (i.e., when num1 < num2).
    borrow = 0
    if num1 < num2:
        borrow = 1

    # Carry flag (C): In subtraction, it's set when no borrow occurs, i.e., when result >= 0.
    carry = 1 if borrow == 0 else 0

    # Zero flag (Z): Set if the result is zero.
    zero = 1 if result == 0 else 0

    # Sign flag (S): Set if the result is negative (most significant bit is 1).
    sign = 1 if (result & (1 << (width - 1))) else 0

    # Overflow flag (O): Set if there was an overflow, i.e., if the sign bit was incorrect.
    overflow = 0
    #if ((result < 0 and sign == 0) or (result >= (1 << (width - 1)) and sign == 1)):
    #    overflow = 1
    if (get_sign(num1, width) == "Positive" and get_sign(num2, width) == "Negative" and sign == 1) or (get_sign(num1, width) == "Negative" and get_sign(num2, width) == "Positive" and sign == 0):
        overflow = 1

    # Parity flag (P): Set if the number of set bits is even.
    parity = bin(result).count('1') % 2 == 0

    return {
        'result': result,
        'borrow': borrow,
        'carry': carry,
        'zero': zero,
        'sign': sign,
        'overflow': overflow,
        'parity': parity
    }


def subtract_hex(hex1, hex2, width):
    # Convert hex to integers
    num1 = int(hex1, 16)
    num2 = int(hex2, 16)

    # Perform the subtraction
    result = num1 - num2

    # Calculate the flags for the given width
    flags = calculate_flags(result, num1, num2, width)

    return flags


# Example Usage:
hex1 = "A3"  # Example hex value 1
hex2 = "62"  # Example hex value 2

# Perform subtraction and calculate flags for 4-bit, 8-bit, and 16-bit widths
#for width in [4, 8, 16]:
for width in [8]:
    flags = subtract_hex(hex1, hex2, width)
    print(f"Flags for {hex1} - {hex2} in {width}-bit arithmetic:")
    print(f"Result: {hex(flags['result'])}")
    print(f"Borrow: {flags['borrow']}")
    print(f"Carry: {flags['carry']}")
    print(f"Zero: {flags['zero']}")
    print(f"Sign: {flags['sign']}")
    print(f"Overflow: {flags['overflow']}")
    print(f"Parity: {flags['parity']}")
    print("-" * 40)


