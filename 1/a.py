import re

sum = 0

with open('./input.txt', 'r') as file:
    for line in file:
        numeric_string = re.sub(r'[^0-9]', '', line)
        num = numeric_string[0] + numeric_string[-1]
        sum += int(num)
# Use regular expression to remove non-numeric characters


# Print the result
print(sum)

if __name__ == "__main__":
    print("Hello, world!")