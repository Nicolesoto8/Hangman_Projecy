import random
from hangman_words import text_w

def gallows(panal):
    if panal == 0:
        gal = "------- I \n"\
              "        I\n"\
              "        I\n" \
              "        I\n" \
              "        I\n" \
              "        I\n" \
              "        I \n" \
              "        I\n"\
        "===================="
    if panal ==1:
        gal = "------- I \n" \
              " I      I\n" \
              "        I\n" \
              "        I\n" \
              "        I\n" \
              "        I\n" \
              "        I \n" \
              "        I\n" \
              "===================="
    if panal == 2:
        gal = "------- I \n" \
              " I      I\n" \
              " 0      I\n" \
              "        I\n" \
              "        I\n" \
              "        I\n" \
              "        I \n" \
              "        I\n" \
              "===================="
    if panal == 3:
        gal = "------- I \n" \
              " I      I\n" \
              " 0      I\n" \
              " 1      I\n" \
              "        I\n" \
              "        I\n" \
              "        I \n" \
              "        I\n" \
              "===================="
    if panal == 4:
        gal = "------- I \n" \
              " I      I\n" \
              " 0      I\n" \
              "/1      I\n" \
              "        I\n" \
              "        I\n" \
              "        I \n" \
              "        I\n" \
              "===================="
    if panal == 5:
        gal = "------- I \n" \
              " I      I\n" \
              " 0      I\n" \
              "/1\     I\n" \
              "        I\n" \
              "        I\n" \
              "        I \n" \
              "        I\n" \
              "===================="
    if panal == 6:
        gal = "------- I \n" \
              " I      I\n" \
              " 0      I\n" \
              "/1\     I\n" \
              "/       I\n" \
              "        I\n" \
              "        I \n" \
              "        I\n" \
              "===================="
    if panal == 7:
        gal = "------- I \n" \
              " I      I\n" \
              " 0      I\n" \
              "/1\     I\n" \
              "/ \     I\n" \
              "        I\n" \
              "        I \n" \
              "        I\n" \
              "===================="
    return gal
name = input('a name ')
again ='y'
while again == 'y':
    # chose a random word from the tex_w
    index = random.randint(0,len(text_w))
    word = text_w[index] # the word in hangman
    secret_word = list(word) # the word is broken down into a list of letters
    new_word = ['*' for i in range(len(secret_word))] # the letters in the list of secret_word are changed into '*'
    penalty = 0 # the penalty you start with
    letters_used = []  # the list of letters you already guess
    while '*' in new_word and penalty < 7: # this alows you to still guess if there are '*' left and the amount of penalty is less then 7
        guess = input('enter a letter\n') # here you guess a letter
        if guess not in secret_word or guess in letters_used: # this is what happens if you guess a letter that dose not go in secret_word
            penalty += 1 # you get +1 in penalty
        else: # this the opposite
            for i in range(len(secret_word)): # if the integer of the letter is in the secret_word
                if guess == secret_word[i]: # if the leter you guess is in the integers of the secret_word
                    new_word[i] = secret_word[i] # the integers in new_word are equal to the integers in secret_word
        letters_used.append(guess) # the letter you guess is going to be added to the list of letters_used
        print(gallows(penalty))
        print(letters_used)
        print('penalty',penalty) # here we will be placed the gallows call
        print(new_word)
    if penalty >= 7:
        print('GAME OVER',name ,'DIED ')
    else:
        print('YOU SAVED',name )
    again = input('if you want to go again press y, else, press n \n')
print('thank you for playing hangman! see you next time!')
exit()