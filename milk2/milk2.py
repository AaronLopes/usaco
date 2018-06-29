"""
ID: aaronlo1
LANG: PYTHON3
TASK: milk2
"""

fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')
n = int(fin.readline())
times = []
mx = 0
lx = 0
m_lx = 0

for line in fin:
	times.append(line.split())

int_times = [map(int, i) for i in times]
head = int_times[0][0]
tail = int_times[0][1]

#longest time
for i in range(len(int_times) - 1):
	if int_times[i][0] < head:
		head = int_times[i][0]
	elif int_times[i][1] > tail:
		tail = int_times[i][1]
	elif int_times[i + 1][0] > int_times[i][1]:
		head = int_times[i+1][0]
		tail = int_times[i+1][1]

mx = tail - head
print(mx)

lx = 0 
#shortest time 
for i in range(len(int_times) - 1):
	if int_times[i][0] < head: 
		lx += head - int_times[i][0]
 



"""mx = int(tail) - int(head)
#no milking
for i in range(len(times) - 1):
	if int(times[i][1]) < int(times[i+1][0]) and int(times[i+1][0]) > int(tail): 
		m_lx = int(times[i+1][0]) - int(times[i][1])
	if m_lx > lx:
		lx = m_lx

#print(mx, lx)
fout.write(str(mx) + " " + str(lx) + "\n")"""
fout.close
fin.close


