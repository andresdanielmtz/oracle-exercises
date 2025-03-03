binary = "101"
iterator = len(binary) - 1
result = 0
while iterator >= 0:
    if binary[iterator] == "1":
        result += 2 ** iterator
    iterator -= 1
print(f"result: \t {result}")