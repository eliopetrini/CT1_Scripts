
#hex_value = "0xFF12"
#signed = False



# Wenn es sich um eine negative Zahl handelt (MSB = 1), muss vor der Umwandlung in Dezimal in das Zweierkomplement umgewandelt werden

def hex_to_decimal(hex_value, signed: bool = True) -> int:
    # Remove the "0x" prefix if present
    if hex_value.startswith("0x"):
        hex_value = hex_value[2:]

    # Convert the hex string into bytes
    byte_array = bytes.fromhex(hex_value)

    # Convert the bytes to an integer
    int_value = int.from_bytes(byte_array, signed=signed)

    return int_value


#print(hex_to_decimal(hex_value, signed))




print(hex_to_decimal("0xF6", signed=False))
#print(hex_to_decimal("0x7FA2", signed=False))

11110110