scores = [12, 17, 9, 15, 14]

temp_score = 0
temp_index = 0
for index, score in enumerate(scores):
    if temp_score < score:
        temp_score = score
        temp_index = index + 1


print(f"Best score {temp_score}, student number {temp_index}")