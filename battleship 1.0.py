# Battle ship 1.0 stage: Nate S and Trusha

# Done with 1.0 stage
import random

if __name__ == "__main__":
    grid = []
    user_grid = [[" ", "1","2", "3", "4"],
                 ["A", " ", " ", " ", " "],
                 ["B", " ", " ", " ", " "],
                 ["C", " ", " ", " ", " "],
                 ["D", " ", " ", " ", " "]]
    ship_counter = 0 
    row_num = [" ", "1","2", "3", "4"]
    grid.append(row_num)
    for rand_row in range(4):
        roworder = 0
        row_letter = ["A", "B", "C", "D"]
        row = [f"{row_letter[rand_row]}", 0,0,0,0]
        grid.append(row)
        rand_row+=1
        for order in range(4):
            number = random.randint(1,4)
            if number == 4:
                grid[rand_row][order+1] = 1
                ship_counter += 1

    for row in user_grid:
        print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")
    
    print(f"There are {ship_counter} ships on the board.")
    user_choices = ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4", "D1", "D2", "D3", "D4"]
    user_guesses_list = []
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

