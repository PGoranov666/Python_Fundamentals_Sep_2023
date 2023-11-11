course_data = {}

while True:
    command = input()
    if command == 'end':
        break
    course_name, student_name = command.split(" : ")

    if course_name not in course_data:
        course_data[course_name] = []
    course_data[course_name].append(student_name)

for course, students in course_data.items():
    print(f"{course}: {len(students)}")

    for student in students:
        print(f"-- {student}")
