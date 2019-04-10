
import random

def has_user_won(word, letter_list):
    matches = 0
    for letter in word:
        if letter in letter_list:
            matches += 1

    if matches == len(word) :
        return True
    else:
        return False

def load_words_from_file():
    #esto hace que del fichero con las palabras cree una lista
    file = open("lista_palabras.txt", "r")
    memory_words = list()
    for line in file:
        line = line.rstrip()
        memory_words.append(line)
    file.close()
    return memory_words

def print_word_with_hidden_characters(word, letter_list):
    for current_letter in word:
        if current_letter in letter_list:
            print(current_letter, " ",end = '')
        else:
            print("-", " ", end = '')

memory_words = load_words_from_file()

word = random.choice(memory_words)

print("The word has",len(word), "letters.")
word_letter = set(list(word))

letter_list = set()
lifes = 8
while lifes > 0:
    print("\n")
    letter = input("Enter a letter or a word: ")
    letter_list.add(letter)
    #este if compara la palabra que el usuario cree con la que es, si es correcta: win
    if letter == word:
        print("You're right!")
        exit()

    print_word_with_hidden_characters(word, letter_list)
    
    #esto se tiene que hacer solo si la letra no aparece en la palabra.
    if letter not in word:
        lifes = lifes - 1
    print("\n")
    print("Te quedan", lifes, "oportunidades")
    print(letter_list)

   #redirige al def y lo ejecuta, si el resultado es True: win and exit

    if has_user_won(word, letter_list):
        print("You win!!!!")
        exit()

print("Game Over! The word was", word,".")