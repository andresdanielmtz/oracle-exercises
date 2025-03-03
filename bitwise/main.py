num = 100
binary_num = bin(num)

print(f"Binary: {binary_num}")
for i in range(0, len(binary_num) - 2):
    print(f"bit: \t {(num >> i) & 1}")
    