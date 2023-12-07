file_path = 'input.txt'
sum=0
with open(file_path, 'r') as file:
    time = int(next(file).split(':')[1].replace(" ", ""))
    distance = int(next(file).split(':')[1].replace(" ", ""))
    for i in range(1, time, 1):
        if (time-i) * i > distance:
            sum += 1
print(sum)






