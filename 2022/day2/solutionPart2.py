opponent_plays_index = {'A': 0, 'B': 1, 'C': 2}
final_outcome = {'X': [2, 0], 'Y': [0, 3], 'Z': [1, 6]}
play_scores = [1, 2, 3]
total_score = 0

with open("input.txt", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        opponent_play, final_round_outcome = line.split(" ")
        opponent_play_index = opponent_plays_index[opponent_play]
        index_to_advance, round_score = final_outcome[final_round_outcome.strip()]
        total_score += round_score + play_scores[(opponent_play_index + index_to_advance) % 3]


print(f"My total score is: {total_score}")
