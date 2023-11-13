# Problem Link: https://www.beecrowd.com.br/judge/en/problems/view/1015

import math

def get_point_position():
	numbers_str = input().split(' ')
	x = float(numbers_str[0])
	y = float(numbers_str[1])
	return (x, y)

def calculate_distance_between_two_points(p1, p2):
	return math.sqrt(math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2))

def parse_result_in_string(number):
	return "{:.4f}".format(number)

p1 = get_point_position()
p2 = get_point_position()

result = calculate_distance_between_two_points(p1, p2)

print(parse_result_in_string(result))