save_value_change = 3


def all_increment(_values):
    last_value = -1
    for value in _values:
        # first item
        if last_value == -1:
            last_value = value
            continue

        if last_value == value:
            return False

        if last_value > value:
            return False

        last_value = value

    return True


def all_decrement(_values):
    last_value = -1
    for value in _values:
        # first item
        if last_value == -1:
            last_value = value
            continue

        if last_value == value:
            return False

        if last_value < value:
            return False

        last_value = value

    return True


def is_change_save(_values):
    for i in range(1, len(_values)):
        difference = abs(_values[i] - _values[i - 1])
        if difference > save_value_change:
            return False

    return True


amount_save_reports = 0

for row in open('data_1.txt').readlines():
    parts = row.split(' ')
    values = []
    for part in parts:
        values.append(int(part.strip()))

    if not all_increment(values) and not all_decrement(values):
        continue

    if is_change_save(values):
        #print(parts)
        amount_save_reports += 1

print("Save Reports:", amount_save_reports)
