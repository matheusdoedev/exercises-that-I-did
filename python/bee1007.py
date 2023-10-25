# Problem Link: https://www.beecrowd.com.br/judge/en/problems/view/1007

A = int(input())
B = int(input())
C = int(input())
D = int(input())

def calculate_difference(a, b, c, d):
	return (a * b) - (c * d)

print("DIFERENCA = " + calculate_difference(A, B, C, D).__str__())
