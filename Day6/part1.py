filename = "Day6\\sample_input.txt"

characters = []
with open(filename) as f:
    for line in f:
        characters = line

set_len = 0
index = 0
while set_len != 4:
    aset = set()
    small_list = characters[index:index+4]
    aset.update(small_list)
    set_len = len(aset)
    index += 1

print(str(index + 3))
