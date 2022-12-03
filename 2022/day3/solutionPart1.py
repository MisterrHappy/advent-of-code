import string

priorities = list(string.ascii_lowercase) + list(string.ascii_uppercase)
priorities_sum = 0

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        half_items_amount = len(line.strip()) // 2
        first_rucksack = line[:half_items_amount]
        second_rucksack = line[half_items_amount:]

        for item in first_rucksack:
            if item in second_rucksack:
                priorities_sum += priorities.index(item) + 1
                break

print(f"The sum of the priorities is: {priorities_sum}")
