company_employees = {}

while True:
    command = input()
    if command == "End":
        break

    company_name, employee_id = command.split(" -> ")

    if company_name not in company_employees:
        company_employees[company_name] = []

    if employee_id not in company_employees[company_name]:
        company_employees[company_name].append(employee_id)

for company_name, employee_ids in company_employees.items():
    print(f"{company_name}")
    for employee_id in employee_ids:
        print(f"-- {employee_id}")
