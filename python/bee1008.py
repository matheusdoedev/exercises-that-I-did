# Problem Link: https://www.beecrowd.com.br/judge/en/problems/view/1008

employee_id = int(input())
employee_worked_hours = int(input())
employee_amount_per_hour = float(input())

def calculate_the_employee_month_salary(employee_worked_hours, employee_amount_per_hour):
	return employee_worked_hours * employee_amount_per_hour

print("NUMBER = " + employee_id.__str__())
print("SALARY = U$ " + "{:.2f}".format(calculate_the_employee_month_salary(employee_worked_hours, employee_amount_per_hour)))