from matrix_ops import Matrix

class Pos():
    def __init__(self,p):
        self.x = p[0]
        self.y = p[1]
    def __repr__(self):
        return f"({self.x}, {self.y})"

class Guard():
    def __init__(self,pos):
        self.pos = pos
        self.x = pos.x
        self.y = pos.y
        self.corners = []
    
    def set_corner(self,pos):
        self.corners.append(pos)
        if len(self.corners) == 3:
            self.corners.pop(0)
            


def GetData(filename):
    map = []
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        # print(f"'{line=}'")
        line = line.strip()
        map.append(list(line))
    mat_map = Matrix(map)
    return mat_map

def FindGuard(map):
    for y in range(map.h):
        for x in range(map.w):
            if map.cell((x,y)) == "^":
                return x, y
    return -1,-1

def MoveGuard(map, g):
    map.set((g.x, g.y), "X")
    next_space = map.cell((g.x + g.dx, g.y + g.dy))
    match next_space:
        case '#':
            # right turn
            g.dx, g.dy = -g.dy, g.dx
            g.set_corner(Pos((g.x,g.y)))
            map.set((g.x,g.y), "O")
        case '.' | 'X':
            # move
            g.x = g.x + g.dx
            g.y = g.y + g.dy
            map.set((g.x,g.y), "*")
        case None:
            # off map
            map.set((g.x, g.y), "X")
            return map, guard, False
    # print(f"{guard.corners}\n\n")
    return map, guard, True



def LookRight(map, guard):
    out = ""
    if len(guard.corners) < 2: return None
    c0 = guard.corners[0]
    c1 = guard.corners[1]
    delta = Pos((c0.x - c1.x, c0.y - c1.y))
    target = Pos((delta.x + guard.x - guard.dy, delta.y + guard.y + guard.dx))
    if map.cell((target.x,target.y)) == "#":
        out = "LOOP!"

    return f"{out} {(guard.x,guard.y)} delta {delta} target {target} cell {map.cell((target.x,target.y))}"

def Part1(map,guard):
    on_map = True
    while on_map:
        map, guard, on_map = MoveGuard(map, guard)
    return sum(m.count("X") for m in map.prt())


def Part2(map,guard):
    on_map = True
    while on_map:
        map, guard, on_map = MoveGuard(map, guard)
        print(map.prt())
        print(LookRight(map, guard))
    return sum(m.count("X") for m in map.prt())


map = GetData ("./tinput.txt")
# print(map.prt())
guard = Guard(Pos(FindGuard(map)))
guard.dx = 0
guard.dy = -1
print(f"Test map Part 1 {Part1(map,guard)}")

map = GetData ("./input.txt")
# print(map.prt())
guard = Guard(Pos(FindGuard(map)))
guard.dx = 0
guard.dy = -1
print(f"Map Part 1 {Part1(map,guard)}")


map = GetData ("./tinput.txt")
# print(map.prt())
guard = Guard(Pos(FindGuard(map)))
guard.dx = 0
guard.dy = -1
print(f"Test map Part 2 {Part2(map,guard)}")

map = GetData ("./input.txt")
# print(map.prt())
guard = Guard(Pos(FindGuard(map)))
guard.dx = 0
guard.dy = -1
# print(f"Map Part 2 {Part2(map,guard)}")
