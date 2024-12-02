import collections

def GetData(filename):
    reports = []
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        reports.append([int(i) for i in line.split(' ')])
    return reports

def Part1(reports):
    safe_reports = 0
    for report in reports:
        safe_report = True
        last_read = report[0]
        if report[1] == report[0]:
            continue
        first_sign = (report[1] - report[0])/abs(report[1] - report[0])
        for read in report[1:]:
            if read - last_read == 0:
                safe_report = False
                break
            sign = (read - last_read)/abs(read - last_read)
            if sign != first_sign:
                safe_report = False
            last_read = read

        last_read = report[0]
        for read in report[1:]:
            delta = abs(last_read - read)
            if delta < 1 or delta > 3:
                safe_report = False
            last_read = read

        if safe_report:
            safe_reports += 1
    return safe_reports


def CheckSign(report):
    first_sign = (report[1] - report[0])/abs(report[1]-report[0]) if (report[1]-report[0]) !=0 else 0
    last_read = report[0]
    for read in report[1:]:
        sign = (read - last_read)/abs(read-last_read) if (read-last_read) !=0 else 0
        if sign != first_sign:
            return False
        last_read = read
    return True


def CheckDelta(report):
    last_read = report[0]
    for read in report[1:]:
        delta = abs(read-last_read)
        if delta < 1 or delta > 3:
            return False
        last_read = read
    return True


def Part2(reports):

    safe_reports = 0
    for report in reports:
        original_report = report
        if CheckDelta(report) and CheckSign(report):
            safe_reports += 1
        else:
            for i, num in enumerate(report):
                rep = report[0:i] + report[i+1:]
                if CheckDelta(rep) and CheckSign(rep):
                    safe_reports += 1
                    break;

    return safe_reports

reports = GetData("./Day_02/input.txt")
print(f"Part 1 result: {Part1(reports)}")
print(f"Part 2 result: {Part2(reports)}")
