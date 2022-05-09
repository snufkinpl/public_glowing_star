def remainder(a, b):
    if a > b:
        if b == 0:
            return None
        else:
            result = a % b
    else:
        if a == 0:
            return None
        result = b % a
    return result


print(remainder(17, 5))
print(remainder(13, 72))
print(remainder(72, 13))
print(remainder(1, 0))
print(remainder(0, 0))
print(remainder(0, 1))
print(remainder(-1, 0))
print(remainder(0, -1))
print(remainder(-13, -13))
print(remainder(-60, 340))
print(remainder(60, -40))
