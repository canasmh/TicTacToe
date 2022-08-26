class TicTacToe:

    def __init__(self):
        self.turns = 0
        self.game_over = False
        self.current_player = "Player 1"
        self.current_piece = "X"
        self.game_plays = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.game_board = \
            f"""
             {self.game_plays[0]} | {self.game_plays[1]} | {self.game_plays[2]}
            -----------
             {self.game_plays[3]} | {self.game_plays[4]} | {self.game_plays[5]}
            -----------
             {self.game_plays[6]} | {self.game_plays[7]} | {self.game_plays[8]}"""

        self.game_instructions = \
            f"""
            Welcome to the game of Tic Tac Toe!
            
            Instructions are simple. Fill a row, column, or diagonal with your symbol ('X' or 'O') to win!
            
            The board is laid out in the following manner:\n\n 
            {self.game_board}"""

    def add_game_piece(self, index):
        game_plays = self.game_plays
        game_plays[index] = self.current_piece
        self.game_plays = game_plays
        self.game_board = \
            f"""
                     {self.game_plays[0]} | {self.game_plays[1]} | {self.game_plays[2]}
                    -----------
                     {self.game_plays[3]} | {self.game_plays[4]} | {self.game_plays[5]}
                    -----------
                     {self.game_plays[6]} | {self.game_plays[7]} | {self.game_plays[8]}"""
        # self.game_plays[index] = self.current_piece
        print(f"Game_Plays: {game_plays}")
        self.check_if_game_won()

        if not self.game_over:
            self.turns += 1
            self.update_player()

    def update_player(self):
        if self.turns % 2 == 0:
            self.current_player = "Player 1"
            self.current_piece = "X"
        else:
            self.current_player = "Player 2"
            self.current_piece = "O"

    def check_if_game_won(self):
        game_plays = self.game_plays
        print("\n\n")
        if game_plays[0] == game_plays[1] == game_plays[2]:
            print(f"Congratulations {self.current_player}, you won!")
            self.game_over = True
        elif game_plays[3] == game_plays[4] == game_plays[5]:
            print(f"Congratulations {self.current_player}, you won!")
            self.game_over = True
        elif game_plays[6] == game_plays[7] == game_plays[8]:
            print(f"Congratulations {self.current_player}, you won!")
            self.game_over = True
        elif game_plays[0] == game_plays[3] == game_plays[6]:
            print(f"Congratulations {self.current_player}, you won!")
            self.game_over = True
        elif game_plays[1] == game_plays[4] == game_plays[7]:
            print(f"Congratulations {self.current_player}, you won!")
            self.game_over = True
        elif game_plays[2] == game_plays[5] == game_plays[8]:
            print(f"Congratulations {self.current_player}, you won!")
            self.game_over = True
        elif game_plays[0] == game_plays[4] == game_plays[8]:
            print(f"Congratulations {self.current_player}, you won!")
            self.game_over = True
        elif game_plays[2] == game_plays[4] == game_plays[6]:
            print(f"Congratulations {self.current_player}, you won!")
            self.game_over = True
        elif self.turns == len(self.game_plays) - 1:
            print("Looks like its a draw!")
            self.game_over = True

    def reset_board(self):
        self.turns = 0
        self.game_over = False
        self.current_player = "Player 1"
        self.current_piece = "X"
        self.game_plays = [1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == "__main__":

    game = TicTacToe()
    print(game.game_instructions)
