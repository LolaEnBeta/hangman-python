
word = input("Enter the word:")
word_length = len(word)
print(word_length)

x = 8
while x > 0:
    letter = input("Write one letter:")
    letter_position = word.find(letter)
    print(letter_position)
    x = x - 1
print("Game Over!")
