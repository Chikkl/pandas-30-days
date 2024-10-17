import pandas as pd
import numpy as np

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    col_name = 'SecondHighestSalary'
    if len(employee['salary'].unique()) < 2:
        return pd.DataFrame({col_name: [np.NaN]})
    salary = sorted(employee['salary'].unique(), reverse=True)[1]
    return pd.DataFrame({col_name: [salary]})