# Battle ship 2.2 stage: Nate S and Trusha

import random

def create_board(grid_size):
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

def dictionary():
    fleet = {
        "carrier": [],
        "battleship": [],
        "cruiser": [],
        "submarine": [],
        "destroyer": []
    }
    return fleet

def Ship_placement(grid, grid_size, fleet):
    shipNumber = 1
    while True:
        if shipNumber == 5:
            break
        randomList = random.randint(grid_size + 1, grid_size + grid_size)
        randomSpot = random.randint(1, grid_size)
        if grid[randomList][randomSpot] != " ":
            continue
        else:
            randomDirection = random.randint(1, 4)
            # 1 = down
            if randomDirection == 1:
                for SpotAddCheck in range(shipNumber):
                    try:
                        if grid[randomList - (SpotAddCheck + 1)][randomSpot] != " ":
                            CoordCheck = False
                            break
                        else:
                            CoordCheck = True
                    except:
                        CoordCheck = False
                        break
                if CoordCheck == True:
                    grid[randomList][randomSpot] = 1
                    for SpotAdd in range(shipNumber):
                        grid[randomList - (SpotAdd + 1)][randomSpot] = 1
                    shipNumber += 1
                else:
                    continue
            # 2 = up
            if randomDirection == 2:
                for SpotAddCheck in range(shipNumber):
                    try:
                        if grid[randomList + (SpotAddCheck + 1)][randomSpot] != " ":
                            CoordCheck = False
                            break
                        else:
                            CoordCheck = True
                    except:
                        CoordCheck = False
                        break
                if CoordCheck == True:
                    grid[randomList][randomSpot] = 1
                    for SpotAdd in range(shipNumber):
                        grid[randomList + (SpotAdd + 1)][randomSpot] = 1
                    shipNumber += 1
                else:
                    continue
                
            # 3 = right
            if randomDirection == 3:
                for SpotAddCheck in range(shipNumber):
                    try:
                        if grid[randomList][randomSpot + (SpotAdd + 1)] != " ":
                            CoordCheck = False
                            break
                        else:
                            CoordCheck = True
                    except:
                        CoordCheck = False
                        break
                if CoordCheck == True:
                    grid[randomList][randomSpot] = 1
                    for SpotAdd in range(shipNumber):
                        grid[randomList][randomSpot + (SpotAdd + 1)] = 1
                    shipNumber += 1
                else:
                    continue
            # 4 = left
            if randomDirection == 4:
                for SpotAddCheck in range(shipNumber):
                    try:
                        if grid[randomList][randomSpot + (SpotAdd + 1)] != " ":
                            CoordCheck = False
                            break
                        else:
                            CoordCheck = True
                    except:
                        CoordCheck = False
                        break
                if CoordCheck == True:
                    grid[randomList][randomSpot] = 1
                    for SpotAdd in range(shipNumber):
                        grid[randomList][randomSpot + (SpotAdd + 1)] = 1
                    shipNumber += 1
                else:
                    continue

def win_check(grid, shown_grid, row, column, player_turns, ship_counter, destroyer, fleet):
    WinCheck = False
    if ship_counter == 0:
        WinCheck = True

    elif grid[row][column] == " ":
        shown_grid[row][column] = "X"

        print("Missed")
        print(f"There are {ship_counter} ships on the board.")
        
    elif fleet["destroyer"] == [row][column] == 2:
        
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

def coordinate(grid_size, player_grid, comp_hidden_grid):
    check = True
    while check:
        user_guess = input("Please enter your guess (A,1): ")
        let = user_guess.split(",")
        if len(user_guess) < 3 or int(user_guess[2]) == 0 or user_guess[1] != ",":
            print("Please enter a valid guess")
            continue
        try:
            check_let = ord(let[0])
            check_let -= 64
            check_let += grid_size
            if comp_hidden_grid[check_let][int(let[1])] == " " or comp_hidden_grid[check_let][int(let[1])] == 1 or comp_hidden_grid[check_let][int(let[1])] == 2:
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
                            check = False
                            break
                        else:
                            check = True 
            else:
                print("Please enter a valid guess.")
        except:
            print("Please enter a valid guess.")

    while True:
        grid = grid_size + grid_size
        comp_guess_list = random.randint(1 + grid_size, grid)
        comp_guess_spot = random.randint(1, grid_size)
        letter_order = grid_size
        for letter in range(grid):
            row_lets = chr(64 + (letter + 1))
            letter_order += 1 
            if comp_guess_list == letter_order:
                comp_guess_letter = row_lets
                break
        if player_grid[comp_guess_list][comp_guess_spot] ==  " " or player_grid[comp_guess_list][comp_guess_spot] == 1 or player_grid[comp_guess_list][comp_guess_spot] == 2:
            break
    return let, comp_guess_letter, comp_guess_list, comp_guess_spot

if __name__ == "__main__":
    num_ships = 5
    ship_counter_player = num_ships
    destroyer_player = 2
    ship_counter_computer = num_ships
    destroyer_computer = 2
    player_turn = True
    grid_size = 10

    # create boards
    player_grid = create_board(grid_size)
    comp_grid = create_board(grid_size)
    comp_hidden_grid = create_board(grid_size)

    player_fleet = dictionary()
    computer_fleet = dictionary()
    
    Ship_placement(player_grid, grid_size, player_fleet)
    Ship_placement(comp_grid, grid_size, computer_fleet)

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
        let , comp_guess_letter, comp_guess_list, comp_guess_spot = coordinate(grid_size, player_grid, comp_hidden_grid)
        order_row = 0
        column = int(let[1])
        
        for specific_letter in range(grid_size):
            row_let = chr(64 + (specific_letter + 1))
            order_row += 1
            if let[0] == row_let:
                rowindex = order_row + grid_size

        winCheck, destroyer_player, ship_counter_player = win_check(comp_grid, comp_hidden_grid, rowindex, column, player_turn, ship_counter_player, destroyer_player, player_fleet)

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
            print(f"Computer choose coordinate {comp_guess_letter}{comp_guess_spot}")
            winCheck, destroyer_computer, ship_counter_computer = win_check(player_grid, player_grid, comp_guess_list, comp_guess_spot, player_turn, ship_counter_computer, destroyer_computer, computer_fleet)

            if ship_counter_computer == 0:
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

                print("Computer won! Computer hit all player ships!")
                print(" ")
                break
            else:
                player_turn = True