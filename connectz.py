# sys enables use of CLI arguments
import sys


def main() -> None:
    file_name = check_args()
    print(file_name)                                                                # temp line - REMOVE in final submission
    read_file(file_name)


def check_args():
    """ Check number of arguments provided in CLI  """
    if len(sys.argv) != 2:
        print("connectz.py: Provide one input file") # Incorrect number of arguments provided
        exit()
    else:
        """ Return filename if check passed """
        file_name = sys.argv[1]
        print(f"args check passed filename = {file_name}")                          # temp line - REMOVE in final submission
        return file_name


def check_dimensions(game_file):
    """ Check if first line contains three integer values """
    setup = game_file.readline() # read 1st line of file
    print(setup)                                                                    # temp line - REMOVE in final submission
    setup_list = setup.split() # convert space-separated string to a list
    if not (all([value.isdigit() for value in setup_list])):
        print("8") # Non-digit values found
        exit()
    elif len(setup_list) != 3:
        print("8") # Invalid number of dimension values in file
    elif setup_list[2] > setup_list[0] or setup_list[2] > setup_list[1]:
        print("7") # Impossible game as insufficient columns / rows to meet win requirement
    print(setup_list)                                                               # temp line - REMOVE in final submission


def read_file(file_name):
    """ Read file and check format conforms """
    try:
        game_file = open(file_name, "r")

        """ check correct file type """
        file_ext = file_name.split('.')[1]
        if file_ext != "txt":
            print("8") # Invalid file type provided
            exit()

        check_dimensions(game_file) 

        game_file.close()

    except FileNotFoundError:
        print("9") # File not found
        exit()


if __name__ == '__main__':
    main()
