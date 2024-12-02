from uu import decode

save_value_change = 3


def remove_bad_increment(_values):
    fixed_counter = 0
    new_values = []
    for value in _values:
        new_values.append(value)
        if len(new_values) == 0:
            continue

def get_value_stats(_values):
    increments = 0
    decrements = 0
    equals = 0
    too_steep = 0

    value_categories = []

    last_value = -1
    for value in _values:
        # first item
        if last_value == -1:
            last_value = value
            continue

        number_information = {
            'value': value,
            'category': '',
            'too_steep': False
        }

        difference = abs(value - last_value)
        if difference > save_value_change:
            too_steep += 1
            number_information['too_steep'] = True

        if last_value == value:
            last_value = value
            equals += 1
            number_information['category'] = 'equals'
            value_categories.append(number_information)
            continue

        if last_value > value:
            last_value = value
            decrements += 1
            number_information['category'] = 'decrements'
            value_categories.append(number_information)
            continue

        if last_value < value:
            last_value = value
            increments += 1
            number_information['category'] = 'increments'
            value_categories.append(number_information)
            continue

    return {'increments': increments, 'decrements': decrements, 'equals': equals, 'too_steep': too_steep, 'value_info': value_categories}


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
    errors = 0
    for i in range(1, len(_values)):
        difference = abs(_values[i] - _values[i - 1])
        if difference > save_value_change:
            errors += 1

    return errors <= 1


amount_save_reports = 0

for row in open('data_1_example.txt').readlines():
    parts = row.split(' ')
    values = []
    for part in parts:
        values.append(int(part.strip()))

    print(get_value_stats(values))

    #if not all_increment(values):
        #values = remove_bad_increment(values)

    if not all_increment(values) and not all_decrement(values):
        continue

    if is_change_save(values):
        #print(parts)
        amount_save_reports += 1

print("Save Reports:", amount_save_reports)
