with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    max_line_len = 0
    for line in lines:
        for i in range(3,len(line)):
            set_of_4 = set()
            for j in range(14):
                 set_of_4.add(line[i-j])       
            if len(set_of_4) == 14:
                print("first marker after character: ", i+1)
                break