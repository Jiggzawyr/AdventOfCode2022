with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    max_cal = [0,0,0]
    sum_cal = 0
    for line in lines:
        if line == '' :
            for m in max_cal:
                if sum_cal > m:
                    print("**************")
                    print("max_cal: ", max_cal)
                    print("sum_cal: ", sum_cal)
                    max_cal.append(sum_cal)
                    print("max_cal: ", max_cal)
                    max_cal.sort()
                    print("max_cal: ", max_cal)
                    max_cal = max_cal[1:]
                    print("max_cal: ", max_cal)
                    break
            sum_cal = 0 
        else: 
            sum_cal += int(line)
    sum_max_cal = sum(max_cal)
    print("sum_max_cal: ", sum_max_cal)