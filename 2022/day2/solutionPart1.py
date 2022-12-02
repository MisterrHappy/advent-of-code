game_items = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
total_score = 0

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        opponent_play, my_play = line.split(" ")
        opponent_play_score = game_items[opponent_play]
        my_play_score = game_items[my_play.strip()]
        score_diff = my_play_score - opponent_play_score
        total_score += 3 if not score_diff else 6 if score_diff == 1 or score_diff == -2 else 0
        total_score += my_play_score


print(f"My total score is: {total_score}")
