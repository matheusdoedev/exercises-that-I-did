# Problem Link: https://www.beecrowd.com.br/judge/en/problems/view/1010

total = 0.0
str_numbers_list = (input() + '\n' + input()).split('\n')

for line in str_numbers_list:
	numbers = line.split(' ')
	total = total + (int(numbers[1]) * float(numbers[2]))

print("VALOR A PAGAR: R$ " + "{:.2f}".format(total))