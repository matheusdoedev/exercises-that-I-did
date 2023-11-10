# Problem Link: https://www.beecrowd.com.br/judge/en/problems/view/1012

import math

PI = 3.14159

numbers_str = input().split(' ')

A = float(numbers_str[0])
B = float(numbers_str[1])
C = float(numbers_str[2])

def calculate_rectangled_triangle_area(base, height):
	return (base * height) / 2

def calculate_circle_area(radius):
	return PI * math.pow(radius, 2)

def calculate_trapezium_area(big_base, small_base, height):
	return ((big_base + small_base) * height) / 2

def calculate_square_area(side):
	return math.pow(side, 2)

def calculate_rectangle_area(base, height):
	return base * height

def parse_result_in_string(number):
	return "{:.3f}".format(number)

print("TRIANGULO: " + parse_result_in_string(calculate_rectangled_triangle_area(A,C)))
print("CIRCULO: " + parse_result_in_string(calculate_circle_area(C)))
print("TRAPEZIO: " + parse_result_in_string(calculate_trapezium_area(A,B,C)))
print("QUADRADO: " + parse_result_in_string(calculate_square_area(B)))
print("RETANGULO: " + parse_result_in_string(calculate_rectangle_area(A,B)))