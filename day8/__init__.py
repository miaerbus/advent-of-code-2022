file1 = open('day8/input', 'r')
lines = file1.readlines()

WIDTH = len(lines[0]) - 1
HEIGHT = len(lines)


def treetop_tree_house():
    trees = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip()):
            if char != '':
                trees.append(Tree(char, i, j))

    visible = []
    counter = []
    for tree in trees:
        if tree.is_on_edge():
            visible.append(tree)
        else:
            top_is_visible, top_count = top(tree, trees)
            right_is_visible, right_count = right(tree, trees)
            bottom_is_visible, bottom_count = bottom(tree, trees)
            left_is_visible, left_count = left(tree, trees)
            count = top_count * right_count * bottom_count * left_count
            counter.append(count)
            if top_is_visible or right_is_visible or bottom_is_visible or left_is_visible:
                visible.append(tree)

    print("Treetop tree house, part 1:", len(visible))
    print("Treetop tree house, part 2:", max(counter))


def right(tree, trees):
    count = 0
    for t in trees:
        if t.x == tree.x and t.y > tree.y:
            count += 1
            if t.value >= tree.value:
                return False, count
    return True, count


def bottom(tree, trees):
    count = 0
    for t in trees:
        if t.x > tree.x and t.y == tree.y:
            count += 1
            if t.value >= tree.value:
                return False, count
    return True, count


def left(tree, trees):
    count = 0
    for t in reversed(trees):
        if t.x == tree.x and t.y < tree.y:
            count += 1
            if t.value >= tree.value:
                return False, count
    return True, count


def top(tree, trees):
    count = 0
    for t in reversed(trees):
        if t.x < tree.x and t.y == tree.y:
            count += 1
            if t.value >= tree.value:
                return False, count
    return True, count


class Tree:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y

    def is_on_edge(self):
        if self.x == 0 or self.x == WIDTH - 1 or self.y == 0 or self.y == HEIGHT - 1:
            return True
        return False


treetop_tree_house()
