
def GetData(filename):
    rules = []
    pages = []
    with open(filename) as f:
        lines = f.readlines()
    rules_section = True
    for line in lines:
        # print(f"'{line=}'")
        line = line.strip()
        if len(line) == 0:
            rules_section = False
            continue
        if rules_section:
            rule = line.split("|")
            # print(f"{rule=}, {rules=}")
            rules.append(rule)
        else:
            pages.append(line.split(','))
    return rules, pages

def Part1(rules, pages):
    middle_sum = 0
    for p in pages:
        safe = True
        for rule in rules:
            # print(f"{p=}; {rule=}")
            if rule[0] in p and rule[1] in p:
                if p.index(rule[0]) > p.index(rule[1]):
                    safe = False
                    # print(f"{p=}, {rule[0]=} {rule[1]=}")
                    # print(f"{p.index(rule[0])=};{p.index(rule[1])=}")
        if safe:
            # print(f"Safe {p=}")
            middle_sum += int(p[len(p)//2])
    return middle_sum


def SortPages(rules,row):
    # the most inefficient (but transparent)
    # bubble sort ever implemented
    # print(f"\n\n{row=}")
    for cycle in range(len(row)**2):
        changed = False
        for i,page in enumerate(row):
            swap = False
            for r in rules:
                if page == r[0] and r[1] in row[0:i]:
                    swap_1 = i
                    swap_2 = row.index(r[1])
                    # print(f"{' '.join(row[0:i + 1])} rule {r[0]}|{r[1]}")
                    row[swap_1], row[swap_2] = row[swap_2], row[swap_1]
                    # print(f"{' '.join(row[0:i + 1])} - Swapped {swap_1} {swap_2} ")
                    swap = True
                    changed = True
                    break
            if swap: break
        if not changed: 
            # print(f"No change on cycle {cycle} of {len(row)**2}")
            break
    # print(f"{row=}")
    return row
    


def Part2(rules, pages):
    # Same rules as part 1 to spot the safe
    # Send the unsafe updates to SortPages
    middle_sum = 0
    for p in pages:
        safe = True
        for rule in rules:
            # print(f"{p=}; {rule=}")
            if rule[0] in p and rule[1] in p:
                if p.index(rule[0]) > p.index(rule[1]):
                    safe = False
        if safe:
            pass
        else:
            sorted = SortPages(rules,p)
            middle_sum += int(sorted[len(p)//2])
    return middle_sum


rules, pages = GetData ("./tinput.txt")
print(f"Test Result Part 1: {Part1(rules, pages)}")
print(f"Test Result Part 2: {Part2(rules, pages)}")

rules, pages = GetData ("./input.txt")
print(f"Final Result Part 1: {Part1(rules, pages)}")
print(f"Final Result Part 2: {Part2(rules, pages)}")