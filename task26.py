import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    all_exams = students.merge(subjects, how='cross')
    exams_count = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    res = all_exams.merge(exams_count, on=['student_id', 'subject_name'], how='left').fillna({'attended_exams': 0}).sort_values(by=['student_id', 'subject_name'])
    return res
    