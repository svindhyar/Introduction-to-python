# read text file
with open("data/text.txt") as file:
    text = file.read()

# lowercase text "introduction to python!"
text = text.lower()

# remove special characters 
for delete_character in ".,!?":
    text = text.replace(delete_character, "")

# split text into list of words
text = text.split()

number_of_words = len(text)

unique_words = []
for word in text:
    if word not in unique_words:
        unique_words.append(word)

# list in alphabetical order
text = sorted(unique_words)

# write into report
with open("data/report.txt", "w") as file:
    file.write(f"words: {number_of_words}\n")
    file.write(f"Unique words: {len(unique_words)}\n")
    for words in text:
        file.write(f"{words}\n")