import re

number_of_visible_trees = 0

def look_up_and_down(start: int, end: int, tree_height, trees_lines, column):
    for l in range(start, end):
        if int(tree_height) <= int(trees_lines[l][column]):
            return False
    return True


with open("input.txt", "r") as input_file:
    trees_lines = input_file.readlines()
    first_line = trees_lines[0].rstrip()
    # Visible trees on the edges. 4 is the already counted corners 
    number_of_visible_trees += 2 * len(first_line) + 2 * len(trees_lines) - 4

    # skip first and last lines of trees
    for x in range(1, len(trees_lines) - 1):
        tree_line = trees_lines[x]
        for y in range(1, len(tree_line) - 2):
            tree_height = tree_line[y]
            regex_pattern = re.compile(f'[{tree_height}-9]')
            # Look right and left
            if not re.search(regex_pattern, tree_line[y + 1:]) or not re.search(regex_pattern, tree_line[:y]):
                number_of_visible_trees += 1
                continue

            # Look up and down
            if look_up_and_down(0, x, tree_height, trees_lines, y) or look_up_and_down(x + 1, len(trees_lines), tree_height, trees_lines, y):
                number_of_visible_trees += 1
                continue

print(f"The number of visible trees is: {number_of_visible_trees}")
