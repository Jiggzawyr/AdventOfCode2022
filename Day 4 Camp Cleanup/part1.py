with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    sum = 0
    for line in lines:
        pair = line.split(',')
        range_1 = pair[0].split('-')
        range_2 = pair[1].split('-')
        if ((int(range_1[0]) <= int(range_2[0]) and int(range_1[1]) >= int(range_2[1])) 
            or (int(range_1[0]) >= int(range_2[0]) and int(range_1[1]) <= int(range_2[1]))
        ) :
            sum += 1
    print("sum: ", sum)