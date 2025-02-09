"""
El primero era el clásico de convertir en ASCII los lowercased chars de un string, pero el plotwist es tomar los dos valores mas pequeños + los dos valores más grandes y outputear la suma.
"""

string = "ABCDEFGHIJKLMNOP"


def highest_lowest_ascii(string) -> int:
    highest = float("-inf")
    second_highest = float("-inf")
    lowest = float("inf")
    second_lowest = float("inf")

    for char in string:
        val = ord(char)
        print(val)
        if val < lowest:
            lowest = val
        if val > lowest and val < second_lowest:
            second_lowest = val
        if val > highest:
            second_highest = highest
            highest = val
        if val < highest and val > second_highest:
            second_highest = val

    print("results")
    print(highest)
    print(second_highest)
    print(lowest)
    print(second_lowest)
    return highest + second_highest + lowest + second_lowest


res = highest_lowest_ascii(string)
print(f"Result: {res}")
