students = ["Aman", "Riya", "Rahul", "Sneha"]
marks = [85, 92, 56, 78]


def calculate_average(scores):
    """Return the average of the given scores."""
    total = 0
    student_count = len(scores)
    for score in scores:
        total = total + score
    average = total / student_count
    return average


def count_above_average(scores):
    """Return how many scores are above the class average."""
    average = calculate_average(scores)
    count = 0
    for score in scores:
        if score > average:
            count = count + 1
    return count


print("Student Marks:")
for student, score in zip(students, marks):
    print(f"{student} scored {score}")

print("Class Average:", calculate_average(marks))
print("Students above average:", count_above_average(marks))
