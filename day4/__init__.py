file1 = open('day4/input', 'r')
lines = file1.readlines()


def camp_cleanup():
    count = 0
    contained = 0
    overlapped = 0
    for line in lines:
        count += 1
        pair = line.strip().split(',')
        contained += is_contained(pair)
        overlapped += is_overlapped(pair)
    print("Camp cleanup, part 1:", contained)
    print("Camp cleanup, part 2:", overlapped)


def is_contained(pair):
    first = pair[0].split('-')
    second = pair[1].split('-')
    first_start = int(first[0])
    first_end = int(first[1])
    second_start = int(second[0])
    second_end = int(second[1])
    if first_start <= second_start and first_end >= second_end:
        return 1
    if first_start >= second_start and first_end <= second_end:
        return 1
    return 0


def is_overlapped(pair):
    first = pair[0].split('-')
    second = pair[1].split('-')
    first_start = int(first[0])
    first_end = int(first[1])
    second_start = int(second[0])
    second_end = int(second[1])
    if first_start <= second_end and first_end >= second_start:
        # print(first_start, first_end, '-', second_start, second_end)
        return 1
    if first_start >= second_end and first_end <= second_start:
        # print(first_start, first_end, '-', second_start, second_end)
        return 1
    return 0


camp_cleanup()
