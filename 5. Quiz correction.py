answers = ['b', 'a', 'd', 'c']
correct = ['b', 'c', 'd', 'c']

temp = 0
for i,j in zip(answers, correct):
    if i == j:
        temp = temp + 1

print(f"score {temp} / {len(answers)}")

