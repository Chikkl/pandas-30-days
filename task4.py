import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    viewer_equlas_author = views[views['author_id'] == views['viewer_id']]
    return pd.DataFrame({'id':sorted(viewer_equlas_author['author_id'].unique())})