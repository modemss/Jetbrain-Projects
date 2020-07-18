#%%
import random
lst = ['python', 'java', 'kotlin', 'javascript']
random.seed()
word = random.choice(lst)
def update(letter=None):
    global mask
    if letter in word:
        for i in range(len(mask)):
            if word[i] == letter:
                mask[i] = letter
def play():
    lives = 8
    global mask
    mask = ['-' for i in word]
    lstw = list()
    while lives > 0:
        if ''.join(mask) == word:
            print(word, 'You guessed the word!', 'You survived!', sep='\n')
            break
        print()
        print(''.join(mask))
        inp = input('Input a letter: ')
        if len(inp) > 1:
            print('You should input a single letter')
            continue
        if inp in lstw:
            print('You already typed this letter')
            continue
        lstw.append(inp)
        if not inp.isalpha() or not inp.islower():
            print('It is not an ASCII lowercase letter')
            continue
        elif inp not in word:
            lives -= 1
            print('No such letter in the word')
            continue
        else:
            update(inp)
    if lives == 0:
        print('You are hanged!')

print('H A N G M A N')
menu = input("Type \"play\" to play the game, \"exit\" to quit: ")
if menu == 'play':
    play()
elif menu == 'exit':
    quit()






