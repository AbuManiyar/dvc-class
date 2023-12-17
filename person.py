import pandas as pd


data = {
    'names':['abu', 'guru', 'arvind'],
    'place': ['rmd', 'gdg', 'gdg'],
    'year': [2000, 1999, 1998]
}

df = pd.DataFrame(data)
print(df)

df.to_csv('data/data.csv', index=False)