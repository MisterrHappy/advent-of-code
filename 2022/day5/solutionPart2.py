from io import TextIOWrapper
import re

stacks: list[list] = []
crate_pattern = re.compile(r'\[[A-Z]\][.\s]')

def parse_crates(line: str):
    stack_index = 0
    for i in range(0, len(line), 4):
        crate = line[i:i+4]
        if crate_pattern.match(crate):
            stacks[stack_index].append(crate[1])
        stack_index += 1

def parse_initial_stacks(stacks, input_file: TextIOWrapper):
    first_line = input_file.readline()
    num_stacks = len(first_line) // 4
    for _ in range(num_stacks):
        stacks.append([])

    parse_crates(first_line)
    while first_line.strip():
        first_line = input_file.readline()
        parse_crates(first_line)

with open("input.txt", "r") as input_file:
    parse_initial_stacks(stacks, input_file)
    moves = input_file.readlines()

    for move_string in moves:
        move = re.findall(r'\d+', move_string)
        stack_index_origin = int(move[1]) - 1
        stack_index_destination = int(move[2]) - 1
        number_of_crates_to_move = int(move[0])
        crates_to_move = stacks[stack_index_origin][:number_of_crates_to_move]
        stacks[stack_index_destination] = crates_to_move + stacks[stack_index_destination]
        stacks[stack_index_origin] = stacks[stack_index_origin][number_of_crates_to_move:]

message = ''
for s in stacks:
    if len(s):
        message += s[0]
      
print(f"The message is: {message}")
