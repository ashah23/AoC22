import sys
import os
sys.path.append(os.getcwd() + '\\')
import utils


lines = utils.read_from_file("Day1\\input.txt")

cur_elf = 1
cur_cals = 0

## elf carrying the most cals 
hi_cals = 0
fatty = 0
for line in lines:
    if line == '\n':
        if cur_cals > hi_cals:
            fatty = cur_elf
            hi_cals = cur_cals
        cur_elf += 1
        cur_cals = 0
    else:
        cur_cals += int(line)
if cur_cals > hi_cals:
    fatty = cur_elf
    hi_cals = cur_cals
    
print("Elf with most cals: " + str(fatty))
print("Calories carried: " + str(hi_cals))
