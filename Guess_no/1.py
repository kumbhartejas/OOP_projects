import random

class Guess:
    def __init__(self):
        print("_____________ Welcome to Guess the number game _____________")
        print(" You have to guess a random number between 1 to 100 in 7 changes to win ")
        self.menu()

    def menu(self):
        while True:
            print("\n Enter 1 to start new game\n Enter 2 to exit")
            try:
                menu=int(input("choice: "))
                if menu==1:
                    self.start()
                elif menu==2:
                    break
                else:
                    print("Please enter a valid input")
            except ValueError:
                print("Please enter a valid number")

    def start(self):
        self.guess_no=random.randint(1,100)
        self.chances=7
        
        while self.chances>0:
         try:
            guess=int(input("\n Please guess a number between 1 and 100: "))
            self.chances-=1
            if guess==self.guess_no:
                print("-------Congratulation ! You win your guess was right------\n")
                break
            elif self.chances==0:
                print(f"\n ------You lose! The number was {self.guess_no}------")
            elif guess>self.guess_no:
                print("Your guess is greater, please enter smaller number")
            elif guess<self.guess_no:
                print("Your guess is lower, please enter bigger number")
            
         except ValueError:
             print("Please enter valid no")

player=Guess()
          



