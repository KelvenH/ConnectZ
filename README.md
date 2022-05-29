## Intro
Game checker program for 'Connect Z' (please refer to supporting docs for full program specifications).

To run;

* save the game file(s) to be checked in the same directory as the connectz.py file 
* Enter the following within the CLI providing only a single filename 
`python connectz.py inputfilename `
* Upon assessing the game file, an outcome code will be presented in the CLI / terminal.
* The Output Specifications table below provides an explanaition of the outcome code.


## Output Specifications:

| Code | Reason | Description | Additional Checks / Notes | Status | Function Covering Requirement |
| ---- | ------ | ----------- | ------------------------- | ------ | ----------------------------- |
| 0 | Draw | This happens when every possible space in the frame was filled with a counter, but neither player achieved a line of the required length. | - | Not Started | - |
| 1 | Win for player 1 | The first player achieved a line of the required length. | <ul><li>Row</li><li>Column</li><li>Diagonal</li></ul> | In Progress (row complete) | <ul><li>check_row_win</li><li>TBC</li><li>TBC</li></ul> |
| 2 | Win for player 2 | The second player achieved a line of the required length. | Per player1 win | In Progress (row complete) | <ul><li>check_row_win</li><li>TBC</li><li>TBC</li></ul> |
| 3 | Incomplete | The file conforms to the format and contains only legal moves, but the game is neither won nor drawn by either player and there are remaining available moves in the frame. Note that a file with only a dimensions line constitues an incomplete game. | - | Not Started | - |
| 4 | Illegal continue | All moves are valid in all other respects but the game has already been won on a previous turn so continued play is considered an illegal move. | - | :white_check_mark: | check_last_move |
| 5 | Illegal row | The file conforms to the format and all moves are for legal columns but the move is for a column that is already full due to previous moves. | - requires tracking of column usage | :white_check_mark: | build_game |
| 6 | Illegal column | The file conforms to the format but contains a move for a column that is out side the dimensions of the board. i.e. the column selected is greater than X | - | :white_check_mark: | build_game |
| 7 | Illegal game | The file conforms to the format but the dimensions describe a game that can never be won. | Min win exceeds column and row dimensions | :white_check_mark: |  validate_content |
| 8 | Invalid file | The file is opened but does not conform to the format. |<ul><li>Non-digit values supplied in file</li><li>Negative or zero values provided</li><li>Attempt to initialise game without 3 values</li></ul>  | :white_check_mark: |  validate_content |
| 9 | File error | The file can not be found, opened or read for some reason. | <ul><li>File not found</li><li>File type is not .txt type</li></ul>| :white_check_mark: | read_file |
| connectz.py: Provide one input file | Invalid arguments | If the game is run with no arguments or more than one argument it should print as a single line to standard out. | - | :white_check_mark: | check_args |


## Bugs:

| Brief Details | Cause | Notes | Status|
| ------------- | ----- | ----- | ----- |
| File with multiple validation errors returned multiple output codes| A check for valid positive values was originally nested within a TRY statement which returned the origianl (expected) error code but also the error code associated with the EXCEPT statement (unexpected) | Lifted this check to sit outside / independent of the TRY statement | RESOLVED |
| Possible performance issue maybe encountered due to re-using read() variable | The 'setup_line' variable effectively makes a copy of the 'content' variable which reads the game file. Although this splits the original variable and only retains the first line there maybe possible performance issues with large data files | Further testing required | OPEN |


## Specific Challenges:

- Taking argument (filename) from CLI & reading content (see acknowledgment below for guidance used)
- Defining approach to assess outcome (turn by turn vs final status) - i.e. factoring in 'illegal continue' as all other requirements can be determined by  assessing after all moves performed.


## Acknowledgements:

    Pass arguments from CLI: https://www.youtube.com/watch?v=Y4A_0tCe8ik
