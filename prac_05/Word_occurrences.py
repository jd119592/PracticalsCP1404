""" Word_occurrences.py
estimated time: 35min
actual time:    45min
a program to count the occurrences of words in a string.
The program should ask the user for a string, then print the counts of
how many of each word are in the string"""

from operator import itemgetter

word_to_count = {}
text = input("Text: ")
words = text.split()

for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1


sorted_words = sorted(word_to_count.items(), key=itemgetter(0))
sorted_word_to_count = dict(sorted_words)

longest_name_length = max([len(word) for word in sorted_word_to_count])

for word, count in sorted_word_to_count.items():
   print(f"{word:{longest_name_length}} : {count}")

