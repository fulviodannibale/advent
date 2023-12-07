file_path = 'input.txt'
sum=0
with open(file_path, 'r') as file:
    for line in file:
        calibration_number=[]
        for i in range(len(line)):
            if line[i].isdigit():
                calibration_number.append(int(line[i]))
                break

        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                calibration_number.append(int(line[i]))
                break

        sum += calibration_number[0]*10 + calibration_number[1]
print(sum)




