# sys enables use of CLI arguments
import sys
print(sys.argv)


def main() -> None:
    check_args()

def check_args():
    """ Check correct number of arguments provided in CLI  """
    if len(sys.argv) != 2:
        print("connectz.py: Provide one input file")
        exit()
    else:
        print("args check passed")


if __name__ == '__main__':
    main()
