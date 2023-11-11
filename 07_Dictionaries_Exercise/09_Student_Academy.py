student_data = {}

num_pairs_of_rows = int(input())

for _ in range(num_pairs_of_rows):
    student_name = input()
    student_grade = float(input())

    if student_name not in student_data:
        student_data[student_name] = []
    student_data[student_name].append(student_grade)

for student_name, grades in student_data.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student_name} -> {average_grade:.2f}")
