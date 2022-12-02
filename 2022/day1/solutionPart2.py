allElfsCalories = []

with open("input.txt", "r") as inputFile:
    lines = inputFile.readlines()
    elfCalories = 0
    for line in lines:
        if not line.strip():
            allElfsCalories.append(elfCalories)
            elfCalories = 0
        else:
            elfCalories += int(line)

allElfsCalories.sort(reverse=True)
print(f"Top three sum is: {sum(allElfsCalories[0:3])}")
