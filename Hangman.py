import json
import random
from collections import Counter
import conboy


rand=random.randint(0,176063)
file=open("d:\projects\dictionary\Dictionary.json","r")
dictionary=json.load(file)
word = dictionary[rand]["word"].upper()
description = dictionary[rand]["description"]
word_type = dictionary[rand]["type"]
word_len = len(word)
print("\n")
print("*"*100,end="\n")
print("HANGMAN")
print("\n\n")
print("Guess the given word correctly before 5 wrong guesses\n")
print("\nHints:",description,word_type,word_len,"letters\n") 
for i in word:
    print('_',end=" ")
     
letter_guessed=""
state=0
chances=5
correct=0

while(chances!=0):
    try:
        print("\n")
        guess = str(input("Enter a letter to guess: ")).upper()
    except:
        print("Invalid Input! Enter lettrs only.")
        continue

    if not guess.isalpha():
        print("Enter valid alphabet")
        continue
    elif len(guess) > 1:
        print("Please enter a single character at a time.")
        continue
    elif guess in letter_guessed:
        print("you have already guessed that letter")

    if guess in word:
        k = word.count(guess)
        for _ in range(k):
            letter_guessed+=guess

    elif not guess in word:
        state+=1
        chances-=1

    for char in word:
        if char in letter_guessed and (Counter(letter_guessed) != Counter(word)):
            print(char,end=" ")
            correct+=1

        elif (Counter(letter_guessed) == Counter(word)):
            print("You guessed it correctly")
            state=6
            print(f"The word is {word}.")
            break 
            break

        else:
            print("_",end=" ")

        

    if chances <= 0 and (Counter(letter_guessed)!=Counter(word)):
        print("\n\nAlas! You lost the game.")
        print(f"The correct word was {word}.")
        
    
    conboy.boy(state)

                
