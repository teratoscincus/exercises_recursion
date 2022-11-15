def rock_judger(rocks):
    if len(rocks) <= 2:
        a = rocks[0]
        b = rocks[-1]
    else:
        # Split in half.
        last_index = int(len(rocks) - 1)
        mid_index = int(last_index / 2)
        a_half = rocks[:mid_index]
        b_half = rocks[mid_index:last_index]

        # Pass on two half.
        a = rock_judger(a_half)
        b = rock_judger(b_half)

    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a


def fam_tree(tree):
    if len(tree) == 0:
        return
    for child in tree["children"]:
        print(child["name"])
        fam_tree(child)


def fact(n):
    if n == 1:
        # Base case
        return n
    else:
        # Recursive case
        return n * fact(n - 1)


if __name__ == "__main__":
    # from random import randint
    # rocks = [randint(1, 100) for _ in range(20)]

    # largest_rock = rock_judger(rocks)
    # print("Largest rock is size:", largest_rock)

    # fmt: off
    tree = {
        "name": "John", 
        "children": [
            {
                "name": "Jim", 
                "children": []
            },
            {
                "name": "Zoe",
                "children": [
                    {"name": "Kyle", "children": []},
                    {"name": "Sophia", "children": []}
                ]
            }
        ]
    }

    # fam_tree(tree)
    # fmt: on

    a = fact(4)
    print(a)
