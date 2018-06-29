"""
ID: aaronlo1
PROB: gift1
LANG: PYTHON3
"""

import collections

in_data = open('gift1.in', 'r')
out_data = open('gift1.out', 'w')

members = collections.OrderedDict()
np = int(in_data.readline())

#figure out group members
for i in range(np):
	members.update({str(in_data.readline()):0})
#find number of lines 
with open('gift1.in') as f:
   size=sum(1 for _ in f)

count = 0
while count < size - np:
	print(members)
	current_mem = in_data.readline()
	count = count + 1
	nums = str(in_data.readline()).split()
	if len(nums) == 0:
		break
	amt = int(nums[0])
	split = int(nums[1])
	if split == 0:
		give = 0
		mine = 0
	else:
		give = amt//split
		mine = amt%split
	members.update({current_mem: members[current_mem] - amt + mine})
	for i in range(split):
		key = in_data.readline()
		members.update({key: members[key] + give})

for key, value in members.items():
	out_data.write(key.rstrip('\n') + ' ')
	out_data.write(str(value))
	out_data.write('\n')
