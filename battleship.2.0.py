# Battle ship 1.3 stage: Nate S and Trusha

import random

def create_board():
    board = []
    board.append(" ")
    for num in range(grid_size):
        board.append(num+1)
    
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
            randomList = random.randint(grid_size + 1, grid_size + grid_size)
            randomSpot = random.randint(1, grid_size)
            if grid[randomList][randomSpot] != " ":
                continue
            else:
                grid[randomList][randomSpot] = 1
                shipNumber += 1
                continue
        elif shipNumber == 2:
            randomList = random.randint(grid_size + 1, grid_size + grid_size)
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
    if ship_counter == 0:
        WinCheck = True

    elif grid[row][column] == " ":
        shown_grid[row][column] = "X"

        print("Missed")
        print(f"There are {ship_counter_player} ships on the board.")
        
    elif grid[row][column] == 1:
        if player_turns == True:
            shown_grid[row][column] = "C"
            print("\nCorrect. You sunk a dingy")
        else:
            shown_grid[row][column] = "C"
            print("Computer sunk a dingy")
        ship_counter -= 1
        print(f"There are {ship_counter} ships on the board.")
        
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
            shown_grid[row][column] = "C"
            if destroyer == 0:
                print("Computer sunk the dingy ")
                ship_counter -= 1
            else:
                print("Computer partially hit a dingy")

        print(f"There are {ship_counter} ships on the board.")

    return WinCheck, destroyer, ship_counter

def coordinate(user_guesses_list):
    check = True
    while check:
        user_guess = input("Please enter your guess (A,1): ")

        if len(user_guess) < 3 or int(user_guess[2]) == 0:
            print("Please enter a valid guess")
            continue
        try:
            if user_guess[1] == ",":
                if user_guess not in user_guesses_list:
                    let = user_guess.split(",")
                    for letters in range(grid_size):
                        check_let = chr(64 + (letters + 1))
                        if check_let == let[0]:
                            check = False
                            break
                        else:
                            check = True
                    if check == True:
                        print("Please enter a valid guess")
                        continue
                    else:
                        for num in range(grid_size+1):
                            if int(let[1]) == num:
                                user_guesses_list.append(user_guess)
                                check = False
                                break
                            else:
                                check = True 
                else:
                    print("Please enter a valid guess.")
            else:
                print("Please enter a valid guess.")
        except:
            print("Please enter a valid guess.")
    return let

if __name__ == "__main__":
    user_guesses_list = []
    num_ships = 2
    ship_counter_player = num_ships
    destroyer_player = 2
    ship_counter_computer = num_ships
    destroyer_computer = 2
    player_turn = True

    while True:
        try:
            grid_size = int(input("How big do you want your grid (must be between 4 to 10.): "))
            if grid_size >= 4 or grid_size <= 10:
                break
            else:
                print("Please enter a valid input.")
        except:
            print("Please enter a valid input.")

    # create boards
    player_grid = create_board()
    comp_grid = create_board()
    comp_hidden_grid = create_board()

    Ship_placement(player_grid)
    print(player_grid)
    Ship_placement(comp_grid)
    print(comp_grid)
    print(f"There are {num_ships} ships on the board.")
    print("If you hit a ship an C will be on the board, otherwise it will be an X.")
    while True:
        print("\nPlayer Board:")
        i = 0
        first_row = ""
        for row in player_grid:
            number = str(row) + " "
            first_row += number
            if i == grid_size:
                print(first_row)
            if i > grid_size:
                print(*row)
            i += 1
        print("\nComputers Board")
        i = 0
        first_row = ""
        for row in comp_hidden_grid:
            number = str(row) + " "
            first_row += number
            if i == grid_size:
                print(first_row)
            if i > grid_size:
                print(*row)
            i += 1

        
        print("\nPlayers turn: ")

        let = coordinate(user_guesses_list)
        
        order_row = 0
        column = int(let[1])
        print(column)
        
        for specific_letter in range(grid_size):
            row_let = chr(64 + (specific_letter + 1))
            order_row += 1
            if let[0] == row_let:
                rowindex = order_row + grid_size

        winCheck, destroyer_player, ship_counter_player = win_check(comp_grid, comp_hidden_grid, rowindex, column, player_turn, ship_counter_player, destroyer_player)
        if ship_counter_player == 0:

            print("\nPlayer Board:")
            i = 0
            first_row = ""
            for row in player_grid:
                number = str(row) + " "
                first_row += number
                if i == grid_size:
                    print(first_row)
                if i > grid_size:
                    print(*row)
                i += 1
            print("\nComputers Board")
            i = 0
            first_row = ""
            for row in comp_hidden_grid:
                number = str(row) + " "
                first_row += number
                if i == grid_size:
                    print(first_row)
                if i > grid_size:
                    print(*row)
                i += 1

            print("Player Wins! All computer ships hit! You won!")
            print(" ")
            break
        else:
            player_turn = False

        if player_turn == False:
            print("\nComputer's turn: ")
            while True:
                comp_guess_list = random.randint(1 + grid_size, grid_size + grid_size)
                comp_guess_spot = random.randint(1, grid_size)
                letter_order = 0
                for letter in range(grid_size):
                    row_lets = chr(64 + (letter + 1))
                    letter_order += 1
                    if comp_guess_list == letter_order:
                        comp_guess_letter = row_lets
                        break
                if player_grid[comp_guess_list][comp_guess_spot] ==  " " or player_grid[comp_guess_list][comp_guess_spot] == 1 or player_grid[comp_guess_list][comp_guess_spot] == 2:
                    break
            winCheck, destroyer_computer, ship_counter_computer = win_check(player_grid, player_grid, comp_guess_list, comp_guess_spot, player_turn, ship_counter_computer, destroyer_computer)

            if ship_counter_computer == 0:

                print("\nPlayer Board:")
                for row in player_grid:
                    print(*row)
                print("\nComputers Board")
                for row in comp_hidden_grid:
                    print(*row)

                print("Computer won! Computer hit all player ships!")
                print(" ")

                break
            else:
                player_turn = True
