import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(left=orders, right=company, how='inner', on='com_id')
    red_sales = df[df['name'] == 'RED']['sales_id']
    return sales_person[~sales_person['sales_id'].isin(red_sales)][['name']]