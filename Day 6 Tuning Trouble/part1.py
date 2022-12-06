with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    max_line_len = 0
    for line in lines:
        for i in range(3,len(line)):
            set_of_4 = set()
            set_of_4.add(line[i-3])
            set_of_4.add(line[i-2])
            set_of_4.add(line[i-1])
            set_of_4.add(line[i])          
            if len(set_of_4) == 4:
                break