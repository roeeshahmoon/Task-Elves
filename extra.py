original_string = "9one1two4four7nine"

to_replace = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
              "six": "6", "seven": "7", "eight": "8", "nine": "9"}


new_string = original_string
for key, value in to_replace.items():
    new_string = new_string.replace(key, value)

print(original_string)
print(new_string)
