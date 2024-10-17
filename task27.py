import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby("managerId", as_index = False).agg("count")
    return employee[employee["id"].isin(df[df["id"] >= 5]["managerId"].values)][["name"]]