import pandas as pd
import numpy as np

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    col = f'getNthHighestSalary({N})'
    unique_salary = employee.salary.unique()
    if len(unique_salary) < N or N <= 0:
        return pd.DataFrame([np.NaN], columns=[col])
    else:
        salary = sorted(unique_salary, reverse=True)[N-1]
        return pd.DataFrame([salary], columns=[col])