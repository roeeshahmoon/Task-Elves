
def extract_numbers(input_string):
    return ''.join(char for char in input_string if char.isdigit())

def sum_values_in_list(string_list):
    total_sum = 0
    for value in string_list:
            total_sum += int(value)
    return total_sum

def replace_text_to_nums(input_string):
    dict_replace = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
              "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    res_string = input_string
    for key, value in dict_replace.items():
        res_string = res_string.replace(key, value)
    return res_string

if __name__ == "__main__":
    with open('input_day_two.txt', 'r') as file:
        numbers_list = []
        two_digits_list = []
        # Read the entire content of the file
        content = file.readlines()
        print("this is start of mission day 2 by Roee Shahmoon")
        for line in content:
            newline = replace_text_to_nums(line)    

            #print("this is line:", line)
            #print("this is line after replace:", newline)
            #print("this is line after extract numbers:", extract_numbers(newline))
            #print("**********************************************************\n")

            numbers_list.append(extract_numbers(newline))
        #print(numbers_list)
        for str in numbers_list:
            if len(str) == 1:
                two_digits_list.append(str + str)
            else:
                two_digits_list.append(str[0] + str[-1])

    print(two_digits_list)

    result = sum_values_in_list(two_digits_list)
    print("the result day two is:" ,result)