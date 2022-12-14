import math

file1 = open('day11/input', 'r')
lines = file1.readlines()


def monkey_in_the_middle():
    count = 0
    monkeys = []
    monkey_id = 0
    items = []
    operation = ''
    divider = 0
    monkey_if_positive = 0
    monkey_if_negative = 0
    for line in lines:
        if line.strip():
            if count == 0:
                monkey_id = int(line.strip().split()[1][0])
            elif count == 1:
                starting_items = line.strip().split()[2:]
                for item in starting_items:
                    if ',' in item:
                        items.append(int(item[:-1]))
                    else:
                        items.append(int(item))
            elif count == 2:
                operation = line.strip().split("=")[1].strip()
            elif count == 3:
                divider = int(line.strip().split()[3])
            elif count == 4:
                monkey_if_positive = int(line.strip().split()[5])
            elif count == 5:
                monkey_if_negative = int(line.strip().split()[5])
            count += 1
        else:
            monkeys.append(Monkey(monkey_id, items, operation, divider, monkey_if_positive, monkey_if_negative, 0))
            count = 0
            monkey_id = 0
            items = []
            operation = ''
            divider = 0
            monkey_if_positive = 0
            monkey_if_negative = 0

    least_common_denominator = 1
    for monkey in monkeys:
        least_common_denominator *= monkey.divider

    for i in range(10_000):
        print("inspecting #", i)
        inspect(monkeys, least_common_denominator)

    largest, second_largest = two_largest(monkeys)

    print("Monkey in the middle:", largest * second_largest)


def inspect(monkeys, lcd):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspection += 1
            # value = math.floor(eval(monkey.operation.replace("old", str(item))) / 3)  # part 1
            value = math.floor(eval(monkey.operation.replace("old", str(item))) % lcd)  # part 2
            if value % monkey.divider == 0:
                monkeys[monkey.monkey_if_positive].items.append(value)
            else:
                monkeys[monkey.monkey_if_negative].items.append(value)
        # after inspection, remove all items from the monkey
        monkey.items = []


def two_largest(monkeys):
    largest = 0
    second_largest = 0
    for monkey in monkeys:
        if monkey.inspection > largest:
            second_largest = largest
            largest = monkey.inspection
        elif largest > monkey.inspection > second_largest:
            second_largest = monkey.inspection
    return largest, second_largest


class Monkey:
    def __init__(self, monkey_id, items, operation, divider, monkey_if_positive, monkey_if_negative, inspection):
        self.monkey_id = monkey_id
        self.items = items
        self.operation = operation
        self.divider = divider
        self.monkey_if_positive = monkey_if_positive
        self.monkey_if_negative = monkey_if_negative
        self.inspection = inspection


monkey_in_the_middle()
