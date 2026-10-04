"""calculate the student's grade based on the scores from the input and
the predefined weights for each category"""

EXAM_WEIGHT = 0.5
ASSIGNMENT_WEIGHT = 0.3
QUIZ_WEIGHT = 0.2

midterm_exam_grade = float(input("Please enter midterm grade: "))
final_exam_grade = float(input("Please enter final exam grade: "))
assignment_one = float(input("Please enter first assignment grade: "))
assignment_two = float(input("Please enter second assignment grade: "))
quiz_one = float(input("Please enter first quiz grade: "))
quiz_two = float(input("Please enter second quiz grade: "))

if midterm_exam_grade >= 0 and midterm_exam_grade <= 100 and final_exam_grade >= 0 and final_exam_grade <= 100:
    exam_grade = (midterm_exam_grade + final_exam_grade) / 2 * EXAM_WEIGHT
else:
    print("Invalid input. Please enter exams within the 0 - 100 range.")
    exam_grade = 0

if assignment_one >= 0 and assignment_one <= 30 and assignment_two >= 0 and assignment_two <= 30:
    assignment_grade = ((assignment_one + assignment_two) /
                        2 / 30 * 100) * ASSIGNMENT_WEIGHT
else:
    print("Invalid input. Please enter assignments within the 0 - 30 range.")
    assignment_grade = 0

if quiz_one >= 0 and quiz_one <= 20 and quiz_two >= 0 and quiz_two <= 20:
    quiz_grade = ((quiz_one + quiz_two) / 2 / 20 * 100) * QUIZ_WEIGHT
else:
    print("Invalid input. Please enter quizzes within the 0 - 20 range.")
    quiz_grade = 0

final_grade = exam_grade + assignment_grade + quiz_grade

print(f"The students final grade is {final_grade:.2f}%")
