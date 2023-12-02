
def extract_numbers(input_string):
    return ''.join(char for char in input_string if char.isdigit())

def sum_values_in_list(string_list):
    total_sum = 0
    for value in string_list:
            total_sum += int(value)
    return total_sum

with open('input.txt', 'r') as file:
    numbers_list = []
    two_digits_list = []
    # Read the entire content of the file
    content = file.readlines()
    print("this is start of mission day 1 by Roee Shahmoon")
    for line in content:
        #print(extract_numbers(line))
        numbers_list.append(extract_numbers(line))
    #print(numbers_list)
    for str in numbers_list:
        if len(str) == 1:
            two_digits_list.append(str + str)
        else:
            two_digits_list.append(str[0] + str[-1])

#print(two_digits_list)

result = sum_values_in_list(two_digits_list)
print("The Result Of Day One is:", result)