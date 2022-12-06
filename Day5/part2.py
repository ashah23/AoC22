filename = "Day5\\input.txt"

lines = []
longest_line = 0
encountered_break = False
with open(filename) as f:
    for line in f:
        lines.append(line)
        if line == '\n':
            encountered_break = True
        if not encountered_break:
            if len(line) > longest_line:
                longest_line = len(line)

# parse inputs into stacks
stack_list = []
line_num = 0
for i in range(int(longest_line / 4)):
    stack_list.append([])

for line in lines:
    line_num += 1
    if len(line) <= 2:
        break
    line_index = 1
    list_index = 0
    while line_index < len(line):
        letter = line[line_index]
        if letter != " ":
            stack_list[list_index].append(letter)
        line_index += 4
        list_index += 1

# clean up the number of each list
for index in range(len(stack_list)):
    stack_list[index] = stack_list[index][:-1]
    stack_list[index].reverse()


for line_index in range(line_num, len(lines)):
    instructions = lines[line_index].strip().split(' ')
    amount = int(instructions[1])
    ## need to go from 1 based to 0 based
    from_stack = int(instructions[3]) - 1
    to_stack = int(instructions[5]) - 1
    all_items = []
    for i in range(amount):
        all_items.append(stack_list[from_stack].pop())
    for i in range(amount):
        stack_list[to_stack].append(all_items.pop())

mystr = ''
for i in range(len(stack_list)):
    mystr += stack_list[i][-1]

print(mystr)
