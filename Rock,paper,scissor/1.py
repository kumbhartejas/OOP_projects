import random
class Game:
 
 def __init__(self):
    print("_____Welcome to Stone,Paper and Scissor Game____")
    self.choices=["stone","paper","scissor"]
    self.menu()

 def menu(self):
  while True:
   print("\nType 's' to start or 'e' to end")
   try:
    m=input("\n: ").lower()
    if m=="s":
     self.start()
    elif m=="e":
     break
    else:
     print("Invalid input")
   except:
    print("invalid input")
     

 def user_choice(self):
  print("\nEnter 1 for stone\nEnter 2 for paper\nEnter 3 for Scissor")
  try:
   user=int(input("User:"))
   if user==1:
    return "stone"
   elif user==2:
    return "paper"
   elif user==3:
    return "scissor"
   else:
    print("Invalid choice")
  except:
   print("invalid input")



 def start(self):
  computer=random.choice(self.choices)
  userc = self.user_choice()
  if not userc:
    return 
  if computer==userc:
   print("Its a Tie")

  elif computer=='stone' and userc=="paper":
   print("You win, Your paper grab the stone")
  elif computer=="paper" and userc=="stone":
   print("Computer win, Your stone was grabbed by paper")

  elif computer=="scissor" and userc=="stone":
   print("You win, Your stone break the scissor")
  elif computer=='stone' and userc=="scissor":
   print("Computer win, Your scissor was break by stone")

  elif computer=='scissor' and userc=="paper":
   print("You win, Your scissor cut the paper")
  elif computer=="paper" and userc=="scissor":
   print("Computer win, Your paper was cut by scissor")


 


p1=Game()

 
