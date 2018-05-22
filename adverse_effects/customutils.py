import pandas as pd


def count(df, columns):
    df_category_count = pd.DataFrame(df.groupby(by=columns).size())
    df_category_count = df_category_count.reset_index()
    
    colnames = columns
    colnames.append('count')
    
    df_category_count.columns = colnames
    df_category_count = df_category_count.sort_values('count', ascending=False)
    
    return (df_category_count)
