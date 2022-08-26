from TicTacToe import TicTacToe

game = TicTacToe()
print(game.game_instructions)
print("\n\n")
still_playing = True

while still_playing:
    while not game.game_over:
        incorrect_input = True
        while incorrect_input:
            turn_str = input(f"{game.current_player}: Select a tile to play: ")

            try:
                turn = int(turn_str)
            except ValueError:
                print(f"{turn_str} is not a valid integer. Please try again.")
                continue
            else:
                if turn < 1 or turn > 9:
                    print(f"Please select a number between 1 and 9")
                    continue

                elif game.game_plays[turn - 1] == "X" or game.game_plays[turn - 1] == "O":
                    print(f"Tile {turn} has already been played. Please select a different tile.")
                    continue
                else:
                    incorrect_input = False

        game.add_game_piece(turn - 1)
        print(game.game_board)
        print("\n\n")

    wants_to_play_again = False
    valid_answer = False
    while not valid_answer:
        play_again = input("Would you like to play again? (y/n) ")
        if play_again.lower() == "y":
            valid_answer = True
            game.reset_board()
            print(game.game_instructions)
        elif play_again.lower() == "n":
            valid_answer = True
            still_playing = False
        else:
            print("Not a valid answer. Please type 'y' for yes or 'n' for no.")