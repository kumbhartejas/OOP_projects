import pandas as pd

class TicTacToe:

    def __init__(self):
        self.df = pd.DataFrame([
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ])

        self.user_input()
        self.check_winner()

    def display_board(self):
        print(self.df.to_string(index=False, header=False))

    def user_input(self):

        print("Board Positions")
        print("""
1 2 3
4 5 6
7 8 9
""")

        self.display_board()

        for i in range(4):

            input1 = int(input("Player 1 (X): "))

            match input1:
                case 1:
                    self.df.loc[0, 0] = "X"
                case 2:
                    self.df.loc[0, 1] = "X"
                case 3:
                    self.df.loc[0, 2] = "X"
                case 4:
                    self.df.loc[1, 0] = "X"
                case 5:
                    self.df.loc[1, 1] = "X"
                case 6:
                    self.df.loc[1, 2] = "X"
                case 7:
                    self.df.loc[2, 0] = "X"
                case 8:
                    self.df.loc[2, 1] = "X"
                case 9:
                    self.df.loc[2, 2] = "X"
                case _:
                    print("Invalid Input")

            self.display_board()

            input2 = int(input("Player 2 (O): "))

            match input2:
                case 1:
                    self.df.loc[0, 0] = "O"
                case 2:
                    self.df.loc[0, 1] = "O"
                case 3:
                    self.df.loc[0, 2] = "O"
                case 4:
                    self.df.loc[1, 0] = "O"
                case 5:
                    self.df.loc[1, 1] = "O"
                case 6:
                    self.df.loc[1, 2] = "O"
                case 7:
                    self.df.loc[2, 0] = "O"
                case 8:
                    self.df.loc[2, 1] = "O"
                case 9:
                    self.df.loc[2, 2] = "O"
                case _:
                    print("Invalid Input")

            self.display_board()

    def check_winner(self):

        df = self.df

        # Player 1
        if (
            (df.loc[0,0]=="X" and df.loc[0,1]=="X" and df.loc[0,2]=="X") or
            (df.loc[1,0]=="X" and df.loc[1,1]=="X" and df.loc[1,2]=="X") or
            (df.loc[2,0]=="X" and df.loc[2,1]=="X" and df.loc[2,2]=="X") or
            (df.loc[0,0]=="X" and df.loc[1,0]=="X" and df.loc[2,0]=="X") or
            (df.loc[0,1]=="X" and df.loc[1,1]=="X" and df.loc[2,1]=="X") or
            (df.loc[0,2]=="X" and df.loc[1,2]=="X" and df.loc[2,2]=="X") or
            (df.loc[0,0]=="X" and df.loc[1,1]=="X" and df.loc[2,2]=="X") or
            (df.loc[0,2]=="X" and df.loc[1,1]=="X" and df.loc[2,0]=="X")
        ):
            print("Player 1 Wins")

        # Player 2
        elif (
            (df.loc[0,0]=="O" and df.loc[0,1]=="O" and df.loc[0,2]=="O") or
            (df.loc[1,0]=="O" and df.loc[1,1]=="O" and df.loc[1,2]=="O") or
            (df.loc[2,0]=="O" and df.loc[2,1]=="O" and df.loc[2,2]=="O") or
            (df.loc[0,0]=="O" and df.loc[1,0]=="O" and df.loc[2,0]=="O") or
            (df.loc[0,1]=="O" and df.loc[1,1]=="O" and df.loc[2,1]=="O") or
            (df.loc[0,2]=="O" and df.loc[1,2]=="O" and df.loc[2,2]=="O") or
            (df.loc[0,0]=="O" and df.loc[1,1]=="O" and df.loc[2,2]=="O") or
            (df.loc[0,2]=="O" and df.loc[1,1]=="O" and df.loc[2,0]=="O")
        ):
            print("Player 2 Wins")

        else:
            print("No Winner Yet")


obj = TicTacToe()