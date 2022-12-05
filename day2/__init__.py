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
        pair = line.strip().split(" ")
        total_part_1 += part_1(pair)
        total_part_2 += part_2(pair)
    print('Rock paper scissors part 1:', total_part_1)
    print('Rock paper scissors part 2:', total_part_2)


# Your total score is the sum of your scores for each round.
# The score for a single round is the score for the shape you selected: 1 for Rock, 2 for Paper, and 3 for Scissors,
# plus the score for the outcome of the round: 0 if you lost, 3 if the round was a draw, and 6 if you won.
def part_1(arr):
    if arr[0] == 'A':
        if arr[1] == 'X':
            # rock vs rock: draw (3) + rock (1)
            return 4
        elif arr[1] == 'Y':
            # rock vs paper: win (6) + paper (2)
            return 8
        elif arr[1] == 'Z':
            # rock vs scissors: loss (0) + scissors (3)
            return 3
    elif arr[0] == 'B':
        if arr[1] == 'X':
            # paper vs rock: loss (0) + rock (1)
            return 1
        elif arr[1] == 'Y':
            # paper vs paper: draw (3) + paper (2)
            return 5
        elif arr[1] == 'Z':
            # paper vs scissors: win (6) + scissors (3)
            return 9
    elif arr[0] == 'C':
        if arr[1] == 'X':
            # scissors vs rock: win (6) + rock (1)
            return 7
        elif arr[1] == 'Y':
            # scissors vs paper: loss (0) + paper (2)
            return 2
        elif arr[1] == 'Z':
            # scissors vs scissors: draw (3) + scissors (3)
            return 6


# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
def part_2(arr):
    if arr[0] == 'A':
        if arr[1] == 'X':
            # rock vs scissors: loss (0) + scissors (3)
            return 3
        elif arr[1] == 'Y':
            # rock vs rock: draw (3) + rock (1)
            return 4
        elif arr[1] == 'Z':
            # rock vs paper: win (6) + paper (2)
            return 8
    elif arr[0] == 'B':
        if arr[1] == 'X':
            # paper vs rock: loss (0) + rock (1)
            return 1
        elif arr[1] == 'Y':
            # paper vs paper: draw (3) + paper (2)
            return 5
        elif arr[1] == 'Z':
            # paper vs scissors: win (6) + scissors (3)
            return 9
    elif arr[0] == 'C':
        if arr[1] == 'X':
            # scissors vs paper: loss (0) + paper (2)
            return 2
        elif arr[1] == 'Y':
            # scissors vs scissors: draw (3) + scissors (3)
            return 6
        elif arr[1] == 'Z':
            # scissors vs rock: win (6) + shape (1)
            return 7


rock_paper_scissors()
