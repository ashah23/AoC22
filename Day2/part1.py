#########
# Guide:
# A, X = rock
# B, Y = paper
# C, Z = scissors


filename = "Day2\\input.txt"
total_score = 0

def calc_round_score(op_rps, self_rps):
    score = 0
    ## ROCK
    if self_rps == 'X':
        score += 1
        ## rock v rock = tie
        if op_rps == 'A':
            score += 3
        ## rock v paper = loss
        elif op_rps == 'B':
            score += 0
        ## rock v scissors = win
        elif op_rps == 'C':
            score += 6

    ## PAPER
    if self_rps == 'Y':
        score += 2
        ## paper v rock = win
        if op_rps == 'A':
            score += 6
        ## paper v paper = tie
        elif op_rps == 'B':
            score += 3
        ## paper v scissors = loss
        elif op_rps == 'C':
            score += 0

    ## SCISSORS
    if self_rps == 'Z':
        score += 3
        ## scissors v rock = loss
        if op_rps == 'A':
            score += 0
        ## scissors v paper = win
        elif op_rps == 'B':
            score += 6
        ## scissors v scissors = tie
        elif op_rps == 'C':
            score += 3
    
    return score

with open(filename) as f:
    for line in f:
        op_rps = line[0]
        self_rps = line[2]
        round_score = calc_round_score(op_rps, self_rps)
        # print(str(round_score))
        total_score += round_score

print(str(total_score))
