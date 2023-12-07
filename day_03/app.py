result_map = []
total_sum = 0

with open("input.txt", 'r') as file:
    for line in file:
        line_chars = list(line.strip())
        result_map.append(line_chars)

symbols = "#$%&'()*+,-/:;<=>?@[\]^_`{|}~"

def is_symbol(item):
    return item in symbols

def check_up(row_index, char_index, num_len):
    for i in range(num_len + 1):
        item = result_map[row_index - 1][char_index + i]
        if is_symbol(item):
            return True
    return False

def check_left(row_index, char_index, num_len):
    item = result_map[row_index][char_index]
    return is_symbol(item)

def check_down(row_index, char_index, num_len):
    for i in range(num_len + 1):
        item = result_map[row_index + 1][char_index + i]
        if is_symbol(item):
            return True
    return False

def check_right(row_index, char_index, num_len):
    item = result_map[row_index][char_index + num_len]
    return is_symbol(item)

def check_surrounding(row_index, char_index, num_len):
    if row_index == 0 and char_index == 0:
        return check_down(row_index, char_index, num_len) or check_right(row_index, char_index, num_len)
    if row_index == 0 and char_index == len(result_map[0]) - 1:
        return check_down(row_index, char_index, num_len) or check_left(row_index, char_index, num_len)
    if row_index == len(result_map) - 1 and char_index == 0:
        return check_up(row_index, char_index, num_len) or check_right(row_index, char_index, num_len)
    if row_index == len(result_map) - 1 and char_index == len(result_map[0]) - 1:
        return check_up(row_index, char_index, num_len) or check_left(row_index, char_index, num_len)
    if row_index == 0:
        return check_down(row_index, char_index, num_len+1) or check_left(row_index, char_index, num_len) or check_right(row_index, char_index, num_len)
    if row_index == len(result_map) - 1:
        return check_up(row_index, char_index, num_len+1) or check_left(row_index, char_index, num_len) or check_right(row_index, char_index, num_len)
    if char_index == 0:
        return check_up(row_index, char_index, num_len) or check_down(row_index, char_index, num_len+1) or check_right(row_index, char_index, num_len)
    if char_index + num_len == len(result_map[0]) - 1:
        return check_up(row_index, char_index, num_len) or check_down(row_index, char_index, num_len) or check_left(row_index, char_index, num_len)

    return check_up(row_index, char_index, num_len+1) or check_down(row_index, char_index, num_len+1) or check_left(row_index, char_index, num_len) or check_right(row_index, char_index, num_len+1)

for row_index in range(len(result_map)):
    num = 0
    count_decimal = 0
    for char_index in range(len(result_map[row_index])-1, -1, -1):
        item = result_map[row_index][char_index]
        if item.isdigit():
            num = num + int(item) * (10 ** count_decimal)
            count_decimal += 1
            if char_index == 0:
                if check_surrounding(row_index, char_index, count_decimal):
                    total_sum += num
                    print(f"item: {num}")
                num = 0
                count_decimal = 0
        else:
            if num != 0:
                if check_surrounding(row_index, char_index, count_decimal):
                    total_sum += num
                    print(f"item: {num}")
                num = 0
                count_decimal = 0

print(total_sum)
