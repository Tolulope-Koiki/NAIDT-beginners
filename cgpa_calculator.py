def calculate_cgpa():
    """Calculates the CGPA using a 5-point grading scale."""

    total_points = 0
    total_credits = 0

    while True:
        grade = input("Enter grade (A, B, C, D, F, or Q to quit): ")
        if grade.upper() == 'Q':
            break

        credits = int(input("Enter credits for the course: "))

        grade_points = assign_points(grade)
        total_points += grade_points * credits
        total_credits += credits

    cgpa = total_points / total_credits
    return cgpa

def assign_points(grade):
    """Assigns grade points based on the 5-point scale."""

    points = {
        'A': 5,
        'B': 4,
        'C': 3,
        'D': 2,
        'F': 0
    }
    return points.get(grade.upper(), 0)  # Handle invalid grades gracefully

# Get user input and calculate CGPA
cgpa = calculate_cgpa()

# Print the CGPA
p
rint("Your CGPA is:", cgpa)
