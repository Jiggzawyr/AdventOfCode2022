from functools import cmp_to_key

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
    len1 = len(l1)
    len2 = len(l2)
    cnt = 0
    while cnt < len1 and cnt < len2:
        len1 = len(l1)
        len2 = len(l2)
        if l1[cnt][0] != '[' and l2[cnt][0] != '[': # both values are integers
            if int(l1[cnt]) < int(l2[cnt]): return 1
            if int(l1[cnt]) > int(l2[cnt]): return -1
        else:
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
            compare_res = compare(l1_new,l2_new)
            if compare_res == 1: return 1
            if compare_res == -1: return -1
        cnt += 1
    if not cnt < len1 and cnt < len2: return 1
    if cnt < len1 and not cnt < len2: return -1
    return 0

def custom_sort(a,b):
    return True if compare(a,b) == 1 else False

packets = []

DIVIDER_PACKET_1 = ["[[2]]"]
DIVIDER_PACKET_2 = ["[[6]]"]

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    cnt = 1
    sum = 0
    while 3*(cnt-1) < len(lines):
        packet_one = lines[3*(cnt-1)]
        packet_two = lines[3*(cnt-1)+1]
        list_one = custom_split(packet_one[1:-1])
        list_two = custom_split(packet_two[1:-1])
        packets.append(list_one)
        packets.append(list_two)
        cnt += 1
    packets.append(DIVIDER_PACKET_1)
    packets.append(DIVIDER_PACKET_2)

packets = sorted(packets, key=cmp_to_key(compare), reverse=True)
cnt = 1
decoder_key = 1
for packet in packets:
    print(packet)
    if packet == DIVIDER_PACKET_1: decoder_key *= cnt
    if packet == DIVIDER_PACKET_2: decoder_key *= cnt
    cnt += 1
print("decoder_key: ", decoder_key)