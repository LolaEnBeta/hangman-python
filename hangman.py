
word = input("Enter the word:")
word_length = len(word)
print(word_length)

x = 8
while x > 0:
    letter = input("Write one letter:")
    found_letter = False
    #este for recorre cada letra de la palabra.
    for current_letter in word:
        #este if comprueba que la letra de la palabra coincide con la letra input, 
        #si coincide la escribe, sino escribe -.
        if current_letter == letter:
            print(current_letter)
            found_letter = True
        else:
            print("-")

    #esto se tiene que hacer solo si la letra no aparece en la palabra.
    if not found_letter:
        x = x - 1
    print("Te quedan ", x, " oportunidades")
print("Game Over!")
