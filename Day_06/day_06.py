
def GetData(filename):
    map = []
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        # print(f"'{line=}'")
        line = line.strip()
        map.append(list(line))
    map = PadMap(map)
    return map

def PadMap(map):
    new_map = []
    new_map.append(list(" " * (len(map[0]) + 2)))
    for line in map:
        new_map.append([" "]+line + [" "])
    new_map.append(" " * (len(map[0]) + 2))
    return new_map

def PrintMap(map):
    for line in map:
        print(''.join(line))

def MoveGuard(map, guard):
    map[guard["y"]][guard["x"]] = "X"
    next_space = map[guard["y"] + guard["dy"]][guard["x"] + guard["dx"]]
    match next_space:
        case '#':
            guard["dx"], guard["dy"] = -guard["dy"], guard["dx"]
        case '.' | 'X':
            guard["x"] = guard["x"] + guard["dx"]
            guard["y"] = guard["y"] + guard["dy"]
            map[guard["y"]][guard["x"]] = '*'
        case _:
            return map, guard, False
    return map, guard, True

def MoveGuard2(map, guard, corners):
    map[guard["y"]][guard["x"]] = "."
    next_space = map[guard["y"] + guard["dy"]][guard["x"] + guard["dx"]]
    match next_space:
        case '#':
            guard["dx"], guard["dy"] = -guard["dy"], guard["dx"]
            map[guard["y"]][guard["x"]] = 'X'
            corners.append([guard["x"], guard["y"]])
        case '.':
            guard["x"] = guard["x"] + guard["dx"]
            guard["y"] = guard["y"] + guard["dy"]
            map[guard["y"]][guard["x"]] = '*'
        case 'X':
            print("Crossed X")
            PrintMap(map)
            print(f"Block at {guard['x'] + guard['dx'] * 2}, {guard['y'] + guard['dy'] * 2}")
            PrintMap(map)
            # map = ClearMapOfX(map)
            # PrintMap(map)
            guard["x"] = guard["x"] + guard["dx"]
            guard["y"] = guard["y"] + guard["dy"]
            map[guard["y"]][guard["x"]] = '*'
        case _:
            return map, guard, False
    return map, guard, True

def ClearMapOfX(map):
    new_map = []
    for line in map:
        new_map.append(['.' if c == 'X' else c for c in line])
    return new_map



def FindGuard(map):
    for y, line in enumerate(map):
        if "^" in line:
            return {"x": line.index("^"), "y": y}
    return {"x": -1, "y": -1}
 


def Part1(map, guard):
    on_map = True
    step = 0
    while on_map:
        map, guard, on_map = MoveGuard(map, guard)
    PrintMap(map)
    return sum(m.count("X") for m in map)

def Sign(v1, v2):
    if v1 > v2: return -1
    elif v1 < v2: return 1
    else: return 0     

def Part2(map, guard):
    # DOES NOT WORK!!
    on_map = True
    step = 0
    corners = []
    while on_map:
        map, guard, on_map = MoveGuard2(map, guard, corners)
        if len(corners) == 3:
            corners.pop(0)
        if len(corners) == 2:
            g = [guard["x"],guard["y"]]
            c1 = corners[0]
            clear = True
            if guard["dx"]:
                x = g[0]
                for y in range(g[1]+guard["dx"],c1[1]+guard["dx"],guard["dx"]):
                    print(f"{map[y][x]}",end='')
                    if map[y][x] != '.':
                        clear = False
                if clear & (map[x][c1[1]+guard["dx"]] == "#"):
                    print(f"Block at {x}, {c1[1]+guard["dx"]}")
            print(f"Corner {c1=} {g[0]=}, {c1[1]+guard["dx"]=} {map[c1[1]+guard["dx"]][g[0]]=} {clear=} {guard["dx"]=}")
        PrintMap(map)
    return sum(m.count("X") for m in map)
     
map = GetData ("./tinput.txt")
PrintMap(map)
guard_pos = FindGuard(map)
guard = {"x": guard_pos["x"], "y": guard_pos["y"], "dx": 0, "dy": -1}
print(f"Test Result Part 1: {Part1(map, guard)}")
map = GetData ("./tinput.txt")
PrintMap(map)
guard_pos = FindGuard(map)
guard = {"x": guard_pos["x"], "y": guard_pos["y"], "dx": 0, "dy": -1}
print(f"Test Result Part 2: {Part2(map, guard)}")

map = GetData ("./input.txt")
PrintMap(map)
guard_pos = FindGuard(map)
guard = {"x": guard_pos["x"], "y": guard_pos["y"], "dx": 0, "dy": -1}
# print(f"Final Result Part 1: {Part1(map, guard)}")
# print(f"Final Result Part 2: {Part2(rules, pages)}")