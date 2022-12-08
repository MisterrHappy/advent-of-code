highest_scenic = 0

def look_up_and_down(start: int, end: int, tree_height: str, trees_lines: list[str], column: int, step = 1) -> int:
    score = 0
    for l in range(start, end, step):
        score += 1
        if int(tree_height) <= int(trees_lines[l][column]):
            return score
    return score

def look_right_and_left(start: int, end: int, tree_height: str, trees_lines: list[str], line: int, step = 1) -> int:
    score = 0
    for c in range(start, end, step):
        score += 1
        if int(tree_height) <= int(trees_lines[line][c]):
            return score
    return score


with open("input.txt", "r") as input_file:
    trees_lines = input_file.readlines()
    # skip first and last lines of trees
    for x in range(1, len(trees_lines) - 1):
        tree_line = trees_lines[x]
        for y in range(1, len(tree_line) - 2):
            tree_height = tree_line[y]
           # Look right and left
            score = look_right_and_left(y - 1, -1, tree_height, trees_lines, x, -1) * look_right_and_left(y + 1, len(tree_line) - 1, tree_height, trees_lines, x)
            # Look up and down
            score *= look_up_and_down(x - 1, -1, tree_height, trees_lines, y, -1) * look_up_and_down(x + 1, len(trees_lines), tree_height, trees_lines, y)
            if score > highest_scenic:
                highest_scenic = score

print(f"Highest scenic is: {highest_scenic}")
