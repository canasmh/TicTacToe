class TicTacToe:

    def __init__(self):
        self.turns = 0
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


if __name__ == "__main__":

    game = TicTacToe()
    print(game.game_instructions)
    print(game.game_board)
