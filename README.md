## Output Specifications:

| Code | Reason | Description | Additional Checks / Notes | Status | Function Covering Requirement |
| ---- | ------ | ----------- | ------------------------- | ------ | ----------------------------- |
| 0 | Draw | This happens when every possible space in the frame was filled with a counter, but neither player achieved a line of the required length. | - | Not Started | - |
| 1 | Win for player 1 | The first player achieved a line of the required length. | - | Not Started | - |
| 2 | Win for player 2 | The second player achieved a line of the required length. | - | Not Started | - |
| 3 | Incomplete | The file conforms to the format and contains only legal moves, but the game is neither won nor drawn by either player and there are remaining available moves in the frame. Note that a file with only a dimensions line constitues an incomplete game. | - | Not Started | - |
| 4 | Illegal continue | All moves are valid in all other respects but the game has already been won on a previous turn so continued play is considered an illegal move. | - | Not Started | - |
| 5 | Illegal row | The file conforms to the format and all moves are for legal columns but the move is for a column that is already full due to previous moves. | - | Not Started | - |
| 6 | Illegal column | The file conforms to the format but contains a move for a column that is out side the dimensions of the board. i.e. the column selected is greater than X | - | Not Started | - |
| 7 | Illegal game | The file conforms to the format but the dimensions describe a game that can never be won. | Min win exceeds column and row dimensions | :white_check_mark: |  validate_content |
| 8 | Invalid file | The file is opened but does not conform to the format. |<ul><li>Non-digit values</li><li>Attempt to initialise game without 3 values</li><li>3</li><li>4</li></ul>  | :white_check_mark: |  validate_content |
| 9 | File error | The file can not be found, opened or read for some reason. | <ul><li>File not found</li><li>File type is not .txt type</li></ul>| :white_check_mark: | read_file |
| connectz.py: Provide one input file | Invalid arguments | If the game is run with no arguments or more than one argument it should print as a single line to standard out. | - | :white_check_mark: | check_args |


## Acknowledgements:
    Pass arguments from CLI: https://www.youtube.com/watch?v=Y4A_0tCe8ik
