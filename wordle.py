# importing necessary functions
import random


# Implement a function word_list() that reads the 5_letter_words.txt file and returns a list of the words in the file.
def word_list():
    with open('5_letter_words.txt', 'r') as file:
        sec_words_list = []
        for words in file:
            words = words.strip()
            sec_words_list.append(words)
    return sec_words_list


# Implement a function random_word() that takes a list of words as a parameter and returns a random word from this list.
def random_word(sec_words_list):
    return sec_words_list[random.randrange(len(sec_words_list))]


# Implement a function is_real_word() that takes two parameters, a guess and a word list and returns True if the word
# is in the word list and False otherwise.
def is_real_word(user_guess, sec_words_list):
    return user_guess in sec_words_list


# Implement a function check_guess()that takes two parameters. The first is the guessed word and the second is the
# word the user has to find.following the conditions mentioned in the problem statement
def check_guess(user_guess, sec_word):
    if user_guess == sec_word:
        output = ['X', 'X', 'X', 'X', 'X']
        return ''.join(output)
    output = ['_', '_', '_', '_', '_']
    user_guess = list(user_guess)
    sec_word = list(sec_word)
    for i in range(len(sec_word)):
        if sec_word[i] == user_guess[i]:
            output[i] = 'X'
            sec_word[i] = '_'
            user_guess[i] = '_'
    for letter in sec_word:
        if letter in user_guess and letter != '_':
            index_1 = sec_word.index(letter)
            sec_word[index_1] = '_'
            index_2 = user_guess.index(letter)
            user_guess[index_2] = '_'
            output[index_2] = 'O'
    return ''.join(output)


# Implement a function next_guess() that takes a word list as a parameter. The function asks the user for a guess,
# converts the guess to lower case and checks if the guess is in the word list. If this is the case, the guess is
# returned. otherwise, the function asks the user for another guess.
def next_guess(sec_words_list):
    user_guess = input('Please enter a guess:')
    user_guess = user_guess.lower()
    check = is_real_word(user_guess, sec_words_list)
    while not check:
        print('That\'s not a real word!')
        user_guess = input('Please enter a guess:')
        user_guess = user_guess.lower()
        check = is_real_word(user_guess, sec_words_list)
    return user_guess


# Implement a function play() Uses the functions word_list and random_word to select a random 5 letter word. Asks the
# user for a guess using the next_guess function. Checks each guess using the check_guess function and shows the
# result to the user. Checks if the users guessed the right word with six guesses or less. If yes, the user wins and
# the function prints You won!. otherwise the user loses and the function prints You lost! as well as The word was:
# followed by word the user had to find.
def play():
    sec_words_list = word_list()
    sec_word = random_word(sec_words_list)
    attempt = 6
    while attempt > 0:
        user_guess = next_guess(sec_words_list)
        check = check_guess(user_guess, sec_word)
        print(check)
        attempt -= 1
        if check == 'XXXXX':
            print('You won!')
            return
    print('You lost!')
    print('The word was:', sec_word)


play()
