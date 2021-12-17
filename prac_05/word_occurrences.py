'''
CP1404/CP5632 Practical - Suggested Solution
Count word occurrences in a string
'''

word_to_count = {}
text = input("Text: ")
words = text.split()
print(words)
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

words = list(word_to_count.keys())
words.sort()

for word in words:
    print(word, ":", word_to_count[word])






