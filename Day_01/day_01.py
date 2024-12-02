import collections

def GetData(filename):
    col_a = []
    col_b = []
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        [a,b] = ([int(i) for i in line.split('   ')])
        col_a.append(a)
        col_b.append(b)
    return col_a, col_b

def Part1(col_a, col_b):
    sum_of_differences = 0
    col_a.sort()
    col_b.sort()
    for i, item in enumerate(col_a):
        sum_of_differences += abs(col_a[i] - col_b[i])
    return sum_of_differences


def Part2(col_a, col_b):
    similarity_score = 0
    freq_b = collections.Counter(col_b)

    for num in col_a:
        similarity_score += num * freq_b[num]
    return similarity_score




col_a, col_b = GetData("./Day_01/input.txt")
result = Part1(col_a, col_b)
print(f"part 1 result = {Part1(col_a, col_b)}")
print(f"part 2 result = {Part2(col_a, col_b)}")
