import re

def GetData(filename):
    with open(filename) as f:
        lines = f.readlines()
    return ''.join(lines)

def Part1(instructions):
    result = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", instructions)
    return sum([int(a)*int(b) for a,b in result])

def Part2(instructions):
    sum = 0
    regex = r"(?:mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't)\(\)"
    result = re.findall(regex, instructions)
    count = True
    for r in result:
        if r[0] and r[1] and count:
            sum += int(r[0]) * int(r[1])
        elif r[2]:
            count = True
        elif r[3]:
            count = False
    return sum



instructions = GetData(f"tinput.txt")
print(f"TEST Part 1 result: {Part1(instructions)}")
print(f"TEST Part 2 result: {Part2(instructions)}")

instructions = GetData(f"input.txt")
print(f"\nFINAL Part 1 result: {Part1(instructions)}")
print(f"FINAL Part 2 result: {Part2(instructions)}")