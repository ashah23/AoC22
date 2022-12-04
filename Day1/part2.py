import sys
import os
sys.path.append(os.getcwd() + '\\')
import utils


lines = utils.read_from_file("Day1\\input.txt")

cal_list = []
cur_cals = 0
for line in lines:
    if line == '\n':
        cal_list.append(cur_cals)
        cur_cals = 0
    else:
        cur_cals += int(line)

# add the last element
cal_list.append(cur_cals)

# sort the cals in descending order and sum the top 3
sorted_cals = sorted(cal_list,reverse=True)
total_cals = sum(sorted_cals[:3])
print("Calories carried: " + str(total_cals))
