# sys enables use of CLI arguments
import sys
READ_MODE = "r"

def main() -> None:
    file_name = check_args()
    print(file_name)                                              # temp line - REMOVE in final submission
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


def validate_content(game_file):
    """ Check file contents for invalid inputs / dimensions """
    
    # Identify non-digit values
    content = game_file.read()
    file_values = []
    try:
        # Create list of integer values removing space separation
        file_values = [int(value) for value in content.split()]  
       
    except:
        print("8") # Non-digit value encountered
        exit()
    
    # Check for valid integers
    for value in file_values:
        if value <= 0:
            print("8")  # Negative or zero value encountered
            exit()
    
    # Check game initialser row
    setup_line = content.split('\n', 1)[0]  # read 1st line of file
    setup_values = setup_line.split()       # convert space-separated string to a list
    
    # Invalid number of dimension values in file to initialize game
    if len(setup_values) != 3:
        print("8")
        exit()

    # Impossible game as insufficient columns / rows to meet win requirement
    elif setup_values[2] > setup_values[0] or setup_values[2] > setup_values[1]:
        print("7")
        exit()


def read_file(file_name):
    """ Read file and check format conforms """
    try:
        game_file = open(file_name, READ_MODE)

        """ check correct file type """
        file_ext = file_name.split('.')[1]
        if file_ext != "txt":
            print("9") # Invalid file type provided
            exit()

        validate_content(game_file) 

        game_file.close()

    except FileNotFoundError:
        print("9") # File not found
        exit()


if __name__ == '__main__':
    main()
