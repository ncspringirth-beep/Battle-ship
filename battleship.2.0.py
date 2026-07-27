# Battle ship 1.3 stage: Nate S and Trusha

import random

def create_board():
    board = []
    num_list = []
    num_list.append(" ")
    for num in range(grid_size):
        num_list.append(num+1)
    board.append(num_list)
    for rand_row in range(grid_size):    
        row = [f"{chr(64+(rand_row+1))}"]
        for spot in range(grid_size):
            if spot == grid_size:
                break
            else:
                space = " "
                row.append(space)
        board.append(row)
        rand_row += 1
    return board

def Ship_placement(grid):
    shipNumber = 1
    while True:
        if shipNumber == 1:
            randomList = random.randint(1, grid_size)
            randomSpot = random.randint(1, grid_size)
            if grid[randomList][randomSpot] != " ":
                continue
            else:
                grid[randomList][randomSpot] = 1
                shipNumber += 1
                continue
        elif shipNumber == 2:
            randomList = random.randint(1, grid_size)
            randomSpot = random.randint(1, grid_size)
            if grid[randomList][randomSpot] != " ":
                continue
            else:
                randomDirection = random.randint(1, 4)
                # 1 = down
                if randomDirection == 1:
                    try:
                        if grid[randomList - 1][randomSpot] != " ":
                            continue
                        else:
                            grid[randomList][randomSpot] = shipNumber
                            grid[randomList - 1][randomSpot] = shipNumber
                            break
                    except:
                        continue
                # 2 = up
                if randomDirection == 2:
                    try:
                        if grid[randomList + 1][randomSpot] != " ":
                            continue
                        else:
                            grid[randomList][randomSpot] = shipNumber
                            grid[randomList + 1][randomSpot] = shipNumber
                            break
                    except:
                        continue
                # 3 = right
                if randomDirection == 3:
                    try:
                        if grid[randomList][randomSpot + 1] != " ":
                            continue
                        else:
                            grid[randomList][randomSpot] = shipNumber
                            grid[randomList][randomSpot + 1] = shipNumber
                            break
                    except:
                        continue
                # 4 = left
                if randomDirection == 4:
                    try:
                        if grid[randomList][randomSpot - 1] != " ":
                            continue
                        else:
                            grid[randomList][randomSpot] = shipNumber
                            grid[randomList][randomSpot - 1] = shipNumber
                            break
                    except:
                        continue

def win_check(grid, shown_grid, row, column, player_turns, ship_counter, destroyer):
    WinCheck = False
    if player_turns == True:
        print("player turn")
    elif player_turns == False:
        print("computer turn")

    if ship_counter == 0:
        WinCheck = True
        if player_turns == True:
        
            print("player won")
        elif player_turns == False:
            print("computer won")
    elif grid[row][column] == " ":
        if player_turns == True:
            shown_grid[row][column] = "X"
        print("\nMissed")
        print(f"There are {ship_counter_player} ships on the board.")
        print(" ")
        
    elif grid[row][column] == 1:
        if player_turns == True:
            shown_grid[row][column] = "C"
            print("\nCorrect. You sunk a dingy")
        else:
            print("Computer sunk a dingy")
        ship_counter -= 1
        print(f"There are {ship_counter} ships on the board.")
        print(" ")   
        
    elif grid[row][column] == 2:
        
        if player_turns == True:
            destroyer -= 1
            shown_grid[row][column] = "C"
            if destroyer == 0:
                print("\nCorrect. You sunk a destroyer ship!")
                ship_counter -= 1
            else:
                print("\nCorrect. You partially hit a destroyer")
        else:
            destroyer -= 1
            if destroyer == 0:
                print("Computer sunk the dingy ")
                ship_counter -= 1
            else:
                print("Computer partially hit a dingy")

        print(f"There are {ship_counter} ships on the board.")
        print(" ")
    return WinCheck, destroyer, ship_counter

if __name__ == "__main__":
    ship_counter = 2
    user_guesses_list = []
    num_ships = 2

    while True:
        grid_size = int(input("How big do you want your grid (must be between 4 to 10.): "))
        if grid_size >= 4 or grid_size <= 10:
            break
        else:
            print("Please enter a valid input.")

    # create boards
    player_grid = create_board()
    comp_grid = create_board()
    comp_hidden_grid = create_board()

    print("Player Board:")
    for row in player_grid:
        print(*row)
    print("\nComputers Board")
    for row in comp_hidden_grid:
        print(*row)

    Ship_placement(player_grid)
    Ship_placement(comp_grid)
    for row in comp_grid:
        print(*row)
    

    print(f"There are {num_ships} ships on the board.")
    print("If you hit a ship an C will be on the board, otherwise it will be an X.")
    
    ship_counter_player = num_ships
    destroyer_player = 2
    ship_counter_computer = num_ships
    destroyer_computer = 2
    player_turn = True
    
    while True:
        print("Player Board:")
        for row in player_grid:
            print(*row)
        print("\nComputers Board")
        for row in comp_hidden_grid:
            print(*row)
        
        if ship_counter_player == 0:
            print("\nPlayer Wins! All computer ships hit! You won!")
            break
        elif ship_counter_computer == 0:
            print("\nComputer won! Computer hit all player ships!")
            break
        elif player_turn:
            print("\nPlayers turn: ")

            check = True
            while check:
                user_guess = input("Please enter your guess (A,1): ")
                try:
                    if user_guess[1] == ",":
                        if user_guess not in user_guesses_list:
                            let = user_guess.split(",")
                            for letters in range(grid_size):
                                check_let = chr(64 + (letters + 1))
                                if check_let == let[0]:
                                    break
                            for num in range(grid_size):
                                if int(let[1]) == num:
                                    user_guesses_list.append(user_guess)
                                    break
                            break
                    else:
                        print("Please enter a valid guess.")
                except:
                    print("Please enter a valid guess.")
            order_row = 0
            column = int(let[1])
            
            
            for specific_letter in range(grid_size):
                row_let = chr(64 + (specific_letter + 1))
                order_row += 1
                if let[0] == row_let:
                    rowindex = order_row
            winCheck, destroyer_player, ship_counter_player = win_check(comp_grid, comp_hidden_grid, rowindex, column, player_turn, ship_counter_player, destroyer_player)
            if winCheck == True:
                break
            player_turn = False

            if player_turn == False:
                print("\nComputer's turn: ")
                comp_guess_list = random.randint(1, grid_size)
                comp_guess_spot = random.randint(1, grid_size)
                winCheck, destroyer_computer, ship_counter_computer = win_check(player_grid, comp_hidden_grid, comp_guess_list, comp_guess_spot, player_turn, ship_counter_computer, destroyer_computer)
                player_turn = True
                if winCheck == True:
                    break
