import pandas as pd

class StudentFailException(Exception):
    pass

def read_grades_file(filename):
    df = pd.read_csv(filename)
    results = []
    for i, row in df.iterrows():
        name = row[0]
        grades = row[1:]
        average_grade = grades.mean()
        try:
            if average_grade >= 70:
                pass_fail_status = 'Pass'
            else:
                pass_fail_status = 'Fail'
                raise StudentFailException('Failed')
        except StudentFailException:
            pass
        print(f'{name}: {average_grade} ({pass_fail_status})')

if __name__ == '__main__':
    try:
        results = read_grades_file('student_grades.csv')
    except FileNotFoundError:
        print('Error: File not found')

