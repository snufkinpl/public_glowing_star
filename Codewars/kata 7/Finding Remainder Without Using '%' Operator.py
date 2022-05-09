def remainder(dividend, divisor):
    # your code here; you can use % but your are lame if you do ;)
    result_temp = int(dividend / divisor)
    result_temp = result_temp * divisor
    return dividend - result_temp


# few tests below:
print(remainder(3, 2))
print(remainder(19, 2))
print(remainder(10, 2))
print(remainder(34, 7))
print(remainder(27, 5))
