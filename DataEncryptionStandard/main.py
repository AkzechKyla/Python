M = "BEADCAFE0A459067"
K = "FADEDDECAF016692"

# Permuted choice 1 (PC-1)
permuted_choice_1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]


def hex_to_bin(hex_str):
    # Convert hex string to binary string
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)


def bin_to_4bit_blocks(bin_str):
    # Divide the binary string into 4-bit blocks
    return [bin_str[i : i + 4] for i in range(0, len(bin_str), 4)]


def permute_choice_1(bin_str):
    # Permute the binary string according to PC-1
    return "".join(bin_str[i - 1] for i in permuted_choice_1)

def left_shift(key_half, shifts):
    # Perform left shift on the key half
    return key_half[shifts:] + key_half[:shifts]


print("Input Values:")
print("M = ", M)
print("K = ", K)
print()

print("Initial Step: Convert K (hexadecimal) to binary")
K_bin = hex_to_bin(K)
K_blocks = bin_to_4bit_blocks(K_bin)
print("K = ", K_bin)
print(K_blocks)
print()

print("Step 1: Permute the 64-bit key (K_bin) into a 56-bit key using PC-1")
pc1_key = permute_choice_1(K_bin)
print("K += ", pc1_key)

print("Step 2: Split the 56-bit key into two 28-bit halves, C0 and D0")
c0 = pc1_key[:28]
d0 = pc1_key[28:]
print("C0 = ", c0)
print("D0 = ", d0)

print("Step 3: Create 16 block Cn and Dn (1<=n<=16) using left shift")

for i in range(1, 17):
    shift = 1 if i in [1, 2, 9, 16] else 2
    c0 = left_shift(c0, shift)
    d0 = left_shift(d0, shift)
    print("C{} = ".format(i), c0)
    print("D{} = ".format(i), d0)
    print()
