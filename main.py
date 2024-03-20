# 1. Given a text file. You need to create a new file to rewrite all the words consisting of at least seven letters from the first file.
# 2. Given a text file. Count the number of words in it.
# 3. Create a program that checks the text for invalid words.
# If an invalid word is found, it should be replaced with a set of characters *.
# Based on the results of the program, you need to show the statistics of actions.
# We have text:
# To be, or not to be, that is the question,
# Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune,
# Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep;
# No more; and by a sleep to say we end The heart-ache and the thousand natural shocks
# That flesh is heir to, 'tis a consummation Devoutly to be wish'd. To die, to sleep

with open('text.txt', 'r', encoding='utf-8') as input_file:
    content = input_file.read()
    words = content.split()
    long_words = [word.strip(',.') for word in words if len(word) >= 7]

with open('new.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(' '.join(long_words))

with open('new.txt', 'r', encoding='utf-8') as output_file:
    print("Task 1")
    print("Edited text:")
    print(output_file.read())

with open('text.txt', 'r', encoding='utf-8') as input_file:
    content = input_file.read()
    words = content.split()
    word_count = len(words)
    print("\nTask 2")
    print("Words count in file:", word_count)

with open('text.txt', 'r', encoding='utf-8') as input_file:
    content = input_file.read()
    prohibited_words = ['die']
    replaced_text = content
    count = 0
    for word in prohibited_words:
        replaced_text, n = replaced_text.replace(word, '*' * len(word)), replaced_text.count(word)
        count += n

    print("\nTask 3")
    print("Prohibited word:", prohibited_words[0])
    print("Result:")
    print(replaced_text)
    print("Statistics: {} word replacements {}.".format(count, prohibited_words[0]))
