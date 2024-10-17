import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[(patients['conditions'].str.contains(r'\sDIAB1'))|(patients['conditions'].str.startswith('DIAB1'))]