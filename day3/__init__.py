file1 = open('day3/input', 'r')
lines = file1.readlines()


def rucksack():
    count = 0
    total = 0
    array = []
    total_in_array = 0
    for line in lines:
        count += 1
        first, second = line[:len(line) // 2], line[len(line) // 2:]
        char = find_first_common_letter(first, second)
        total += get_ord(char)
        array.append(line)
        if count % 3 == 0:
            char = find_common_letter(array)
            total_in_array += get_ord(char)
            # reset
            array = []

    print("Rucksack part 1:", total)
    print("Rucksack part 2:", total_in_array)


def find_first_common_letter(first, second):
    for c1 in first:
        for c2 in second:
            if c1 == c2:
                return c1


def find_common_letter(array):
    for c0 in array[0]:
        for c1 in array[1]:
            for c2 in array[2]:
                if c0 == c1 and c1 == c2:
                    return c0


def get_ord(char):
    if char.islower():
        # a = 1, b = 2, c = 3 ...
        return ord(char) - 96
    else:
        # A = 27, B = 28, C = 29 ...
        return ord(char) - 64 + 26


rucksack()
