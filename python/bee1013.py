# Problem Link: https://www.beecrowd.com.br/judge/en/problems/view/1013

numbers_str = input().split(' ')
biggest_number = 0

for number in numbers_str:
	serialized_number = int(number)

	if serialized_number > int(biggest_number):
		biggest_number = number

print(biggest_number.__str__() + " eh o maior")