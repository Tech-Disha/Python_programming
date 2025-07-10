#hangman game

#create a greeting
#create a word list
#randomly choose a word from the word list created
#ask a user to guess a letter
#take the input letter from user and make it lowercase
#check if the letter is in the wrod
#create an empty list
#For each letter in secret_word add "_" that will be printed on the console
#loop through each of the letter in chosen word
#if the letter is in the word replace "_" with the letter
#use while loop to keep guessing the letter until complete word is guessed
#create a variable starting with 0 and when it gets to 5 the game ends
#print users get only 5 guesses


import random
name = input("Enter your name ")
greeting = print(f"Welcome {name}to Hangman game")
print ("Guess the correct fruit ")

words = ["apple", "banana", "cherry", "orange", "mango"]
secret_word = random.choice(words)

print("You will only get 5 incorrect guesses")

display_word = []
for letter in secret_word:
    display_word += "_"
print(display_word)

num = 0

game_over = False

while not game_over:
    guess = input("Enter the your guess ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter

    if guess not in secret_word:
        num += 1
        guesse_left = 5 - num
        print (f"You can now make only {guesse_left} incorrect guesses")
        if num >= 5:
            print("You lose the game")
            game_over = True
    print(display_word)

    if "_" not in display_word:
        print("You Win!!")
        print(f"You correctly guessed the word {secret_word}")
        game_over = True



