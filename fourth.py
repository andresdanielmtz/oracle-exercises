num = 22
binary_string = ""

while num > 0:
    binary_string = str(num % 2) + binary_string
    num //= 2
print(f"result: {binary_string}")
print(f"result: {binary_string[-4]}")
