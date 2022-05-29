import sys # sys enables use of CLI arguments


READ_MODE = "r"

def main() -> None:
    
    file_name = check_args()                                        # validate CLI inputs and return file name
    game_inputs = read_file(file_name)                              # validate file content and return game data
    game_grid, cols, rows, target = build_game(game_inputs)         # check for invalid games & populate 'grid ref' view of game
    player_A_moves, player_B_moves = create_player_moves(game_grid) # create seperate player moves
    # check results & determine win/draw outcomes
    check_row_win(player_A_moves, player_B_moves, rows)                    
    # clear lists for next game                                     # clear lists to ensure not impairing subsequent runs


def check_args():
    """ Check number of arguments provided in CLI  """
    if len(sys.argv) != 2:
        print("connectz.py: Provide one input file")   # Incorrect number of arguments provided
        exit()
    else:
        """ Return filename if check passed """
        file_name = sys.argv[1]
        # print(f"args check passed filename = {file_name}")        
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
    setup_values = setup_line.split()       # convert space-separated string to a list
    
    # Invalid number of dimension values in file to initialize game
    if len(setup_values) != 3:
        print(8)
        exit()
    
    try:
        # Create list of integer values removing space separation
        file_values = [int(value) for value in content.split()]  
    
    except ValueError:
        print(8) # Non-digit value encountered
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
    del game_inputs[0:3]        # remove game dimension values retaining only player moves
    
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
    
    print(game_grid)
    return (game_grid, cols, rows, target)


def create_player_moves(game_grid):
    print(game_grid)
    
    # extract player A moves
    player_A = "A"
    player_A_moves = [move for move in game_grid if player_A in move]
    print(player_A_moves)

    # extract player B moves
    player_B = "B"
    player_B_moves = [move for move in game_grid if player_B in move]
    print(player_B_moves)

    return (player_A_moves, player_B_moves)


def check_row_win(player_A_moves, player_B_moves, rows):
    print(player_A_moves)
    print(player_B_moves)
    max_rows = rows
    row_counter = 1
    for x in range(max_rows):
        print(row_counter)
        row_counter += 1
        #search_term = "Y" + str(row_counter) 
        #print(search_term)


if __name__ == '__main__':
    main()
