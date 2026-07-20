# Battle ship 1.1 stage: Nate S and Trusha

import random

if __name__ == "__main__":
    grid = []
    user_grid = []
    numbers_list = []
    ship_counter = 0 
    row_num = [" ", "1","2", "3", "4", "5", "6", "7", "8", "9", "10"]
    row_letter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    user_guesses_list = []

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

    numbers_list.append(row_num[0])
    for numbers in range(grid_size):
        if numbers == grid_size:
            break
        else:
            numbers_list.append(row_num[numbers+1])
    grid.append(numbers_list)
    user_grid.append(numbers_list)
    
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
        user_grid.append(row)
        rand_row+=1
    
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


    print(grid)


    for row in user_grid:
        print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")
    
    print(f"There are {ship_counter} ships on the board.")
    print("If you hit a ship an O will be on the board, otherwise it will be an X.")

    while True:
        if ship_counter == 0:
            print("\nAll ships hit! You won!")
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

