import re

# file_name = "data_1_example.txt"
file_name = "data_1.txt"

data = open(file_name).readlines()

find_multiplications_regex = re.compile(r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)")

found_groups = []
for row in data:
    found_groups.extend(find_multiplications_regex.findall(row))

total = 0
for found_group in found_groups:
    result = int(found_group[0]) * int(found_group[1])
    total += result

print(total)
