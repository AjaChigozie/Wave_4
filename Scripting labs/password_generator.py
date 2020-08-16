# Write a function called generate_password that selects three random words from the list of words word_list and
# concatenates them into a single string. Your function should not accept any arguments and should reference the
# global variable word_list to build the password.

import random
# Use an import statement at the top


def generated_password(filename):
    word_file = "words.txt"
    word_list = []

    # fill up the word_list
    with open('words.txt', 'r') as words:
        for line in words:
            # remove white space and make everything lowercase
            word = line.strip().lower()
            # don't include words that are too long or too short
            if 3 < len(word) < 8:
                word_list.append(word)
    return word_list

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces


word_list = generated_password(filename='words.txt')
# test your function
print(random.choice(word_list) + random.choice(word_list) + random.choice(word_list))

