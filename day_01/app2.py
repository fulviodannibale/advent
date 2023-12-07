file_path = 'input.txt'
sum=0
word_to_digit_mapping = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}

def replace_with_digits(input_string):
    for word, digit in word_to_digit_mapping.items():
        input_string = input_string.replace(word, digit)
    return input_string


with open(file_path, 'r') as file:
    for line in file:
        replaced_string = replace_with_digits(line)
        calibration_number=[]
        for i in range(len(replaced_string)):
            if replaced_string[i].isdigit():
                calibration_number.append(int(replaced_string[i]))
                break

        for i in range(len(replaced_string) - 1, -1, -1):
            if replaced_string[i].isdigit():
                calibration_number.append(int(replaced_string[i]))
                break

        sum += calibration_number[0]*10 + calibration_number[1]
print(sum)




