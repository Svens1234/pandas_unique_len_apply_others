import numpy as np
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4],
                   'B': [123, 245, 321, 123],
                   'C': ['aaa', 'bbb', 'ccc', 'ddd']})

print(df)
print(df['B'].unique())
print(len(df['B'].unique()))
print(df['B'].nunique())
print(df['B'].value_counts()) #число 123 встречается один раз, число 245 и число 321 по одному разу
print(df)
print(df[df['A']<3])
print(df[(df['A']<3) & (df['B']<200)])
print(df)
print(df['A'].sum())


def times3(x):
    return x*3


print(df['A'].apply(times3))
print(df['A'].apply(times3).sum())
print(df['A'].apply(lambda x:x*3))
print(df['C'].apply(len))
print(df)
print(df.columns)
print(df.index)
print(df.sort_values('B')) #сортировка по значениям
print(df.isnull())

df1 = pd.DataFrame({'A': [1, 1, 1, 2, 2, 2],
                   'B': [123, 222, 222, 123, 123, 222],
                   'C': ['aaa', 'bbb', 'aaa', 'bbb', 'bbb', 'aaa'],
                   'D': [1, 2, 4, 3, 1, 5]})

print(df1)
print(df1.pivot_table(values='D', index=['A', 'B'], columns=['C']))
