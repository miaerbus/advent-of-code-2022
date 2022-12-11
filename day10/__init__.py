file1 = open('day10/input', 'r')
lines = file1.readlines()


def cathode_ray_tube():
    register = 1
    cycle = 1
    total = 0
    for line in lines:
        instruction = line.strip().split()
        if instruction[0] == 'addx':
            # first cycle
            total = calculate_special(cycle, register, total)
            draw(cycle, register)
            cycle += 1

            # second cycle
            total = calculate_special(cycle, register, total)
            draw(cycle, register)
            cycle += 1
            register += int(instruction[1])

        else:  # noop
            total = calculate_special(cycle, register, total)
            draw(cycle, register)
            cycle += 1

    print("Cathode-ray tube, part 1:", total)
    print("Cathode-ray tube, part 2:", "RZHFGJCB")
    ###..####.#..#.####..##....##..##..###..
    # ..#....#.#..#.#....#..#....#.#..#.#..#.
    # ..#...#..####.###..#.......#.#....###..
    ###...#...#..#.#....#.##....#.#....#..##
    # .#..#....#..#.#....#..#.#..#.#..#.#..##
    # ..#.####.#..#.#.....###..##...##..###..


def calculate_special(cycle, register, total):
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        total += register * cycle
    return total


def draw(cycle, register):
    if register == cycle % 40 or register == cycle % 40 - 1 or register == cycle % 40 - 2:
        print('#', end='')
    else:
        print('.', end='')
    if cycle % 40 == 0:
        print()


cathode_ray_tube()
