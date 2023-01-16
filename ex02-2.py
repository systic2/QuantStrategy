import pandas as pd

df_ex2 = pd.DataFrame({'가격':[100, 140, 155, 70, 90],
                       'PER':[1.1, 0.8, 0.7, 2.3, 3.9],
                       '거래량':[1000, 800, 890, 700, 2000]},
                      index=['a', 'b', 'c', 'd', 'e'])
print(df_ex2)
print("=========================")
print(df_ex2[df_ex2['가격']>=100])
print("=========================")
print(df_ex2[df_ex2['거래량']<1000])
print("=========================")
print(df_ex2['PER'].sort_values())
print("=========================")
print(df_ex2['PER'].sort_values(ascending=False))
print("=========================")
print(df_ex2.sort_values(by='PER'))
print("=========================")
print(df_ex2.sort_values(by='PER', ascending=False))
print("=========================")
print(df_ex2['거래량'].rank())
print("=========================")
print(df_ex2['거래량'].rank(ascending=False))

