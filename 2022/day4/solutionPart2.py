total_overlaps = 0

def check_overlap(left_start: int, right_start: int, end: int) -> bool:
    return left_start >= right_start and left_start <= end

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        left_elf_range, right_elf_range = line.split(",")
        left_elf_start, left_elf_end = left_elf_range.split("-") 
        right_elf_start, right_elf_end = right_elf_range.split("-") 

        left_start = int(left_elf_start)
        left_end = int(left_elf_end.strip())

        right_start = int(right_elf_start)
        right_end = int(right_elf_end.strip())

        if check_overlap(left_start, right_start, right_end) or check_overlap(right_start, left_start, left_end):
            total_overlaps += 1


print(f"Number of total overlaps is: {total_overlaps}")
