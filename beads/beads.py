"""
ID: aaronlo1
LANG: PYTHON3
TASK: beads
"""

fin = open('beads.in', 'r')
fout = open('beads.out', 'w')
n = int(fin.readline())
a = list(str(fin.readline().rstrip('\n')))
beads = a + a
totals = []

def forw(i):
	t = 0
	b = beads[i]
	for j in range(i, len(beads)):
		if b == 'r':
			if beads[j] == 'b':
				break
			t += 1
		elif b == 'b':
			if beads[j] == 'r':
				break
			t += 1
		else:
			if beads[j] == 'r':
				t += 1
				b = 'r'
			elif beads[j] == 'b':
				t += 1
				b = 'b'
			else:
				t += 1
	return t, j

for i in range(len(beads)):
	t1, k = forw(i)
	t2, q = forw(k)
	totals.append(t1 + t2)

m = max(totals)
if m > len(a):
	m = len(a)

fout.write(str(m) + "\n")
fout.close()
fin.close()
