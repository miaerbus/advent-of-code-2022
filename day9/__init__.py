file1 = open('day9/sample', 'r')
lines = file1.readlines()

head = [(0, 0)]
tail = [(0, 0)]
positions = set()


def rope_bridge():
    for line in lines:
        direction, amount = line.strip().split()
        move(direction, int(amount))

    print("Rope bridge, part 1:", len(positions))
    print("Rope bridge, part 2:")


def move(direction, amount):
    if direction == 'R':
        for i in range(amount):
            last_head = head[-1]
            last_tail = tail[-1]
            head_to_add = (last_head[0] + 1, last_head[1])
            head.append(head_to_add)
            tail_to_add = (head_to_add[0] - 1, last_head[1])
            check_diagonal(head_to_add, last_tail, tail_to_add)

    elif direction == 'L':
        for i in range(amount):
            last_head = head[-1]
            last_tail = tail[-1]
            head_to_add = (last_head[0] - 1, last_head[1])
            head.append(head_to_add)
            tail_to_add = (head_to_add[0] + 1, last_head[1])
            check_diagonal(head_to_add, last_tail, tail_to_add)

    elif direction == 'U':
        for i in range(amount):
            last_head = head[-1]
            last_tail = tail[-1]
            head_to_add = (last_head[0], last_head[1] + 1)
            head.append(head_to_add)
            tail_to_add = (last_head[0], head_to_add[1] - 1)
            check_diagonal(head_to_add, last_tail, tail_to_add)

    elif direction == 'D':
        for i in range(amount):
            last_head = head[-1]
            last_tail = tail[-1]
            head_to_add = (last_head[0], last_head[1] - 1)
            head.append(head_to_add)
            tail_to_add = (last_head[0], head_to_add[1] + 1)
            check_diagonal(head_to_add, last_tail, tail_to_add)


def check_diagonal(head_to_add, last_tail, tail_to_add):
    if abs(last_tail[0] - head_to_add[0]) < 2 and abs(last_tail[1] - head_to_add[1]) < 2:
        tail.append(last_tail)
        positions.add(last_tail)
    else:
        tail.append(tail_to_add)
        positions.add(tail_to_add)


rope_bridge()
