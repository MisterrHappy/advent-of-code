import string

priorities = list(string.ascii_lowercase) + list(string.ascii_uppercase)
priorities_sum = 0

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    for line_index in range(0, len(lines), 3):
        elf_one, elf_two, elf_three = lines[line_index:(line_index + 3)]

        for item in elf_one:
            if item in elf_two and item in elf_three:
                priorities_sum += priorities.index(item) + 1
                break

print(f"The sum of the priorities is: {priorities_sum}")
