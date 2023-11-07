# Problem Link: https://www.beecrowd.com.br/judge/en/problems/view/1011

import math

PI = 3.14159

input_radius = int(input())

def calculates_sphere_volume(radius):
	return (4/3.0) * PI * math.pow(radius, 3)

print("VOLUME = " + "{:.3f}".format(calculates_sphere_volume(input_radius)))