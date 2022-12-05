import re

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    max_line_len = 0
    for line in lines:
        if len(line) > max_line_len: max_line_len = len(line)
        if(line==""): break
    stack_count = (max_line_len + 1) // 4
    stacks = []
    for i in range(stack_count):
        stacks.append([])
    state = 0
    for line in lines:
        if state == 0:
            if(line==""): 
                state = 1
                continue
            cnt = 1
            for i in range(stack_count):
                if(line[cnt]!=' ' and not line[cnt].isnumeric()): stacks[i].insert(0,line[cnt])
                cnt += 4
        if state == 1: 
            count, src, dst  = map(int, re.findall(r'\d+', line))
            for i in range(count):
                crate = stacks[src-1].pop()
                stacks[dst-1].append(crate)
    res = ''
    for i in range(stack_count):
        res += stacks[i].pop()
    print(res)
        