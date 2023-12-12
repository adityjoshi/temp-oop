def gradeCal(score):
    if 90 <= score <= 100:
        return "O"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"

students = 5
subjects = 5

scores = []
grades = []

for i in range(students):
    assignment = float(input(f"Assignment marks {i+1}: "))
    testTotal = float(input(f"Test marks {i+1}: "))
    lab = float(input(f"Lab marks {i+1}: "))

    scoredmarks = 0.1 * assignment + 0.7 * testTotal + 0.2 * lab
    grades.append(gradeCal(scoredmarks))
    scores.append(scoredmarks)

for i in range(students):
    print(f"\nStudent {i + 1}:")
    print(f"Final Test Score: {scores[i]}")
    print(f"Grade: {grades[i]}")
