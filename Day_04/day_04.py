def GetData(filename):
    grid_out = []
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        grid_out.append(list(line.strip()))
    return grid_out


def CreatePatterns():
    # Spent way too long automating this
    # Could have typed them out much faster

    patterns = []

    # Initially doubled up here checking forward and backward
    # on every angle
    angles = []
    for i in range(-1,2):
        for j in range(-1,2):
            angles.append((i,j))

    for a in angles:
        x = y = 0
        # using "=[]" can be trouble
        p_pattern = list()
        u_pattern = list()
        if a[0] == a[1] == 0:
            continue
        for i in range(4):
            p_pattern.append((x,y))
            x += a[0]
            y += a[1]
        patterns.append(p_pattern)
    return patterns

def Part1(grid):
    # Iterate a pattern over the grid
    # Reminds me of a raster image filter

    patterns = CreatePatterns()
    match_count = 0
    for pattern in patterns:
        # I wasted a lot of time on edge checks - 
        # next time I will just pad the matrix with dummy data
        for j, row in enumerate(grid):
            for i, cell in enumerate(row):
                max_i = i + max([x[0] for x in pattern])
                min_i = i + min([x[0] for x in pattern])
                max_j = j + max([x[1] for x in pattern])
                min_j = j + min([x[1] for x in pattern])
                if (max_i > len(row) - 1 or min_i < 0 or max_j > len(grid) - 1 or min_j < 0):
                    continue
                phrase = grid[i + pattern[0][0]][j + pattern[0][1]] \
                    + grid[i + pattern[1][0]][j + pattern[1][1]] \
                    + grid[i + pattern[2][0]][j + pattern[2][1]] \
                    + grid[i + pattern[3][0]][j + pattern[3][1]]
                if phrase == "XMAS":
                    match_count += 1
    return match_count

def CreateXPatterns():
    # Learned my lesson
    patterns = [
        [(0,0),(0,2),(1,1),(2,0),(2,2)],
        [(0,0),(2,0),(1,1),(0,2),(2,2)],
        [(2,2),(0,2),(1,1),(2,0),(0,0)],
        [(2,2),(2,0),(1,1),(0,2),(0,0)]
    ]
    return patterns

def Part2(grid):
    # Same approach, just updated the pattern check
    patterns = CreateXPatterns()
    match_count = 0
    for pattern in patterns:
        for j, row in enumerate(grid):
            for i, cell in enumerate(row):
                max_i = i + max([x[0] for x in pattern])
                min_i = i + min([x[0] for x in pattern])
                max_j = j + max([x[1] for x in pattern])
                min_j = j + min([x[1] for x in pattern])
                if (max_i > len(row) - 1 or min_i < 0 or max_j > len(grid) - 1 or min_j < 0):
                    continue
                phrase = \
                      grid[i + pattern[0][0]][j + pattern[0][1]] \
                    + grid[i + pattern[1][0]][j + pattern[1][1]] \
                    + grid[i + pattern[2][0]][j + pattern[2][1]] \
                    + grid[i + pattern[3][0]][j + pattern[3][1]] \
                    + grid[i + pattern[4][0]][j + pattern[4][1]] 
                if phrase == "MMASS":
                    match_count += 1
    return match_count



grid = GetData(f"tinput.txt")
print(f"TEST Part 1 result: {Part1(grid)}")
print(f"TEST Part 2 result: {Part2(grid)}")

grid = GetData(f"input.txt")
print(f"\nFINAL Part 1 result: {Part1(grid)}")
print(f"FINAL Part 2 result: {Part2(grid)}")