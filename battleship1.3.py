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
    row_num = [" ", "1","2", "3", "4", "5", "6", "7", "8", "9", "10"]
    row_letter = []
    user_guesses_list = []
  
    while True:
        grid_size = int(input("How big do you want your grid (must be between 4 to 10.): "))
        if grid_size >= 4 or grid_size <= 10:
            break
        else:
            print("Please enter a valid input.")

    num_ships = 2

    for letter in range(grid_size):
        row_let = chr(ord('@')+(letter+1))
        row_letter.append(row_let)

    # Player grid - users board in which computer guesses on
    numbers_list.append(row_num[0])
    for numbers in range(grid_size):
        if numbers == grid_size:
            break
        else:
            numbers_list.append(row_num[numbers+1])
    player_grid.append(numbers_list)

    # Player Grid - users board in which computer guesses on
    for rand_row in range(grid_size):    
        roworder = 0
        row = [f"{chr(ord('@')+(rand_row+1))}"]
        for spot in range(grid_size):
            if spot == grid_size:
                break
            else:
                zero = 0
                row.append(zero)
        player_grid.append(row)
        rand_row += 1
    
    # Comp grid - enemy's board for user to guess on 
    comp_numbers_list.append(row_num[0])
    for numbers in range(grid_size):
        if numbers == grid_size:
            break
        else:
            comp_numbers_list.append(row_num[numbers+1])
    comp_grid.append(comp_numbers_list)

    # Comp Grid - enemy's board for user to guess on 
    for random_row in range(grid_size):
        user_row = [f"{chr(ord('@')+(random_row+1))}"]
        for spots in range(grid_size):
            if spots == grid_size:
                break
            else:
                zero = 0
                user_row.append(zero)
        comp_grid.append(user_row)
        random_row += 1
    
    # Comp hidden board - board where o's or x's are printed
    user_numbers_list.append(row_num[0])
    for numbers in range(grid_size):
        if numbers == grid_size:
            break
        else:
            user_numbers_list.append(row_num[numbers+1])
    comp_grid_hidden.append(user_numbers_list)

    # Comp hidden board - board where o's or x's are printed
    for random_row1 in range(grid_size):
        comp_row = [f"{chr(ord('@')+(random_row1+1))}"]
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
    print("If you hit a ship an O will be on the board, otherwise it will be an X.")
    
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
        
        if ship_counter_player == 0:
            print("\nPlayer Wins! All computer ships hit! You won!")
            break
        elif ship_counter_computer == 0:
            print("\nComputer won! Computer hit all player ships!")
            break
        elif player_turn:
            print("\nPlayers turn: ")
            while True:
                user_guess = input("Please enter your guess (A1): ")
                if user_guess not in user_guesses_list:
                    if user_guess[0] in row_letter and user_guess[1] in user_numbers_list:
                            user_guesses_list.append(user_guess)
                            break
                else:
                    print("Please enter a valid guess.")

            order_row = 0
            column = int(user_guess[1])
            
            for specific_letter in row_letter:
                order_row += 1
                if user_guess[0] == specific_letter:
                    rowindex = order_row

            if comp_grid[rowindex][column] == 0:
                comp_grid_hidden[rowindex][column] = "X"
                print("\nMissed")
                print(f"There are {ship_counter_player} ships on the board.")
                print(" ")
                player_turn = False
            elif comp_grid[rowindex][column] == 1:
                comp_grid_hidden[rowindex][column] = "C"
                print("\nCorrect. You hit a dingy")
                ship_counter_player -= 1
                print(f"There are {ship_counter_player} ships on the board.")
                print(" ")   
                player_turn = False
            elif comp_grid[rowindex][column] == 2:
                comp_grid_hidden[rowindex][column] = "C"
                print("\nCorrect. You partially hit a destroyer")
                destroyer_player -= 1
                if destroyer_player == 0:
                    ship_counter_player -= 1
                print(f"There are {ship_counter_player} ships on the board.")
                print(" ")
                player_turn = False

        elif player_turn == False:
            print("\nComputer's turn: ")
            while True:
                comp_guess_list = random.randint(1, grid_size)
                comp_guess_spot = random.randint(1, grid_size)
                if comp_grid[comp_guess_list][comp_guess_spot] == 0:
                    player_grid[comp_guess_list][comp_guess_spot] = "X"
                    letter_order = 0
                    for letter in row_letter:
                        letter_order += 1
                        if comp_guess_list == letter_order:
                            comp_guess_list = letter
                    print(f"Computer choose coordinate {comp_guess_list}{comp_guess_spot} and missed.")
                    print(" ")
                    player_turn = True
                    break
                elif comp_grid[comp_guess_list][comp_guess_spot] == 1:
                    player_grid[comp_guess_list][comp_guess_spot] = "C"
                    print("\n Computer hit a dingy!")
                    letter_order = 0
                    for letter in row_letter:
                        letter_order += 1
                        if comp_guess_list == letter_order:
                            comp_guess_list = letter
                    print(f"Computer choose coordinate {comp_guess_list}{comp_guess_spot} and guessed correctly.")
                    ship_counter_computer -= 1
                    print(" ")    
                    break
                elif comp_grid[comp_guess_list][comp_guess_spot] == 2:
                    player_grid[comp_guess_list][comp_guess_spot] = "C"
                    print("\nComputer partially hit a destroyer")
                    letter_order = 0
                    for letter in row_letter:
                        letter_order += 1
                        if comp_guess_list == letter_order:
                            comp_guess_list = letter
                    print(f"Computer choose coordinate {comp_guess_list}{comp_guess_spot} and guessed correctly.")
                    destroyer_computer -= 1
                    if destroyer_computer == 0:
                        print("\n Computer sunk the destroyer ship!")
                        ship_counter_computer -= 1
                    print(" ") 
                    player_turn = True   
                    break
