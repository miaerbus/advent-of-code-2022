file1 = open('day2/input', 'r')
lines = file1.readlines()


# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
# The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.
# The second column must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.

def rock_paper_scissors():
    count = 0
    total_part_1 = 0
    total_part_2 = 0
    for line in lines:
        count += 1
        total_part_1 += part_1(line.strip().split(" "))
        total_part_2 += part_2(line.strip().split(" "))
    print('Rock scissor paper part 1:', total_part_1)
    print('Rock scissor paper part 2:', total_part_2)


# Your total score is the sum of your scores for each round.
# The score for a single round is the score for the shape you selected: 1 for Rock, 2 for Paper, and 3 for Scissors,
# plus the score for the outcome of the round: 0 if you lost, 3 if the round was a draw, and 6 if you won.
def part_1(arr):
    result = 0
    if arr[0] == 'A':
        if arr[1] == 'X':
            # rock vs rock: draw (3) + shape rock (1)
            result = 4
        if arr[1] == 'Y':
            # rock vs paper: win (6) + shape paper (2)
            result = 8
        if arr[1] == 'Z':
            # rock vs scissors: loss (0) + shape scissors (3)
            result = 3
    if arr[0] == 'B':
        if arr[1] == 'X':
            # paper vs rock: loss (0) + shape rock (1)
            result = 1
        if arr[1] == 'Y':
            # paper vs paper: draw (3) + shape paper (2)
            result = 5
        if arr[1] == 'Z':
            # paper vs scissors: win (6) + shape scissors (3)
            result = 9
    if arr[0] == 'C':
        if arr[1] == 'X':
            # scissors vs rock: win (6) + shape rock (1)
            result = 7
        if arr[1] == 'Y':
            # scissors vs paper: loss (0) + shape paper (2)
            result = 2
        if arr[1] == 'Z':
            # scissors vs scissors: draw (3) + shape scissors (3)
            result = 6
    return result


# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
def part_2(arr):
    result = 0
    if arr[0] == 'A':
        if arr[1] == 'X':
            # rock vs scissors: loss (0) + shape scissors (3)
            result = 3
        if arr[1] == 'Y':
            # rock vs rock: draw (3) + shape rock (1)
            result = 4
        if arr[1] == 'Z':
            # rock vs paper: win (6) + shape paper (2)
            result = 8
    if arr[0] == 'B':
        if arr[1] == 'X':
            # paper vs rock: loss (0) + shape rock (1)
            result = 1
        if arr[1] == 'Y':
            # paper vs paper: draw (3) + shape paper (2)
            result = 5
        if arr[1] == 'Z':
            # paper vs scissors: win (6) + shape scissors (3)
            result = 9
    if arr[0] == 'C':
        if arr[1] == 'X':
            # scissors vs paper: loss (0) + shape paper (2)
            result = 2
        if arr[1] == 'Y':
            # scissors vs scissors: draw (3) + shape scissors (3)
            result = 6
        if arr[1] == 'Z':
            # scissors vs scissors: win (6) + shape rock (1)
            result = 7
    return result


rock_paper_scissors()
