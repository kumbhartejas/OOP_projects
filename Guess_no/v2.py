import random

class Guess_no:
    def __init__(self):
      self.number=random.randint(1,100)
      self.chances=7
      print("You have 7 chances to guess the number between 1 to 100")
      print()
      self.user()

    def user(self):
        for i in range(self.chances):
         try:
            input_no=int(input("Guess a number betw 1 to 100: "))   
            if input_no==self.number:
               print("Congratulations your guess is correct!")
               break
            elif self.chances==0:
              print("Game Over....Number was",self.number)
            elif input_no < self.number:
              print("Your guess is smaller") 
              print(f"{self.chances-i-1} chances left")
              print()
            elif input_no > self.number:
              print("Your guess is greater")
              print(f"{self.chances-i-1} chances left")
              print()
        
         except ValueError:
             print("Please enter valid no")

c1=Guess_no()

