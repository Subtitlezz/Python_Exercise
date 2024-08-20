student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    if student_scores[student] >= 91 and student_scores[student] <= 100:
        student_grades[student] = 'Outstanding'
    elif student_scores[student] >= 81 and student_scores[student] <= 90:
        student_grades[student] = 'Exceeds Expectations'
    elif student_scores[student] >= 71 and student_scores[student] <= 80:
        student_grades[student] = 'Acceptable'
    else:
          student_grades[student] = 'Fail'


ask_for_name = str(input("What is your name? "))

if ask_for_name in student_grades:
    print(f'{ask_for_name} you {student_grades[ask_for_name]} this term')