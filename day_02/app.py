file_path = 'input.txt'
sum_result = 0

with open(file_path, 'r') as file:
    for line in file:
        id_str, games_str = line.split(':')
        identifier = int(id_str.split()[1])
        games = games_str.split(';')

        red_flag = False
        for game in games:
            color_counts = {'blue': 0, 'green': 0, 'red': 0}

            items = [item.strip().split() for item in game.strip().split(',')]
            for count_str, color in items:
                count = int(count_str)
                color_counts[color] += count

            if color_counts['red'] > 12 or color_counts['green'] > 13 or color_counts['blue'] > 14:
                red_flag = True
                break

        if not red_flag:
            sum_result += identifier

print(sum_result)
