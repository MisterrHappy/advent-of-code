number_of_chars = 0

with open("input.txt", "r") as input_file:
    stream = input_file.readlines()[0].strip()
    marker = ''
    for c in stream:
        if len(marker) == 4:
            break

        number_of_chars += 1
        index_of_char = marker.find(c)
        if index_of_char != -1:
            marker = marker[index_of_char + 1:] + c
        else:
            marker += c
            
print(f"The number of processed chars before marker is: {number_of_chars}")
