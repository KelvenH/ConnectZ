import sys # sys enables use of CLI arguments


READ_MODE = "r"

def main() -> None:
    
    file_name = check_args()
    read_file(file_name)


def check_args():
    """ Check number of arguments provided in CLI  """
    if len(sys.argv) != 2:
        print("connectz.py: Provide one input file")   # Incorrect number of arguments provided
        exit()
    else:
        """ Return filename if check passed """
        file_name = sys.argv[1]
        print(f"args check passed filename = {file_name}")         # temp line - REMOVE in final submission
        return file_name


def read_file(file_name):
    """ Read file and check format conforms """
    file_values = [8,8,8]
    print(f"file values A: {file_values}")
    try:
        game_file = open(file_name, READ_MODE)

        file_values = validate_content(game_file)
        
        print(f"file values C: {file_values}")
        build_game(file_values)
        game_file.close()

    except FileNotFoundError:
        print("9") # File not found
        exit()


def validate_content(game_file):
    """ Check file contents for invalid inputs / dimensions """
    
    # Identify non-digit values
    content = game_file.read()
    
    try:
        # Create list of integer values removing space separation
        file_values = [int(value) for value in content.split()]  
        print(f"file values B: {file_values}")
        return (file_values)
    
    except:
        print("8") # Non-digit value encountered
        exit()
    

def build_game(file_values):

    print(f"file values D: {file_values}")



if __name__ == '__main__':
    main()
