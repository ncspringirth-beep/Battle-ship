# Battle ship 1.3 stage: Nate S and Trusha

import random

if __name__ == "__main__":
    player_grid = []
    comp_grid = []
    comp_grid_hidden = []
    numbers_list = []
    user_numbers_list = []
    comp_numbers_list = []
    ship_counter = 0 
    user_guesses_list = []
    num_ships = 2

    while True:
        grid_size = int(input("How big do you want your grid (must be between 4 to 10.): "))
        if grid_size >= 4 or grid_size <= 10:
            break
        else:
            print("Please enter a valid input.")

    # Player grid - users board in which computer guesses on
    numbers_list.append(" ")
    for numbers in range(grid_size):
        if numbers == grid_size:
            break
        else:
            numbers_list.append(numbers+1)
    player_grid.append(numbers_list)

    # Player Grid - users board in which computer guesses on
    for rand_row in range(grid_size):    
        roworder = 0
        row = [f"{chr(64+(rand_row+1))}"]
        for spot in range(grid_size):
            if spot == grid_size:
                break
            else:
                zero = 0
                row.append(zero)
        player_grid.append(row)
        rand_row += 1
    
    # Comp grid - enemy's board for user to guess on 
    comp_numbers_list.append(" ")
    for numbers in range(grid_size):
        if numbers == grid_size:
            break
        else:
            comp_numbers_list.append(numbers+1)
    comp_grid.append(comp_numbers_list)

    # Comp Grid - enemy's board for user to guess on 
    for random_row in range(grid_size):
        user_row = [f"{chr(64+(random_row+1))}"]
        for spots in range(grid_size):
            if spots == grid_size:
                break
            else:
                zero = 0
                user_row.append(zero)
        comp_grid.append(user_row)
        random_row += 1
    
    # Comp hidden board - board where o's or x's are printed
    user_numbers_list.append(" ")
    for numbers in range(grid_size):
        if numbers == grid_size:
            break
        else:
            user_numbers_list.append(numbers+1)
            print(user_numbers_list)
    comp_grid_hidden.append(user_numbers_list)

    # Comp hidden board - board where o's or x's are printed
    for random_row1 in range(grid_size):
        comp_row = [f"{chr(64+(random_row1+1))}"]
        for spots1 in range(grid_size):
            if spots1 == grid_size:
                break
            else:
                zero = 0
                comp_row.append(zero)
        comp_grid_hidden.append(comp_row)
        random_row1 += 1

# players ship computer guess 
    shipNumber = 1
    while True:
        if shipNumber == 1:
            randomList = random.randint(1, grid_size)
            randomSpot = random.randint(1, grid_size)
            if player_grid[randomList][randomSpot] != 0:
                continue
            else:
                shipNumber += 1
                player_grid[randomList][randomSpot] = 1
        elif shipNumber == 2:
            randomList = random.randint(1, grid_size)
            randomSpot = random.randint(1, grid_size)
            if player_grid[randomList][randomSpot] != 0:
                continue
            else:
                randomDirection = random.randint(1, 4)
                # 1 = down
                if randomDirection == 1:
                    try:
                        if player_grid[randomList - 1][randomSpot] != 0:
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
                        if player_grid[randomList + 1][randomSpot] != 0:
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
                        if player_grid[randomList][randomSpot + 1] != 0:
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
                        if player_grid[randomList][randomSpot] != 0:
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
            if comp_grid[randomList][randomSpot] != 0:
                continue
            else:
                shipNumber += 1
                comp_grid[randomList][randomSpot] = 1
        elif shipNumber == 2:
            randomList = random.randint(1, grid_size)
            randomSpot = random.randint(1, grid_size)
            if comp_grid[randomList][randomSpot] != 0:
                continue
            else:
                randomDirection = random.randint(1, 4)
                # 1 = down
                if randomDirection == 1:
                    try:
                        if comp_grid[randomList - 1][randomSpot] != 0:
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
                        if comp_grid[randomList + 1][randomSpot] != 0:
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
                        if comp_grid[randomList][randomSpot + 1] != 0:
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
                        if comp_grid[randomList][randomSpot - 1] != 0:
                            continue
                        else:
                            comp_grid[randomList][randomSpot] = shipNumber
                            comp_grid[randomList][randomSpot - 1] = shipNumber
                            break
                    except:
                        continue


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
        for row in comp_grid_hidden:
            print(*row)

        print("\n Com board not hidden values")
        for row in comp_grid:
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
                                    if int(let[1]) in user_numbers_list:
                                        user_guesses_list.append(user_guess)
                                        check = False
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

            if comp_grid[rowindex][column] == 0:
                comp_grid_hidden[rowindex][column] = "X"
                print("\nMissed")
                print(f"There are {ship_counter_player} ships on the board.")
                print(" ")
                player_turn = False
            elif comp_grid[rowindex][column] == 1:
                comp_grid_hidden[rowindex][column] = "C"
                print("\nCorrect. You sunk a dingy")
                ship_counter_player -= 1
                print(f"There are {ship_counter_player} ships on the board.")
                print(" ")   
                player_turn = False
            elif comp_grid[rowindex][column] == 2:
                comp_grid_hidden[rowindex][column] = "C"
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
                if player_grid[comp_guess_list][comp_guess_spot] == 0:
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
