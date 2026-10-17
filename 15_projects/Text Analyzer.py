
print("=============")
print("Text Analyzer")
print("=============")

paragraph = input("Enter a paragraph of text: ")

# Word Count

word_count = (
     paragraph.lower()
    .replace(".", "")
    .replace(",", "")
    .replace("!", "")
    .replace("?", "")
    .replace(":", "")
    .replace(";", "")
    .split()
)
print(f"The number of words in your paragraph is {len(word_count)}")

# Character Count(Excluding Spaces)

count = 0
for character in paragraph:
    if character != " ":
        count += 1

print(f"The number of characters in your paragraph is {count}")

#Sentence count

sentence_count = 0

for sentence in paragraph:
    if sentence == "." or sentence == "!" or sentence == "?":
        sentence_count += 1
print(f"The number of sentences in your paragraph is {sentence_count}")

#unique words count

word_set = set(word_count)
print(f"The number of unique words in your paragraph is {len(word_set)}")

#most common word

common_word = {}
for word in word_count:
    if word in common_word:
        common_word[word] += 1
    else:
        common_word[word]  = 1

most_common = ""
highest_count = 0

for word in common_word:
    most_common_word_count = common_word[word]
    if most_common_word_count  > highest_count:
        most_common = word
        highest_count=common_word[word]

print(f"Most common word: {most_common}")
print(f"Occurrences: {highest_count} ")


#longest word

longest_word = ""
length = 0

for word in word_count:
    if len(word) > length:
        longest_word = word
        length = len(word)

print(f"Longest word: {longest_word}")
print(f"Length: {length}")

# average word length
total_word_length = 0

for word in word_count:
    total_word_length += len(word)

if not word_count:
    print("No words found to calculate the average!")
else:
    average_word_length = total_word_length / len(word_count)
    print(f"The average word length is {average_word_length:.2f}")



