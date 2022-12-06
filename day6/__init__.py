file1 = open('day6/input', 'r')
lines = file1.readlines()


def tuning_trouble():
    count = 0
    for line in lines:
        count += 1
        part_1 = packet_marker(line, 4)
        part_2 = packet_marker(line, 14)
    print("Tuning trouble, part 1:", part_1)
    print("Tuning trouble, part 2:", part_2)


def packet_marker(string, number):
    for i in range(len(string)):
        if i > number:
            current_string = string[i - number:i]
            if is_unique(current_string):
                return i


def is_unique(string):
    # find all the repeated chars: https://stackoverflow.com/a/32090120/1137612
    set_of_repeated_chars = set(i for i in string if string.count(i) > 1)
    return len(set_of_repeated_chars) == 0


tuning_trouble()
