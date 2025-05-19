M = "BEADCAFE0A459067"
K = "FADEDDECAF016692"

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

permuted_choice_2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]

initial_perm = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
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


def permute_choice_2(bin_str):
    # Permute the binary string according to PC-2
    return "".join(bin_str[i - 1] for i in permuted_choice_2)


def initial_permutation(bin_str):
    # Perform the initial permutation according to the initial permutation table
    return "".join(bin_str[i - 1] for i in initial_perm)


def left_shift(key_half, shifts):
    # Perform left shift on the key half
    return key_half[shifts:] + key_half[:shifts]


def generate_subkeys(c0, d0):
    c_list = []
    d_list = []

    for i in range(1, 17):
        shift = 1 if i in [1, 2, 9, 16] else 2
        c0 = left_shift(c0, shift)
        d0 = left_shift(d0, shift)

        # Print for visualization
        print("C{} = {}".format(i, c0))
        print("D{} = {}".format(i, d0))
        print()

        c_list.append(c0)
        d_list.append(d0)

    return c_list, d_list


def combine_c_d(c_list, d_list):
    subkey_list = []
    for i in range(16):
        c = c_list[i]
        d = d_list[i]
        cd = c + d

        subkey_list.append(cd)

    return subkey_list


print("Input Values:")
print("M = ", M)
print("K = ", K)
print()

print("Initial Step: Convert K (hexadecimal) to binary")
K_bin = hex_to_bin(K)
K_blocks = bin_to_4bit_blocks(K_bin)
print("K = ", K_bin)
print(K_blocks)

print("\nStep 1: Permute the 64-bit key (K_bin) into a 56-bit key using PC-1")
pc1_key = permute_choice_1(K_bin)
print("K += ", pc1_key)

print("\nStep 2: Split the 56-bit key into two 28-bit halves, C0 and D0")
c0 = pc1_key[:28]
d0 = pc1_key[28:]
print("C0 = ", c0)
print("D0 = ", d0)

print("\nStep 3: Create 16 block Cn and Dn (1<=n<=16) using left shift")
c_list, d_list = generate_subkeys(c0, d0)

print("\nStep 4: Combine Cn and Dn, then permute the 56-bit key into a 48-bit key using PC-2")
combined_keys = combine_c_d(c_list, d_list)
for i in range(len(combined_keys)):
    print("C{}D{} = {}".format(i + 1, i + 1, combined_keys[i]))

final_keys = []
print("\nFinal Keys:")
for i in range(len(combined_keys)):
    key = permute_choice_2(combined_keys[i])
    final_keys.append(key)
    print("K{} = {}".format(i + 1, key))

print("\nSecond Step: Encode each 64-bit block of data")

print("\nStep 1: Convert message M (hexadecimal) to binary")
M_bin = hex_to_bin(M)
print("M =", M_bin)

print("\nStep 2: Permute the 64-bit message (M_bin) into a 64-bit message using IP")
ip = initial_permutation(M_bin)
print("IP =", ip)

print("\nStep 3: Split the 64-bit message into two 32-bit halves, L0 and R0")
l0 = ip[:32]
r0 = ip[32:]
print("L0 =", l0)
print("R0 =", r0)
