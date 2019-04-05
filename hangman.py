
word = input("Enter a word:")
print(len(word))
word_letter = set(list(word))

letter_list = set(list())
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

    #este if compara la lista de la palabra introducida con la creada a partir de input
    #si es igual: el jugador gana y cierra el programa
    if letter_list == word_letter:
        print("You win this time!")
        exit()

    #esto se tiene que hacer solo si la letra no aparece en la palabra.
    if not found_letter:
        x = x - 1
    print("Te quedan ", x, " oportunidades")
    print(letter_list)
    
print("Game Over!")
