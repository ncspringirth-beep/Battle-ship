# Battle ship 1.0 stage: Nate S and Trusha
import random

if __name__ == "__main__":
    grid = []
    
    row_num = [" ", "1","2", "3", "4"]
    grid.append(row_num)
    for i in range(4):
        roworder = 0
        row_letter = ["A", "B", "C", "D"]
        row = [f"{row_letter[i]}", 0,0,0,0]
        grid.append(row)
        i+=1
        for j in range(4):
            number = random.randint(1,4)
            if number == 4:
                grid[i][j+1] = 1


    for row in grid:
        print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")
    
    user_choices = ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4", "D1", "D2", "D3", "D4"]
    user_guesses_list = []
    user_guess = input("Please enter your guess (A1): ")
    user_guesses_list.append(user_guess)
    while True:
        if user_guess in user_choices:
            if user_guess[0] == "A":
                rowindex = 1
            elif user_guess[0] == "B":
                rowindex = 2
            elif user_guess[0] == "C":
                rowindex = 3
            elif user_guess[0] == "D":
                rowindex = 4
            break
        else:
            print("Please enter a valid guess.")

