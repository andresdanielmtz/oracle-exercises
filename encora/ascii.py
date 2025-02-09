"""
A mi me salió uno donde tenías que sacar los valores ascii de un string por caracter, agarrar los dos mayores y los dos menores y sumarlos
"""

string = "abcd"


def lowestAndHighestASCIIPair(string: str) -> int:
    if len(string) < 4:
        return -1

    vals = [ord(ch) for ch in string]
    vals.sort()

    return sum(vals[0:2]) + sum(vals[2:])

res = lowestAndHighestASCIIPair(string)
print(f"[Result]: {res}")

# There must be another thing to this. 