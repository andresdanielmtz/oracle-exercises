"""
La tercera era algo como, crea un stack de empleados que ocupan ayuda y stack de empleados que ayudan a otros, printea como cola la persona q ocupa ayuda + la persona q le va a ayudar 
"""

# will use nums and char for improved visibility
need_help = [1, 2, 3, 4, 5, 6]
offer_help = ["a", "b", "c", "d", "e", "f"]


def return_pairs(need_help, offer_help) -> None:
    res = []
    for _ in range(0, len(min(need_help, offer_help, key=len))):
        res.append([need_help.pop(), offer_help.pop()])
    return res
result = return_pairs(need_help=need_help, offer_help=offer_help)
print(f"Result: {result}")