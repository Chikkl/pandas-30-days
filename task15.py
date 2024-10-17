import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products = products.melt(id_vars=['product_id'], value_vars=['store1','store2','store3'], value_name='price', var_name='store')
    products = products.dropna()
    return products