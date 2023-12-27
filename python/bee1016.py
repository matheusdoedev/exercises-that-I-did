# Problem Link: https://www.beecrowd.com.br/judge/en/problems/view/1016

def convert_speed_in_km_to_ms(speed_in_km):
	return speed_in_km / 3.6

def convert_km_to_m(km):
	return km * 1000

# speed must be in m/s, and time in s
def calculate_final_position(initial_position, speed, time):
	return initial_position + (speed * time)

# in km
distance = int(input())
car_x_speed_in_ms = convert_speed_in_km_to_ms(60)

print(car_x_speed_in_ms)

final_position_car_x = calculate_final_position(0, car_x_speed_in_ms, 3600)

print(final_position_car_x)

final_position_car_y = final_position_car_x + convert_km_to_m(distance)

print(final_position_car_y)

time = final_position_car_y / convert_speed_in_km_to_ms(90)

print(time / 60)