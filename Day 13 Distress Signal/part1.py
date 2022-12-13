def custom_split(s):
    if s == '': return []
    cnt = 0
    res = []
    last_comma = -1
    brackets = 0
    while (cnt < len(s)):
        if s[cnt] == '[': brackets += 1
        if s[cnt] == ']': brackets -= 1
        if s[cnt] == ',':
            if brackets == 0:
                res.append(s[last_comma+1:cnt])
                last_comma = cnt
        cnt += 1
    res.append(s[last_comma+1:])
    return res

def compare(l1, l2):
    print("=======================")
    print("l1: ", l1)
    print("l2: ", l2)
    len1 = len(l1)
    len2 = len(l2)
    print("len1: ", len1)
    print("len2: ", len2)
    cnt = 0
    while cnt < len1 and cnt < len2:
        print("cnt: ", cnt)
        len1 = len(l1)
        len2 = len(l2)
        print("l1[cnt]: ", l1[cnt])
        print("l2[cnt]: ", l2[cnt])
        if l1[cnt][0] != '[' and l2[cnt][0] != '[': # both values are integers
            print("BOTH INTEGERS")
            if int(l1[cnt]) < int(l2[cnt]): return 1
            if int(l1[cnt]) > int(l2[cnt]): return -1
        else:
            print("NOT BOTH INTEGERS")
            if l1[cnt][0] == '[':
                l1_new = custom_split(l1[cnt][1:-1])
            else: 
                temp = l1[cnt]
                l1_new = []
                l1_new.append(temp)
            if l2[cnt][0] == '[':
                l2_new = custom_split(l2[cnt][1:-1])
            else: 
                temp = l2[cnt]
                l2_new = []
                l2_new.append(temp)
            print("l1_new: ", l1_new)
            print("l2_new: ", l2_new)
            compare_res = compare(l1_new,l2_new)
            print("compare_res: ", compare_res)
            if compare_res == 1: return 1
            if compare_res == -1: return -1
            print("RETURN FROM RECURSION")
        cnt += 1
    print("cnt: ", cnt)
    print("len1: ", len1)
    print("len2: ", len2)
    if not cnt < len1 and cnt < len2: return 1
    if cnt < len1 and not cnt < len2: return -1
    print("SAME LENGTH")
    return 0

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    cnt = 1
    sum = 0
    while 3*(cnt-1) < len(lines):
        packet_one = lines[3*(cnt-1)]
        packet_two = lines[3*(cnt-1)+1]
        list_one = custom_split(packet_one[1:-1])
        list_two = custom_split(packet_two[1:-1])
        if compare(list_one, list_two) == 1: 
            sum += cnt
            print("COUNTER: ", cnt)
        cnt += 1
    print("sum: ", sum)
