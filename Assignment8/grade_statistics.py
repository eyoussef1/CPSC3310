from pathlib import Path

GRADES_FILE = Path(__file__).resolve().parent / "grades.csv"

TEST_WEIGHT = 0.3
EXAM_WEIGHT = 0.3
DISCUSSION_WEIGHT = 0.2
PROJECT_WEIGHT = 0.2


def main():
    """Read the grades file, calculate weighted grades,
    and print a summary of grade ranges."""

    try:
        weight_final_list = []

        with open(GRADES_FILE, "r") as grades_file:
            grades_file.readline()

            for line in grades_file:
                if line.strip():
                    row = line.strip().split(",")
                    final_grade = process_row(row)
                    weight_final_list.append(final_grade)

        analyze_grade(weight_final_list)

    except FileNotFoundError:
        print("Error: grades.csv file was not found.")

    except Exception as error:
        print(f"Error processing grades file: {error}")


def process_row(row):
    """Calculate one student's weighted final grade."""

    test_avg = average_subject(row[2:6])
    exam_avg = average_subject(row[6:8])
    discussion_avg = average_subject(row[8:10])
    project_score = float(row[10])

    return weight_final(
        test_avg,
        exam_avg,
        discussion_avg,
        project_score
    )


def average_subject(subject_list):
    """Return the average of the scores in subject_list."""

    total = 0

    for score in subject_list:
        total += float(score)

    average = total / len(subject_list)

    return average


def weight_final(test_avg, exam_avg, discussion_avg, project_score):
    """Calculate the weighted final grade."""

    final_grade = (
        test_avg * TEST_WEIGHT
        + exam_avg * EXAM_WEIGHT
        + discussion_avg * DISCUSSION_WEIGHT
        + project_score * PROJECT_WEIGHT
    )

    return final_grade


def analyze_grade(weight_final_list):
    """Count students in each final grade range."""

    grade_90 = 0
    grade_80 = 0
    grade_70 = 0
    grade_60 = 0
    below_60 = 0

    for grade in weight_final_list:
        if grade >= 90:
            grade_90 += 1
        elif grade >= 80:
            grade_80 += 1
        elif grade >= 70:
            grade_70 += 1
        elif grade >= 60:
            grade_60 += 1
        else:
            below_60 += 1

    print(f"Number of students with final grade 90 or above: {grade_90}")
    print(f"Number of students with final grade 80-89: {grade_80}")
    print(f"Number of students with final grade 70-79: {grade_70}")
    print(f"Number of students with final grade 60-69: {grade_60}")
    print(f"Number of students with final grade below 60: {below_60}")


if __name__ == "__main__":
    main()
