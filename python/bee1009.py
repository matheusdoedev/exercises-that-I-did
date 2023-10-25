# Problem Link: https://www.beecrowd.com.br/judge/en/problems/view/1009

sellers_name = input()
sellers_fixed_salary = float(input())
sellers_sales_total = float(input())

def calculate_sellers_salary(fixed_salary, sales_total):
	return fixed_salary + (sales_total * 0.15)

print("TOTAL = R$ " + "{:.2f}".format(calculate_sellers_salary(sellers_fixed_salary, sellers_sales_total)))