
def has_user_won(word, letter_list):
    matches = 0
    for letter in word:
        if letter in letter_list:
            matches += 1

    if matches == len(word) :
        return True
    else:
        return False

word = input("Enter a word:")
print(len(word))
word_letter = set(list(word))
print(word_letter)

letter_list = set()
x = 8
while x > 0:
    letter = input("Write one letter:")
    letter_list.add(letter)
    found_letter = False

    #este for recorre cada letra de la palabra.
    for current_letter in word:
        if current_letter == letter:
            found_letter = True
        #este if comprueba que la letra de la palabra coincide con la letra input, 
        #si coincide la escribe, sino escribe -.
        if current_letter in letter_list:
            print(current_letter)
        else:
            print("-")
   
    #esto se tiene que hacer solo si la letra no aparece en la palabra.
    if not found_letter:
        x = x - 1
    
    print("Te quedan ", x, " oportunidades")
    print(letter_list)

   #refirige al def y lo ejecuta, si el resultado es True: win and exit

    if has_user_won(word, letter_list):
        print("You win!!!!")
        exit()

print("Game Over!")
