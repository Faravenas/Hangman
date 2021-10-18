import os
import random

DATA_PATH = 'data.txt'
HEADER = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       

Instructions:
1.- Guess the word to save the hanged man
2.- We recommend not using characters other than letters of the alphabet!
3.- Easy mode: Short length words, Normal Mode: Medium length words, Hard mode: Large length words, without list of used letters'''
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def main():
    os.system("clear")
    print(HEADER)
    while True:
        query = input("\nPlease choose a difficulty (1 = Easy, 2 = Normal, 3 = Hard): ")
        if query == '1':
            difficulty = 'easy'
            break
        elif query == '2':
            difficulty = 'normal'
            break
        elif query == '3':
            difficulty = 'hard'
            break
        else:
            print("Please choose a valid choise!")
    game(difficulty)


def game(difficulty):
    word = choose_word_from_file()

    while difficulty == 'easy' and len(word) > 4:
        word = choose_word_from_file()

    while difficulty == 'normal' and len(word) < 4 or len(word) > 7:
        word = choose_word_from_file()

    while difficulty == 'hard' and len(word) < 7:
        word = choose_word_from_file()

    word_to_list = [char for char in word]
    blank_word_to_list = ["_" for i in range(len(word_to_list))]
    used_chars = []
    tries = 0

    while True:
        os.system("clear")
        print(HEADER)
        print(HANGMANPICS[tries])
        print(blank_word_to_list)
        print("\nRemaning attempts:", (len(HANGMANPICS) - 1) - tries)

        if difficulty == 'normal' or difficulty == 'easy':
            print("\nYou used and missed the following letters:", used_chars)

        choosen_char = input("\nChoose your letter: ").lower()

        for id,char in enumerate(word_to_list):
            if char == choosen_char:
                blank_word_to_list[id] = char

        if choosen_char not in used_chars and choosen_char not in blank_word_to_list:
            used_chars.append(choosen_char)
            tries = tries + 1

        if tries == len(HANGMANPICS) - 1:
            os.system("clear")
            print("You LOOSE!\n", HANGMANPICS[tries], "\nYou reached the maximum number of attempts:", tries, "\nThe word was:", word)
            break

        if word_to_list == blank_word_to_list:
            os.system("clear")
            print("You WIN!\n", HANGMANPICS[tries], "\nYour tries were:", tries, "\nThe word was:", word)
            break


def choose_word_from_file():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        word_list = [word.replace("\n", "") for word in f]
        word = random.choice(word_list)
    return word


if __name__ == '__main__':
    main()