scores = []
try:
    with open('scores.txt', encoding='utf-8') as f:
        for line in f:
            try:
                score = int(line.strip())
                scores.append(score)
            except ValueError:
                print(f"Invalid score found: {line.strip()}")
            