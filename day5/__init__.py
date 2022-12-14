file1 = open('day5/input', 'r')
lines = file1.readlines()


def supply_stacks():
    count = 0
    instructions = []
    for line in lines:
        count += 1
        if line.strip():
            instructions.append(line)
        else:
            columns = transpose(instructions)
            # reset the array after diagram to append the instructions
            instructions = []

    print("Supply stacks:", decipher(columns, instructions))


def decipher(columns, instructions):
    array = []
    for line in instructions:
        # How to extract numbers from a string in Python https://stackoverflow.com/a/4289557/1137612
        array.append([int(s) for s in line.split() if s.isdigit()])

    for line in array:
        # TODO switch here between part 1 and 2 - refactor this
        move_part_2(columns, line[0], line[1] - 1, line[2] - 1)

    output = ''
    for i in range(len(columns)):
        output += columns[i][0]
    return output


def transpose(instructions):
    last = instructions[-1]
    number_of_columns = int(last.strip().split("  ")[-1])

    # add all but last line into rows
    rows = []
    for line in instructions[:-1]:
        # add missing data at the beginning of a line
        line = line.replace('   ', '[0]')
        rows.append(line.strip())

    # transpose rows into columns: [[], [], ...]
    columns = [[] for _ in range(number_of_columns)]
    for row in rows:
        for i in range(number_of_columns):
            char = row[(4 * i) + 1:(4 * i) + 2]
            # TODO check why ']' appears
            if char != '0' and char != '' and char != ']':
                columns[i].append(char)
    return columns


def move_part_1(columns, amount, base_column, target_column):
    for _ in range(amount):
        remain_base_column = columns[base_column][1:len(columns[base_column])]
        new_base_column = columns[base_column][0:1]
        new_target_column = new_base_column + columns[target_column]
        columns[base_column] = remain_base_column
        columns[target_column] = new_target_column
    return columns


def move_part_2(columns, amount, base_column, target_column):
    remain_base_column = columns[base_column][amount:len(columns[base_column])]
    new_base_column = columns[base_column][0:amount]
    new_target_column = new_base_column + columns[target_column]
    columns[base_column] = remain_base_column
    columns[target_column] = new_target_column
    return columns


supply_stacks()
