# Battle ship 1.1 stage: Nate S and Trusha

import random

if __name__ == "__main__":
    grid = []
    user_grid = []
    numbers_list = []
    user_numbers_list = []
    ship_counter = 0 
    row_num = [" ", "1","2", "3", "4", "5", "6", "7", "8", "9", "10"]
    row_letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    user_guesses_list = []
    chances = 0

    while True:
        grid_size = int(input("How big do you want your grid (must be between 4 to 10.): "))
        if grid_size >= 4 or grid_size <= 10:
            break
        else:
            print("Please enter a valid input.")
    while True:
        placement_choice = str(input("Would you like to place ships manually or randomly (M for manually, R for randomly.): "))
        if placement_choice == "M" or placement_choice == "R":
            break
        else:
            print("Please input M or R for manually or randomly.")

    num_ships = grid_size // 2

    #Ship grid
    numbers_list.append(row_num[0])
    for numbers in range(grid_size):
        if numbers == grid_size:
            break
        else:
            numbers_list.append(row_num[numbers+1])
    grid.append(numbers_list)

    # Ship Grid
    for rand_row in range(grid_size):    
        roworder = 0
        row = [f"{row_letter[rand_row]}"]
        for spot in range(grid_size):
            if spot == grid_size:
                break
            else:
                zero = 0
                row.append(zero)
        grid.append(row)
        rand_row += 1
    
    # User grid
    user_numbers_list.append(row_num[0])
    for numbers in range(grid_size):
        if numbers == grid_size:
            break
        else:
            user_numbers_list.append(row_num[numbers+1])
    user_grid.append(user_numbers_list)

    #User Grid
    for random_row in range(grid_size):
        user_row = [f"{row_letter[random_row]}"]
        for spots in range(grid_size):
            if spots == grid_size:
                break
            else:
                zero = 0
                user_row.append(zero)
        user_grid.append(user_row)
        random_row += 1
        
    if placement_choice == "R":
        for rand_row in range(grid_size):
            if ship_counter == num_ships:
                break
            else:
                for order in range(grid_size):
                    number = random.randint(1,4)
                    if number == 4:
                        if grid[0]:
                            continue
                        else:
                            grid[rand_row][order+1] = 1
                            ship_counter += 1
                    print("")
    else:
        num_ships_avaliable = num_ships
        while num_ships_avaliable != 0:
            ship_placement = input("Where would you like to place the ship (Ex: A1):")
            if ship_placement[0] in row_letter and ship_placement[1] in row_num:
                print(f"Placed ship on {ship_placement}")
                num_ships_avaliable -= 1
                column = int(ship_placement[1])
                for row in range(grid_size):
                    if ship_placement[0] == "A":
                        rowindex = 1
                    elif ship_placement[0] == "B":
                        rowindex = 2
                    elif ship_placement[0] == "C":
                        rowindex = 3
                    elif ship_placement[0] == "D":
                        rowindex = 4
                    elif ship_placement[0] == "E":
                        rowindex = 5
                    elif ship_placement[0] == "F":
                        rowindex = 6
                    elif ship_placement[0] == "G":
                        rowindex = 7
                    elif ship_placement[0] == "H":
                        rowindex = 8
                    elif ship_placement[0] == "I":
                        rowindex = 9
                    elif ship_placement[0] == "J":
                        rowindex = 10
                    else:
                        print("Please enter a correct coordinate.")

                    grid[rowindex][column] = 1

    for row in user_grid:
        print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")
    
    print(f"There are {num_ships} ships on the board.")
    print("If you hit a ship an O will be on the board, otherwise it will be an X.")
    
    ship_counter = num_ships
    while True:
        if ship_counter == 0:
            print("\nAll ships hit! You won!")
            break
        elif chances == 5:
            print("\n All 5 chances used! You lose!")
            break
        else:
            while True:
                user_guess = input("\nPlease enter your guess (A1): ")
                if user_guess in user_choices:
                        user_guesses_list.append(user_guess)
                        break
                else:
                    print("Please enter a valid guess.")

            rowindex = 0
            column = int(user_guess[1])

            if user_guess[0] == "A":
                rowindex = 1
            elif user_guess[0] == "B":
                rowindex = 2
            elif user_guess[0] == "C":
                rowindex = 3
            elif user_guess[0] == "D":
                rowindex = 4
            if grid[rowindex][column] == 0:
                user_grid[rowindex][column] = "X"
                print("\nMissed")
                chances += 1
                print(f"There are {ship_counter} ships on the board.")
                for row in user_grid:
                    print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")
                
            else:
                user_grid[rowindex][column] = "O"
                print("\nCorrect. You hit a ship")
                ship_counter -= 1
                print(f"There are {ship_counter} ships on the board.")
                for row in user_grid:
                    print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")

