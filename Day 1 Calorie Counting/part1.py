with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    max = 0
    sum = 0
    for line in lines:
        if line == '' :
            if sum > max: max = sum
            sum = 0 
        else: 
            sum += int(line)
    print("max: ", max)