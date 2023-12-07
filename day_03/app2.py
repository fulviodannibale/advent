result_map = []
sum = 0
gear_map = {}
with open("input.txt", 'r') as file:
    for line in file:
        # Use a list comprehension to create a list of characters for each line
        line_chars = [char for char in line.strip()]
        result_map.append(line_chars)


def populate_gear_map(rowIndex, charIndex, num):
    coordinated_tuple = (rowIndex, charIndex)
    if coordinated_tuple not in gear_map:
        gear_map[coordinated_tuple] = {"count": 1}
        gear_map[coordinated_tuple]["value"] = num
    else:
        gear_map[coordinated_tuple]["count"] += 1
        gear_map[coordinated_tuple]["value"] *= num
def check_up(rowIndex, charIndex, numLen, num):
    for i in range(numLen + 1):
        item = result_map[rowIndex - 1][charIndex + i]
        if item == '*':
            populate_gear_map(rowIndex - 1, charIndex + i, num)
            return True
    return False

def check_left(rowIndex, charIndex, numLen, num):
    item = result_map[rowIndex][charIndex]
    if item == '*':
        populate_gear_map(rowIndex, charIndex, num)
        return True
    else:
        return False

def check_down(rowIndex, charIndex, numLen, num):
    for i in range(numLen + 1):
        item = result_map[rowIndex + 1][charIndex + i]
        if item == '*':
            populate_gear_map(rowIndex + 1, charIndex + i, num)
            return True
    return False

def check_right(rowIndex, charIndex, numLen, num):
    item = result_map[rowIndex][charIndex + numLen]
    if item == '*':
        populate_gear_map(rowIndex, charIndex + numLen, num)
        return True
    else:
        return False


def check_surrounding(rowIndex, charIndex, numLen, num):
    #topleft
    if rowIndex == 0 and charIndex == 0:
        return (check_down(rowIndex, charIndex, numLen, num) or
                check_right(rowIndex, charIndex, numLen, num))
    #topright
    if rowIndex == 0 and charIndex == len(result_map[0]) - 1:
        return (check_down(rowIndex, charIndex, numLen, num) or
                check_left(rowIndex, charIndex, numLen, num))
    #bottomleft
    if rowIndex == len(result_map) and charIndex == 0:
        return (check_up(rowIndex, charIndex, numLen, num) or
                check_right(rowIndex, charIndex, numLen, num))
    #bottomright
    if rowIndex == len(result_map) and charIndex == len(result_map[0]) - 1:
        return (check_up(rowIndex, charIndex, numLen, num) or
                check_left(rowIndex, charIndex, numLen, num))
    if rowIndex == 0:
        return (check_down(rowIndex, charIndex, numLen+1, num) or
                check_left(rowIndex, charIndex, numLen, num) or
                check_right(rowIndex, charIndex, numLen, num))
    if rowIndex == len(result_map) - 1:
        return (check_up(rowIndex, charIndex, numLen+1, num) or
                check_left(rowIndex, charIndex, numLen, num) or
                check_right(rowIndex, charIndex, numLen, num))
    if charIndex == 0:
        return (check_up(rowIndex, charIndex, numLen, num) or
                check_down(rowIndex, charIndex, numLen+1, num) or
                check_right(rowIndex, charIndex, numLen, num))
    if charIndex + numLen == len(result_map[0]) - 1:
        return (check_up(rowIndex, charIndex, numLen, num) or
                check_down(rowIndex, charIndex, numLen, num) or
                check_left(rowIndex, charIndex, numLen, num))

    return (check_up(rowIndex, charIndex, numLen+1, num) or
            check_down(rowIndex, charIndex, numLen+1, num) or
            check_left(rowIndex, charIndex, numLen, num) or
            check_right(rowIndex, charIndex, numLen+1, num))

for rowIndex in range(len(result_map)):
    num = 0
    count_decimal=0
    for charIndex in range(len(result_map[rowIndex])-1, -1, -1):
        item = result_map[rowIndex][charIndex]
        if item.isdigit():
            num = num + int(item) * (10 ** count_decimal)
            count_decimal += 1
            if charIndex == 0:
                check_surrounding(rowIndex, charIndex, count_decimal, num)
                num = 0
                count_decimal = 0

        else:
            if num != 0:
                check_surrounding(rowIndex, charIndex, count_decimal, num)
                num = 0
                count_decimal = 0
            else:
                continue

for k,v in gear_map.items():
    if v["count"] == 2:
        sum += v["value"]
    print(k,v)

print(sum)



