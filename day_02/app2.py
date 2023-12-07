file_path = 'input.txt'
sum = 0

with open(file_path, 'r') as file:
    for line in file:
        id_str, games_str = line.split(':')
        identifier = int(id_str.split()[1])
        games = games_str.split(';')

        color_counts = {'blue': 0, 'green': 0, 'red': 0}
        for game in games:

            items = [item.strip().split() for item in game.strip().split(',')]
            for count_str, color in items:
                count = int(count_str)
                if(count > color_counts[color]):
                    color_counts[color] = count

        power = color_counts['red'] * color_counts['green'] * color_counts['blue']
        print(power)
        sum += power



print(sum)
