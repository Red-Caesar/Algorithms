grid = [
    ["1","0","1"],
    ["0","1","0"],
    ["1","0","1"]
]

steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
queq_land = []
queq_sea = []
if int(grid[0][0]) == 1:
    queq_land.append((0,0))
else:
    queq_sea.append((0, 0))
grid[0][0] = -1
land_count = 0
flag_land = False
while queq_land or queq_sea:
    if queq_land:
        x, y = queq_land.pop()
        if flag_land is False:
            flag_land = True
            land_count += 1
        for pair in steps:
            n_x = x + pair[0]
            n_y = y + pair[1]
            if n_x >= 0 and n_x < len(grid) and n_y >= 0 and n_y < len(grid[0]):
                if int(grid[n_x][n_y]) == 1:
                    grid[n_x][n_y] = -1
                    queq_land.insert(0, (n_x, n_y))
                elif int(grid[n_x][n_y]) == 0:
                    grid[n_x][n_y] = -1
                    queq_sea.append((n_x, n_y))
    elif queq_sea:
        x, y = queq_sea.pop()
        flag_land = False
        for pair in steps:
            n_x = x + pair[0]
            n_y = y + pair[1]
            if n_x >= 0 and n_x < len(grid) and n_y >= 0 and n_y < len(grid[0]):
                if int(grid[n_x][n_y]) == 1:
                    grid[n_x][n_y] = -1
                    queq_land.insert(0, (n_x, n_y))
                    grid[x][y] = 0
                    break
                elif int(grid[n_x][n_y]) == 0:
                    grid[n_x][n_y] = -1
                    queq_sea.insert(0, (n_x, n_y))
print(land_count)


