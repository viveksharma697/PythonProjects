from fileinput import close
import random
def hangman():
    words_list = ['india', 'russia', 'belarus', 'bangladesh', 'pakistan']
    word = random.choice(words_list)
    turn = 10
    guesses = ''
    a = set('qwertyuioplkjhgfdsazxcvbnm')


    while len(word)>0:
        mainWord = ''
        missed = 0

        for letter in word:
            if letter in guesses:
                mainWord = mainWord + letter
            else:
                mainWord = mainWord + "_ "

        if mainWord == word:
            print(mainWord)
            print("You Won!!!!")
            break
            

        print("Guess the words ", mainWord)
        guess = input()

        if guess in a:
            guesses = guesses + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turn = turn - 1

            if turn==9:
                print("9 turns left!!!!!")
                print("---------------")
            if turn==8:
                print("8 turns left!!!!!")
                print("---------------")
                print("       O       ")
            if turn==7:
                print("7 turns left!!!!!")
                print("---------------")
                print("       O       ")
                print("       |       ")   
            if turn==6:
                print("6 turns left!!!!!")
                print("---------------")
                print("       O       ")
                print("       |       ")
                print("      /        ")  
            if turn==5:
                print("5 turns left!!!!!")
                print("---------------")
                print("       O       ")
                print("       |       ")
                print("      / \      ")  
            if turn==4:
                print("4 turns left!!!!!")
                print("---------------")
                print("      \O       ")
                print("       |       ")
                print("      / \      ")  
            if turn==3:
                print("3 turns left!!!!!")
                print("---------------")
                print("      \O/      ")
                print("       |       ")
                print("      / \      ") 
            if turn==2:
                print("2 turns left!!!!!")
                print("---------------")
                print("      \O/ |    ")
                print("       |       ")
                print("      / \      ") 
            if turn==1:
                print("Only 1 turn left!!!!!  Hangman on his last breath")
                print("---------------")
                print("      \O/_|    ")
                print("       |       ")
                print("      / \      ") 
            if turn==0:
                print("YOU LOOSE  !!!")
                print("You let a good man die")
                print("---------------")
                print("       O_|     ")
                print("      /|\      ")
                print("      / \      ") 
                break



        


p = print("Enter Your First Name : ")
x = input()
q = print("Enter Your Last Name : ")
y = input()
z = x +" "+ y
print("Welcome Mr.", z)
print("------------------------------------")
print("Try to guess the word in less than 10 attempts")
hangman()