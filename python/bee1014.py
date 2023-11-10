# Problem Link: https://www.beecrowd.com.br/judge/en/problems/view/1014

x = int(input())
y = float(input())

def calculate_car_consumption(distance_traveled, spent_fuel_amount):
	return distance_traveled / spent_fuel_amount

def parse_result_in_string(number):
	return "{:.3f}".format(number)

print(parse_result_in_string(calculate_car_consumption(x, y)) + " km/l")