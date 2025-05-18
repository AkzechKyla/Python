M = "BEADCAFE0A459067"
K = "FADEDDECAF016692"


def hex_to_bin(hex_str):
    # Convert hex string to binary string
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)


def bin_to_4bit_blocks(bin_str):
    # Divide the binary string into 4-bit blocks
    return [bin_str[i : i + 4] for i in range(0, len(bin_str), 4)]


# Initial Step: Convert K (hexadecimal) to binary
K_bin = hex_to_bin(K)
K_blocks = bin_to_4bit_blocks(K_bin)

print(K_bin)
print(K_blocks)
