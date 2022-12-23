instructions = []
crt = []
filename = "Day10\\input.txt"
with open(filename) as f:
    for line in f:
        instructions.append(line.strip().split(' '))

cycle = 0
X = 1
sum = 0
cur_crt = []
for inst in instructions:
    cycle += 1
    pos = (cycle % 40) - 1
    if pos >= X-1 and pos <= X+1:
        cur_crt.append('X')
    else:
        cur_crt.append('.')
    if pos == -1:
        crt.append(cur_crt)
        cur_crt = []
        

    if inst[0] == "addx":
        amt = int(inst[1])
        cycle += 1
        pos = (cycle % 40) - 1
        if pos >= X-1 and pos <= X+1:
            cur_crt.append('X')
        else:
            cur_crt.append('.')
        if pos == -1:
            crt.append(cur_crt)
            cur_crt = []
        X += amt
        
cycle += 1
pos = (cycle % 40) - 1
if pos >= X-1 and pos <= X+1:
    cur_crt.append('X')
else:
    cur_crt.append('.')
if pos == -1:
    crt.append(cur_crt)
    cur_crt = []

for line in crt:
    print(line)