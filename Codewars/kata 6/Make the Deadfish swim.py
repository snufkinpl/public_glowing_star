def parse(data):
    result_final = []
    result = 0
    data_list = data
    for char in data_list:
        if char == "i":
            result += 1
        elif char == "d":
            result -= 1
        elif char == "s":
            result *= result
        elif char == "o":
            result_final.append(result)
        else:
            continue
    return result_final


print(parse("ooo"))  # [0,0,0]
print(parse("ioioio"))  # [1,2,3]
print(parse("idoiido"))  # [0,1]
print(parse("isoisoiso"))  # [1,4,25]
print(parse("codewars"))  # [0]
