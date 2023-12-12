def grade(marks):
    if 90 <= marks <= 100:
        return 10
    elif 80 <= marks < 90:
        return 9
    elif 70 <= marks < 80:
        return 8
    elif 60 <= marks < 70:
        return 7
    elif 50 <= marks < 60:
        return 6
    else:
        return 0

subjects= ["subj1","subj2","subj3","subj4","subj5"]
total_grade = 0 

for subject in subjects:
    marks = float(input("enter marks"))
    if 0<marks<=100:
        gradepo = grade(marks)
        total_grade += gradepo
        print(f"grade point for {subject} : {gradepo}")
    else:
        print("enter correct marks")
print(f"total grade point: {total_grade}")