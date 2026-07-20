import random
if __name__ == "__main__":
    # grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    grid = []
    for i in range(4):
        
        row = [0,0,0,0]
        grid.append(row)
        for j in range(4):

            number = random.randint(1,4)
            if number == 4:
                grid[i][j] = 1
    for row in grid:
        print(f" {row[0]} {row[1]} {row[2]} {row[3]}")
    
            