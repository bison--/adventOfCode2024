from uu import decode

save_value_change = 3


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


def stats_save(_value_stats):
    too_steep = _value_stats['too_steep']
    equals = _value_stats['equals']
    increments = _value_stats['increments']
    decrements = _value_stats['decrements']

    if too_steep > 2:
        return False

    if equals > 2:
        return False

    max_value = max(increments, decrements)
    min_value = min(increments, decrements)

    difference = max_value - (max_value - min_value)

    if difference > 1:
        return False

    return True


amount_save_reports = 0

for row in open('data_1_example.txt').readlines():
    parts = row.split(' ')
    values = []
    for part in parts:
        values.append(int(part.strip()))

    value_stats = get_value_stats(values)
    print(values, ' | ', get_value_stats(values))

    #if not all_increment(values):
        #values = remove_bad_increment(values)

    if stats_save(value_stats):
        #print(parts)
        amount_save_reports += 1

print("Save Reports:", amount_save_reports)
