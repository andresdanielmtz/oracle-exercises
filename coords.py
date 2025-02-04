"""
Suppose you have various coordinates of rectangles
Tell me which point is the one missing. 
"""

""" This isn't the best overall approach. """

coords = [[0, 0], [0, 2], [2, 0]]  # [2, 2] is the one missing
# x: 2 is the only one with three instances (so impir)

def missing_coord(lst: list[int]) -> list[int]:
    if not lst:
        return

    x = [coord[0] for coord in lst]
    y = [coord[1] for coord in lst]

    x_result = next(elem for elem in x if x.count(elem) % 2 == 1) 
    y_result = next(elem for elem in y if y.count(elem) % 2 == 1)

    print([x_result, y_result])


missing_coord(coords)
