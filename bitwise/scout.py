num = 5  # 101

result = 0
string_result = "" 
while num > 0:
    print(f"Numero: \t {num % 2}")
    result += num % 2  # num % 2 can be either 1 or 0
    string_result += str(num%2)
    num //= 2  # floor division

print(result)
print(string_result)
