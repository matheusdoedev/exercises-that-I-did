# Problem Link: https://www.beecrowd.com.br/judge/en/problems/view/1005

grade_a = float(input())
grade_b = float(input())

def calculate_student_average(grade_a, grade_b):
	return ((grade_a * 3.5) + (grade_b * 7.5)) / 11

print("MEDIA = " + "{:.5f}".format(calculate_student_average(grade_a, grade_b)))