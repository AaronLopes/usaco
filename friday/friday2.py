"""
ID: aaronlo1
LANG: PYTHON3
TASK: friday
"""

curr_year = 1900
fin = open('friday.in', 'r')
n = int(fin.readline())
final_year = curr_year + n
freq = [0]*7


def numDays(year):
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30 , 31, 30, 31]
	if (year % 100 == 0 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
		days[1] += 1
	return days

total_days = 0
for i in range(curr_year, final_year):
	days = numDays(i)
	for j in range(len(days)):
		freq[(total_days + 13) % 7] += 1
		total_days += days[j]

with open('friday.out', 'w') as fout:
    fout.write(' '.join([str(i) for i in freq[-1:] + freq[:-1]]) + '\n')