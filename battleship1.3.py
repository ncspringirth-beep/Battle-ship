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

if __name__ == "__main__":
    user_guesses_list = []
    num_ships = 2

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

# players ship computer guess 
    shipNumber = 1
    while True:
        if shipNumber == 1:
            randomList = random.randint(1, grid_size)
            randomSpot = random.randint(1, grid_size)
            if player_grid[randomList][randomSpot] != " ":
                continue
            else:
                shipNumber += 1
                player_grid[randomList][randomSpot] = 1
        elif shipNumber == 2:
            randomList = random.randint(1, grid_size)
            randomSpot = random.randint(1, grid_size)
            if player_grid[randomList][randomSpot] != " ":
                continue
            else:
                randomDirection = random.randint(1, 4)
                # 1 = down
                if randomDirection == 1:
                    try:
                        if player_grid[randomList - 1][randomSpot] != " ":
                            continue
                        else:
                            player_grid[randomList][randomSpot] = shipNumber
                            player_grid[randomList - 1][randomSpot] = shipNumber
                            break
                    except:
                        continue
                # 2 = up
                if randomDirection == 2:
                    try:
                        if player_grid[randomList + 1][randomSpot] != " ":
                            continue
                        else:
                            player_grid[randomList][randomSpot] = shipNumber
                            player_grid[randomList + 1][randomSpot] = shipNumber
                            break
                    except:
                        continue
                # 3 = right
                if randomDirection == 3:
                    try:
                        if player_grid[randomList][randomSpot + 1] != " ":
                            continue
                        else:
                            player_grid[randomList][randomSpot] = shipNumber
                            player_grid[randomList][randomSpot + 1] = shipNumber
                            break
                    except:
                        continue
                # 4 = left
                if randomDirection == 4:
                    try:
                        if player_grid[randomList][randomSpot - 1] != " ":
                            continue
                        else:
                            player_grid[randomList][randomSpot] = shipNumber
                            player_grid[randomList][randomSpot - 1] = shipNumber
                            break
                    except:
                        continue
    
    # Computers ship player guess
    shipNumber = 1 
    while True:
        if shipNumber == 1:
            randomList = random.randint(1, grid_size)
            randomSpot = random.randint(1, grid_size)
            if comp_grid[randomList][randomSpot] != " ":
                continue
            else:
                shipNumber += 1
                comp_grid[randomList][randomSpot] = 1
        elif shipNumber == 2:
            randomList = random.randint(1, grid_size)
            randomSpot = random.randint(1, grid_size)
            if comp_grid[randomList][randomSpot] != " ":
                continue
            else:
                randomDirection = random.randint(1, 4)
                # 1 = down
                if randomDirection == 1:
                    try:
                        if comp_grid[randomList - 1][randomSpot] != " ":
                            continue
                        else:
                            comp_grid[randomList][randomSpot] = shipNumber
                            comp_grid[randomList - 1][randomSpot] = shipNumber
                            break
                    except:
                        continue
                # 2 = up
                if randomDirection == 2:
                    try:
                        if comp_grid[randomList + 1][randomSpot] != " ":
                            continue
                        else:
                            comp_grid[randomList][randomSpot] = shipNumber
                            comp_grid[randomList + 1][randomSpot] = shipNumber
                            break
                    except:
                        continue
                # 3 = right
                if randomDirection == 3:
                    try:
                        if comp_grid[randomList][randomSpot + 1] != " ":
                            continue
                        else:
                            comp_grid[randomList][randomSpot] = shipNumber
                            comp_grid[randomList][randomSpot + 1] = shipNumber
                            break
                    except:
                        continue
                # 4 = left
                if randomDirection == 4:
                    try:
                        if comp_grid[randomList][randomSpot - 1] != " ":
                            continue
                        else:
                            comp_grid[randomList][randomSpot] = shipNumber
                            comp_grid[randomList][randomSpot - 1] = shipNumber
                            break
                    except:
                        continue

    print(f"\nThere are {num_ships} ships on the board.")
    print("If you hit a ship an C will be on the board, otherwise it will be an X.")
    
    ship_counter_player = num_ships
    destroyer_player = 2
    ship_counter_computer = num_ships
    destroyer_computer = 2
    player_turn = True

    while True:
        print("\nPlayer Board:")
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
                            number = int(let[1])
                            for letters in range(grid_size+1):
                                check_let = chr(64 + (letters + 1)) 
                                if check_let == let[0]:
                                    break
                            for num in range(grid_size+1):
                                if num != 0:
                                    if number == num:
                                        user_guesses_list.append(user_guess)
                                        check = False
                                        break
                        else:
                            print("Please enter a valid guess.")
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

            if comp_grid[rowindex][column] == " ":
                comp_hidden_grid[rowindex][column] = "X"
                print("\nMissed")
                print(f"There are {ship_counter_player} ships on the board.")
                print(" ")
                player_turn = False
            elif comp_grid[rowindex][column] == 1:
                comp_hidden_grid[rowindex][column] = "C"
                print("\nCorrect. You sunk a dingy")
                ship_counter_player -= 1
                print(f"There are {ship_counter_player} ships on the board.")
                print(" ")   
                player_turn = False
            elif comp_grid[rowindex][column] == 2:
                comp_hidden_grid[rowindex][column] = "C"
                destroyer_player -= 1
                if destroyer_player == 0:
                    print("\nCorrect. You sunk a destroyer ship!")
                    ship_counter_player -= 1
                else:
                    print("\nCorrect. You partially hit a destroyer")
                print(f"There are {ship_counter_player} ships on the board.")
                print(" ")
                player_turn = False

        elif player_turn == False:
            print("\nComputer's turn: ")
            while True:
                comp_guess_list = random.randint(1, grid_size)
                comp_guess_spot = random.randint(1, grid_size)
                if player_grid[comp_guess_list][comp_guess_spot] == " ":
                    player_grid[comp_guess_list][comp_guess_spot] = "X"
                    letter_order = 0
                    for letter in range(grid_size):
                        row_lets = chr(64 + (letter + 1))
                        letter_order += 1
                        if comp_guess_list == letter_order:
                            comp_guess_list = row_lets
                            break
                        
                    print(f"Computer choose coordinate {comp_guess_list}{comp_guess_spot} and missed.")
                    print(" ")
                    player_turn = True
                    break
                elif player_grid[comp_guess_list][comp_guess_spot] == 1:
                    player_grid[comp_guess_list][comp_guess_spot] = "C"
                    print("\n Computer sunk a dingy!")
                    letter_order = 0
                    for letter in range(grid_size):
                        row_lets = chr(64 + (letter + 1))
                        letter_order += 1
                        if comp_guess_list == letter_order:
                            comp_guess_list = row_lets 
                            break

                    print(f"Computer choose coordinate {comp_guess_list}{comp_guess_spot} and guessed correctly.")
                    ship_counter_computer -= 1
                    print(" ")  
                    player_turn = True  
                    break
                elif player_grid[comp_guess_list][comp_guess_spot] == 2:
                    player_grid[comp_guess_list][comp_guess_spot] = "C"
                    letter_order = 0
                    for letter in range(grid_size):
                        row_lets = chr(64 + (letter + 1))
                        letter_order += 1
                        if comp_guess_list == letter_order:
                            comp_guess_list = row_lets
                            break

                    print(f"Computer choose coordinate {comp_guess_list}{comp_guess_spot} and guessed correctly.")
                    destroyer_computer -= 1
                    if destroyer_computer == 0:
                        print("Computer sunk a destroyer ship!")
                        ship_counter_computer -= 1
                    print(" ") 
                    player_turn = True   
                    break
