import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    need_patients = patients[patients['conditions'].str.contains('DIAB1')]
    return need_patients