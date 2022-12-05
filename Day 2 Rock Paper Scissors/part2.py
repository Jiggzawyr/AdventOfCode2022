ABC = {
    "A" : 1, # Rock
    "B" : 2, # Paper
    "C" : 3, # Scissors
}

XYZ = {
    "X" : 0, # Lose
    "Y" : 3, # Draw
    "Z" : 6, # Win
}

def hand(res, opp):
    if res == "X": # lost
        if opp == "A": return "C"
        if opp == "B": return "A"
        if opp == "C": return "B"
    if res == "Y" : # draw
        return opp 
    if res == "Z": # won
        if opp == "A": return "B"
        if opp == "B": return "C"
        if opp == "C": return "A"

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    score = 0
    for line in lines:
        c = line.split()
        score += XYZ[c[1]]
        score += ABC[hand(c[1],c[0])]
    print(score)