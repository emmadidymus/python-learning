
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
print(len(word_set))

#most common word
common_word = {}
for word in word_count:
    if word in common_word:
        common_word[word] += 1
    else:
        common_word[word]  = 1
print(common_word)
