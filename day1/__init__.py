file1 = open('day1/input', 'r')
lines = file1.readlines()


# TODO fix the last dataset not being read
def calorie_counting():
    max_elf_calories = 0
    second_max_elf_calories = 0
    third_max_elf_calories = 0
    current_elf_calories = 0
    for line in lines:
        # if line is not empty
        if line.strip():
            # add data to current elf calories
            current_elf_calories += int(line)
        else:
            # check if total current elf calories is bigger than max elf calories
            # print('Elf with calories:', current_elf_calories)
            if current_elf_calories > max_elf_calories:
                temp = max_elf_calories

                # print('setting elf as first')
                max_elf_calories = current_elf_calories

                # in the third place is now the elf which was the second before
                third_max_elf_calories = second_max_elf_calories

                # in the second place is now the elf which was the first before
                second_max_elf_calories = temp

            elif current_elf_calories > second_max_elf_calories:
                temp = second_max_elf_calories

                # print('setting elf as second')
                second_max_elf_calories = current_elf_calories

                # in the third place is now the elf which was the second before
                third_max_elf_calories = temp

            elif current_elf_calories > third_max_elf_calories:
                # print('setting elf as third')
                third_max_elf_calories = current_elf_calories
            # reset current elf calories
            current_elf_calories = 0

    print('Elf with most calories:', max_elf_calories)
    print('Sum of top three elf calories:', max_elf_calories + second_max_elf_calories + third_max_elf_calories)


calorie_counting()
