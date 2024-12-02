data_left = []
data_right = []

for row in open('data_1.txt').readlines():
    parts = row.split('   ')
    data_left.append(int(parts[0].strip()))
    data_right.append(int(parts[1].strip()))


data_left.sort()
data_right.sort()

total_distance = 0
for i in range(len(data_left)):
    total_distance += abs(data_left[i] - data_right[i])

print(total_distance)


