import sys # sys enables use of CLI arguments


READ_MODE = "r"


def main() -> None:
    
    file_name = check_args()                                        # validate CLI inputs and return file name
    game_inputs = read_file(file_name)                              # validate file content and return game data
    game_grid, cols, rows, target, last_move_id = build_game(game_inputs) # check for invalid games & populate 'grid ref' view of game
    player_A_moves, player_B_moves = create_player_moves(game_grid) # create seperate player moves
    # check results & determine win/draw outcomes
    check_row_win(player_A_moves, player_B_moves, rows, target, last_move_id)                    
   

def check_args():
    """ Check number of arguments provided in CLI  """
    if len(sys.argv) != 2:
        print("connectz.py: Provide one input file")   # Incorrect number of arguments provided
        exit()
    
    else:
        """ Return filename if check passed """
        file_name = sys.argv[1]
       
        return file_name


def read_file(file_name):
    """ Read file and check format conforms """
    try:
        game_file = open(file_name, READ_MODE)

        """ check correct file type """
        file_ext = file_name.split('.')[1]
        if file_ext != "txt":
            print(9) # Invalid file type provided
            exit()

        valid_inputs = validate_content(game_file)
        game_file.close()

        return valid_inputs

    except FileNotFoundError:
        print(9) # File not found
        exit()


def validate_content(game_file):
    """ Check file contents for invalid inputs / dimensions """
    content = game_file.read()

    # Check game initialser row
    setup_line = content.split('\n', 1)[0]  # read 1st line of file
    
    try:
        setup_values = [int(num) for num in setup_line.split()]       # convert space-separated string to a list of ints
    
    except ValueError:
        print(8) # Non-digit value encountered (in set-up line)
        exit()

    # Invalid number of dimension values in file to initialize game
    if len(setup_values) != 3:
        print(8)
        exit()
    
    try:
        # Create list of integer values removing space separation
        file_values = [int(value) for value in content.split()]  
    
    except ValueError:
        print(8) # Non-digit value encountered (in game moves)
        exit()
    
    # Check for valid integers
    for value in file_values:
        if value <= 0:
            print(8)  # Negative or zero value encountered
            exit()
    
    # Impossible game as insufficient columns / rows to meet win requirement
    if setup_values[2] > setup_values[0] or setup_values[2] > setup_values[1]:
        print(7)
        exit()
    
    return file_values


def build_game(game_inputs):
    """ Obtain game dimensions and generate 'grid-ref' for each player turn """
    cols = game_inputs[0]
    rows = game_inputs[1]
    target = game_inputs[2]
    del game_inputs[0:3]    # remove game dimension values retaining only player moves
    
    game_grid = []
    col_tracker = []              

    for index, turn in enumerate(game_inputs):

        if not index % 2:
            player_id = "A"
        
        else:
            player_id = "B"
        
        # Identify illegal column 
        if turn > cols:
            print(6) # col outside dimensions
            exit()

        # Column identifier
        col = "X"
        turn_col_id = col + str(turn)
        col_tracker.append(turn)    # add to col tracker to identify row

        # Identify illegal row (i.e. column already filled)
        if col_tracker.count(turn) > rows:
            print(5) # row height exceeded
            exit()

        # Row identifier
        row = "Y"
        turn_row_id = row + str(col_tracker.count(turn))

        # Generate turn id and add to game grid
        turn_id = player_id + turn_col_id + turn_row_id
        game_grid.append(turn_id)
    
        # Identify last move of game
        last_move_id = game_grid[-1]

    return (game_grid, cols, rows, target, last_move_id)


def create_player_moves(game_grid):
    """ Split gamegrid into seperate player moves"""
    
    # extract player A moves
    player_A = "A"
    player_A_moves = [move for move in game_grid if player_A in move]

    # extract player B moves
    player_B = "B"
    player_B_moves = [move for move in game_grid if player_B in move]

    return (player_A_moves, player_B_moves)


def check_row_win(player_A_moves, player_B_moves, rows, target, last_move_id):
    """ Check for winning rows within player moves"""
    max_rows = rows

    # Check player A rows
    row_counter_A = 1
    for x in range(max_rows):
        search_term = "Y" + str(row_counter_A)
        row_slice_A = [id for id in player_A_moves if search_term in id]
        row_counter_A += 1
        if len(row_slice_A) >= target:
            player="A"
            last_move = row_slice_A[-1]
            check_last_move(player, last_move, last_move_id)

    # Check player B rows
    row_counter_B = 1
    for x in range(max_rows):
        search_term = "Y" + str(row_counter_B)
        row_slice_B = [id for id in player_B_moves if search_term in id]
        row_counter_B += 1
        if len(row_slice_B) >= target:
            player="B"
            last_move = row_slice_B[-1]
            check_last_move(player, last_move, last_move_id)


def check_last_move(player, last_move, last_move_id):
    """ Check players last move from wining line against last turn played """
    if last_move == last_move_id:

        if player == "A":
            print(1) # Player 1 (A) Win
            exit()

        if player == "B":
            print(2)  # Player 2 (B) Win
            exit()

    else:
        print(4) # Illegal continue
        exit()


if __name__ == '__main__':
    main()
