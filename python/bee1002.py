# Problem Link: https://www.beecrowd.com.br/judge/en/problems/view/1002

radius = float(input())

def get_circle_area(radius):
	pi = 3.14159

	return radius ** 2 * pi

print("A=" + "{:.4f}".format(get_circle_area(radius)))