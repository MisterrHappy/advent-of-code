maxCalories = -1

with open("input.txt", "r") as inputFile:
    lines = inputFile.readlines()
    elfCalories = 0
    for line in lines:
        if not line.strip():
            if elfCalories > maxCalories:
                maxCalories = elfCalories
            elfCalories = 0
        else:
            elfCalories += int(line)

print(f"Maximum elf calories is {maxCalories}")
