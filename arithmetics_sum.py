def sum_hex_numbers(hex1, hex2, bit_size):

    if bit_size not in (4, 8, 16, 32):
        raise ValueError("Bit size must be 4, 8, or 16 or 32.")

    # Convert hexadecimal strings to integers
    num1 = int(hex1, 16)
    num2 = int(hex2, 16)

    # Calculate maximum value and mask for the given bit size
    max_value = (1 << bit_size) - 1  # e.g., 0xF for 4-bit, 0xFF for 8-bit
    mask = max_value + 1

    # Perform the addition
    result = num1 + num2

    # Determine carry flag (if the result exceeds the bit size capacity)
    carry = result > max_value

    # Mask the result to fit within the bit size
    result = result & max_value

    # Determine overflow flag (if the sign bit is incorrectly carried over)
    sign_bit = 1 << (bit_size - 1)  # e.g., 0x8 for 4-bit, 0x80 for 8-bit
    overflow = ((num1 & sign_bit) == (num2 & sign_bit)) and ((result & sign_bit) != (num1 & sign_bit))
    # Determine zero flag (if the result is zero)
    zero = result == 0

    # Determine negative flag (if the sign bit of the result is set)
    negative = (result & sign_bit) != 0
    return {
        "result": f"{result:X}",  # Return result as a hexadecimal string
        "carry": carry,
        "overflow": overflow,
        "zero": zero,
        "negative": negative
    }

if __name__ == "__main__":
    hex1 = "6"
    hex2 = "7"
    bit_size = 4

    result = sum_hex_numbers(hex1, hex2, bit_size)
    print(f"Result: {result['result']}")
    print(f"Carry (C): {result['carry']}")
    print(f"Overflow (V): {result['overflow']}")
    print(f"Zero (Z): {result['zero']}")
    print(f"Negative (N): {result['negative']}")
    # False = clear, True = set
    # Overflow Flag: Overflow occurs when the sign bit is improperly carried, i.e., when both operands have the same sign but the result has a different sign.
