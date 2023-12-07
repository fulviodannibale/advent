file_path = 'input.txt'
sum = 0
single_line = {}
lines = []

def parse_line(line):
    card_parts = line.split(':')

    single_line["id"] = card_parts[0].split()[1].strip()
    single_line["count"] = 1
    numbers = card_parts[1].split('|')

    winning_numbers = [int(num) for num in numbers[0].split()]
    my_numbers = [int(num) for num in numbers[1].split()]

    single_line["winning_numbers"] = winning_numbers
    single_line["my_numbers"] = my_numbers
    lines.append(single_line.copy())

with open(file_path, 'r') as file:

    for line in file:
        count_occurences = 0
        parse_line(line)
    for l in lines:
        count_occurences = 0
        for num in l["my_numbers"]:
            if num in l["winning_numbers"]:
                count_occurences += 1
        if (count_occurences > 0):
            for i in range(1, count_occurences + 1):
                if (int(l["id"]) - 1 + i < len(lines)):
                    lines[int(l["id"]) -1 + i]["count"] += 1 * int(lines[int(l["id"])-1]["count"])

    for l in lines:
        sum += int(l["count"])

print(sum)
