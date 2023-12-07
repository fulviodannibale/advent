file_path = 'input.txt'
sum=0
mul=1
with open(file_path, 'r') as file:
    times = [int(time) for time in next(file).split(':')[1].split()]
    distances = [ int(distance) for distance in next(file).split(':')[1].split()]

    for k in range(len(times)):
        for i in range(1, times[k], 1):
            if (times[k]-i) * i > distances[k]:
                sum += 1
        mul *= sum
        sum = 0

print(mul)






