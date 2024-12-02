import collections
debug = False

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
        # print(report)
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
            # print(f"{read=}; {sign=}; {safe_report=}")

        last_read = report[0]
        for read in report[1:]:
            delta = abs(last_read - read)
            if delta < 1 or delta > 3:
                safe_report = False
            last_read = read
            # print(f"{read=}; {delta=}; {safe_report=}")

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
        if debug: print(f"Checksign {read=} {last_read=}")
    return True


def CheckDelta(report):
    last_read = report[0]
    for read in report[1:]:
        delta = abs(read-last_read)
        if delta < 1 or delta > 3:
            return False
        last_read = read
        if debug: print(f"CheckDelta {read=} {last_read=} {delta=}")
    return True


def Part2(reports):
    good = open(".\\Day_02\\good_reports.txt","w")
    bad = open(".\\Day_02\\bad_reports.txt","w")

    safe_reports = 0
    for report in reports:
        original_report = report
        good_report = True
        good_report = good_report and CheckDelta(report) and CheckSign(report)
        if good_report:
            good.write(f"{report}\n")
            safe_reports += 1
        else:
            for i, num in enumerate(report):
                rep = report[0:i] + report[i+1:]
                good_report = CheckDelta(rep) and CheckSign(rep)
                if good_report:
                    if debug: print(f"{report} passed on {i} with {rep}")
                    good.write(f"{report} corrected to {rep}\n")
                    safe_reports += 1
                    break;
            if not good_report: bad.write(f"{report}\n")

    good.close()
    bad.close()
    return safe_reports



reports = GetData("./Day_02/input.txt")
print(f"Part 1 result: {Part1(reports)}")
print(f"Part 2 result: {Part2(reports)}")
