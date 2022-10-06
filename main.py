main_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
available_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_board(board):
    vertical_line = '|'
    horizontal_lines = '-----------'

    tictactoe_schema = \
        ' ' + board[0] + ' ' + vertical_line + ' ' + board[1] + ' ' + vertical_line + ' ' + board[2] + ' ' + '\n' \
        + horizontal_lines + '\n' \
        + ' ' + board[3] + ' ' + vertical_line + ' ' + board[4] + ' ' + vertical_line + ' ' + board[5] + ' ' + '\n' \
        + horizontal_lines + '\n' \
        + ' ' + board[6] + ' ' + vertical_line + ' ' + board[7] + ' ' + vertical_line + ' ' + board[8] + ' ' + '\n'

    print(tictactoe_schema)

def reset_game():
    global available_nums
    global main_board
    available_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    main_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def start_game():
    start_game_str = 'Do you want to start a new game of TicTacToe? (Y/N): '

    start_new_game_response = ''

    while not start_new_game_response == 'Y' and not start_new_game_response == 'N':

        print('Please answer with a Y for yes or a N for no')

        start_new_game_response = input(start_game_str)

        if start_new_game_response == 'Y':
            reset_game()
            ask_player_for_input(1)
        elif start_new_game_response == 'N':
            print("See you again next time!")

def replace_number_picked_with_XorO(player_input_str, player_num):
    num_index = main_board.index(player_input_str)
    if player_num == 1:
        main_board[num_index] = 'X'
    else:
        main_board[num_index] = 'O'

def check_if_player_wins():
    win_combination_1 = main_board[0] == main_board[1] == main_board[2]
    win_combination_2 = main_board[3] == main_board[4] == main_board[5]
    win_combination_3 = main_board[6] == main_board[7] == main_board[8]
    win_combination_4 = main_board[0] == main_board[3] == main_board[6]
    win_combination_5 = main_board[1] == main_board[4] == main_board[7]
    win_combination_6 = main_board[2] == main_board[5] == main_board[8]
    win_combination_7 = main_board[0] == main_board[4] == main_board[8]
    win_combination_8 = main_board[2] == main_board[4] == main_board[6]

    if win_combination_1 or win_combination_2 or win_combination_3 or win_combination_4 or win_combination_5 or \
            win_combination_6 or win_combination_7 or win_combination_8:
        return True
    else:
        return False

def check_if_draw():

    if len(available_nums) == 0:
        return True
    else:
        return False

def ask_player_for_input(player_num):
    player1_plays_str = "Player's 1 turn. Type in which number bracket you want to put an X: "
    player2_plays_str = "Player's 2 turn. Type in which number bracket you want to put an O: "
    player_input = 0
    player_input_str = ''

    print_board(main_board)

    while player_input not in available_nums:
        player_input_str = input(player1_plays_str if player_num == 1 else player2_plays_str)

        if player_input_str.isdigit():
            player_input = int(player_input_str)

            if player_input in available_nums:
                print(f'The number you chose was: {player_input}')
                available_nums.remove(player_input)
                replace_number_picked_with_XorO(player_input_str, player_num)
                if check_if_player_wins():
                    print_board(main_board)
                    print(f'Congratulations! Player {player_num} wins!')
                    start_game()
                elif check_if_draw():
                    print_board(main_board)
                    print(f'This game is a draw!')
                    start_game()
                else:
                    ask_player_for_input(2 if player_num == 1 else 1)
            else:
                print("Please provide a valid number!")

        else:
            print("Please provide a number!")

    return player_input


start_game()