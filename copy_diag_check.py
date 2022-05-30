# copy retained with print statements in case development required

# Check Player B diagonal
    row_counter_B = 1
    diag_streak = 0

    # Search row
    for x in range(max_rows):
        row_search_term = "Y" + str(row_counter_B)
        print(f"row_search_term start of loop{row_search_term}")
        row_slice_B = [val for val in player_B_moves if row_search_term in val]
        print(f"row slice B start of loop{row_slice_B}")
        
        col_counter_B = 1   # Reset col counter inside loop to always start new row search from first col 
        direction = "right" # Reset diagonal direction 
        # Search only proceeds if moves in row
        if len(row_slice_B) !=0:
            print(f"row slice B found = {row_slice_B}")
            # Search for player cols within given row 
            for y in range(max_cols):
                col_search_term = "X" + str(col_counter_B)
                print(f"col_search_term start of col loop {col_search_term}")
                col_in_row_slice_B = [val for val in row_slice_B if col_search_term in val]
                print(f"col_in_row_slice_B ANY {col_in_row_slice_B}")
                # Search only proceeds if cols in row
                if len(col_in_row_slice_B) != 0:
                    diag_streak += 1
                    print(f"diag streak 1 = {diag_streak}") 
                    print(f"col_in_row_slice_B Match Found {col_in_row_slice_B}")
                    # While loop will continue whilst match in diagonal position (diag streak) and space remains to win
                    print(f"current streak {diag_streak}")
                    print(f"win moves needed {target - diag_streak}")
                    print(f"current row A {row_counter_B}")
                    print(f"row space remaining {max_rows - row_counter_B}")
                    next_row_counter_B = row_counter_B #Reset to start new while loops from same row 
                    
                    while diag_streak != 0 and (target - diag_streak) <= (max_rows - row_counter_B):
                        
                        if direction == "left" and diag_streak == 1:
                            next_row_counter_B = row_counter_B + 1 # if first try for left direction start on 1st next row
                        else:
                            next_row_counter_B +=1 # Otherwise iterate from previous loop

                        print("start of while loop") 
                        print(f"next row counter A {next_row_counter_B}")
                        next_row_search_term = "Y" + str(next_row_counter_B)
                        print(f"next_row_search_term {next_row_search_term}")
                        next_row_slice_B = [val for val in player_B_moves if next_row_search_term in val]
                        print(f"next row slice A {next_row_slice_B}")
                        # only proceed if a match in next row
                        if len(next_row_slice_B) !=0:
                            # move to next col within next row (i.e. diagonal from start of while loop)
                            print(f"searching for col in next row {direction}")
                            if direction == "right":
                                next_col_counter_B = col_counter_B +1
                            elif direction == "left":
                                next_col_counter_B = col_counter_B -1

                            next_col_search_term = "X" + str(next_col_counter_B)
                            print(f"next_col_search_term {next_col_search_term}")
                            next_col_in_next_row_slice_B = [val for val in next_row_slice_B if next_col_search_term in val]
                            print(f"next_col_in_next_row_slice_B ANY {next_col_in_next_row_slice_B}")
                            # diagonal match found, increase streak
                            if len(next_col_in_next_row_slice_B) !=0:
                                diag_streak +=1
                                print(f"diag streak 1+ = {diag_streak}")
                                if direction == "right":
                                    col_counter_B += 1
                                if direction == "left":
                                    col_counter_B -= 1
                                # check if diagonal streak meets win requirement, check if last move
                                if diag_streak == target:
                                    print("checking player 1 win")
                                    player="B"
                                    last_move = next_col_in_next_row_slice_B[0]
                                    check_last_move(player, last_move, last_move_id)
                                # if match found but not win reverts to start of while loop
                            
                             # if no col match for right search switch direction and remain in while loop
                             # and diag_streak is 1 to prevent zig zag matches
                            elif direction == "right" and diag_streak == 1:
                                print("switching to left search")
                                direction = "left"
                            
                            # if no col match for left search or right search was on streak, reset diag streak and exit while loop
                            else:
                                diag_streak = 0 
                                print(f"diag streak reset = {diag_streak}")
                        
                        # if no col match for right search switch direction and remain in while loop
                        elif direction == "right":
                            direction = "left"
                        
                        # no match in next row, reset diag streak and exit while loop
                        else:
                            diag_streak = 0
                            direction = "right"
                            print(f"diag streak reset = {diag_streak}")
                
                # no col match in first row        
                else:
                    print(f"NO col_in_row_slice_B No Match Found {col_in_row_slice_B}")
                    diag_streak = 0
                    col_counter_B+=1 # col not found in row, loop on next col (within same row)
        
        # no match found in first row
        else:
            print("match not found in row")
            row_counter_B += 1 # no player matches in row slice move to next row