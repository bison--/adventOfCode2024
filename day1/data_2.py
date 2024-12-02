data_left = []
data_right = []

for row in open('data_2.txt').readlines():
    parts = row.split('   ')
    data_left.append(int(parts[0].strip()))
    data_right.append(int(parts[1].strip()))


data_left.sort()
data_right.sort()

total_distance = 0
for number_left in data_left:
    found_amount = 0
    for number_right in data_right:
        if number_left == number_right:
            found_amount += 1

    total_distance += number_left * found_amount

print(total_distance)


