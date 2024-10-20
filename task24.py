import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df=actor_director.groupby(["actor_id","director_id"]).count().reset_index()
    final=df[df["timestamp"]>=3]
    return final[["actor_id","director_id"]]
    