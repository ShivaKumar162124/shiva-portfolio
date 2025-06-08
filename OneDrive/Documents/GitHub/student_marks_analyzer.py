# Student Marks Analyzer - Simple Python Mini Project

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "Fail"

students = []

# Taking input for 5 students
for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    marks = float(input(f"Enter marks of {name}: "))
    students.append({'name': name, 'marks': marks})

# Displaying all students and grades
print("\nAll Students:")
for s in students:
    print(f"{s['name']} - {s['marks']} - Grade: {get_grade(s['marks'])}")

# Finding the topper
topper = max(students, key=lambda x: x['marks'])
print(f"\nTop Scorer: {topper['name']} with {topper['marks']} marks")

# Calculating average
avg = sum(s['marks'] for s in students) / len(students)
print(f"Average Marks: {avg:.2f}")
