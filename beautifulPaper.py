def is_square(a, b):
    return a == b
  
def solve(a1, b1, a2, b2):
    sides = [a1, b1, a2, b2]
    sides.sort()

    if (a1 + a2 == b1 and a1 + a2 == b2) or (a1 + b2 == b1 and a1 + b2 == a2) or (b1 + a2 == a1 and b1 + a2 == b2) or (b1 + b2 == a1 and b1 + b2 == a2):
        return "Yes"
    else:
        return "No"
