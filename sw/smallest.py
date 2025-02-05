"""
Smallest Substring that contains all characters
"""

from sw import get_all_substrings


def get_all_unique_characters(word: str) -> str:
    res = ""
    for char in word:
        if char not in res:
            res += char
    return "".join(sorted(res))  # return all unique characters as string


example = "career"
example_sub = get_all_substrings(example)
print(example_sub)
example_unique = get_all_unique_characters(example)

for elem in example_sub:
    if ''.join(sorted((elem))) == example_unique:
        print(f"The smallest substring is: \t {elem}")
