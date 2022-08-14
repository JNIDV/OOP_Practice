from grid import Grid

class TicTacToe:
    def __init__(self):
        print("Welcome to Tic Tac Toe!")
        self.run_game = True
        self.match_up = False
        self.play = False
        self.grid = Grid()
        self.player = {}
    
    def get_players(self):
        print("Player X, please enter your name.")
        self.player["X"] = input("Your name: ")
        print("Player O, please enter your name.")
        self.player["O"] = input("Your name: ")

    def get_cell_number(self, player):
        while True:
            print(f"{player}, please enter an integer from 1 to 9, inclusive.")
            try:
                cell_number = int(input("Your number: "))
            except ValueError:
                print("The input is not a number.")
                continue
            if cell_number < 1 or 9 < cell_number:
                print("The number must be between 1 and 9, inclusive.")
                continue
            if self.grid.cell[cell_number] != "_":
                print("The cell is already occupied.")
                continue
            return cell_number
    
    def say_draw(self):
        print(f"{self.player['X']} and {self.player['O']} drew!")

    def congratulate_winner(self):
        winner_mark = self.grid.status
        loser_mark = TicTacToe.switch_player(winner_mark)
        print(f"{self.player[winner_mark]} won against {self.player[loser_mark]}.")

    def check_status(self):
        self.grid.check_columns()
        self.grid.check_rows()
        self.grid.check_diagonals()
        if self.grid.status:
            self.play = False
            self.congratulate_winner()
            return
        self.grid.check_if_full()
        if self.grid.is_full:
            self.play = False
            self.say_draw()

    @staticmethod
    def switch_player(current_mark):
        if current_mark == "X":
            return "O"
        return "X"

    def play_match(self):
        self.grid.reset_grid()
        self.play = True
        self.grid.print_guide()
        current_mark = "X"
        while self.play:
            cell_number = self.get_cell_number(self.player[current_mark])
            self.grid.update_cell(cell_number, current_mark)
            self.grid.print_grid()
            self.check_status()
            current_mark = TicTacToe.switch_player(current_mark)

    def play_again(self):
        while True:
            play_again = input("Play again? (y/n): ").lower()
            if play_again not in ("y", "n"):
                print("Please enter a y or n.")
                continue
            if play_again == "y":
                self.match_up = True
            else:
                self.match_up = False
            return

    def gameplay(self):
        self.get_players()
        self.match_up = True
        while self.match_up:
            self.play_match()
            self.play_again()

    def thank_players(self):
        print("Thank you for playing!")

    def exit(self):
        while True:
            exit = input("Go back to main menu? (y/n): ").lower()
            if exit not in ("y", "n"):
                print("Please enter a y or n.")
                continue
            if exit == "n":
                self.thank_players()
                self.run_game = False
            else:
                self.run_game = True
            return   

def main():
    tictactoe = TicTacToe()
    while tictactoe.run_game:
        tictactoe.gameplay()
        tictactoe.exit()

if __name__ == "__main__":
    main()