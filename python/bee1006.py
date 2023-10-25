# Problem Link: https://www.beecrowd.com.br/judge/en/problems/view/1006

grade_a = float(input())
grade_b = float(input())
grade_c = float(input())

def calculate_student_average(grade_a, grade_b, grade_c):
	return ((grade_a * 2) + (grade_b * 3) + (grade_c * 5)) / 10

print("MEDIA = " + "{:.1f}".format(calculate_student_average(grade_a, grade_b, grade_c)))