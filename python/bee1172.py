# Problem link: https://www.beecrowd.com.br/judge/en/runs/code/36060466
# Obs: I dont submit this solution. My goal with this problem was to use numpy library, however beecrowd doesn't have the numpy in the solution submission environment. So, I used lists to solve this problem in beecrowd.

import numpy as np

def read_a_int():
	return int(input())

numbers = np.array(range(0, 10))
count = 0

while count < numbers.size:
	number = read_a_int()

	if number <= 0:
		numbers[count] = 1
	else:
		numbers[count] = number
	count += 1

count = 0

while count < numbers.size:
	print("X[%d] = %d" % (count, numbers[count]))
	count += 1
