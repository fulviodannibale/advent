file_path = 'input.txt'
sum=0
def parse_line(line):
    card_parts = line.split(':')

    numbers = card_parts[1].split('|')
    
    winning_numbers = [int(num) for num in numbers[0].split()]
    my_numbers = [int(num) for num in numbers[1].split()]

    return winning_numbers, my_numbers

with open(file_path, 'r') as file:
    for line in file:
        count_occurences = 0
        winning_numbers, my_numbers = parse_line(line)
        for num in my_numbers:
            if num in winning_numbers:
                count_occurences += 1

        if(count_occurences > 0):
            sum += 2 ** (count_occurences-1)


print(sum)




