import pandas as pd

ex1 = pd.Series([100, 500, 150])
print(ex1)

ex2 = pd.Series([100, 500, 150], index=['카카오', '삼성전자', '현대차'])
print(ex2)
print(ex2['카카오'])
print(ex2['현대차'])
print(ex2[1])

df_ex1 = pd.DataFrame({'가격':[100, 500, 150], 'PER':[0.5, 1.2, 0.2], 'ROA':[1.01, 3.1, 0.97]},
                  index=['카카오', '삼성전자', '현대차'])
print(df_ex1['가격'])
print(df_ex1['가격']['삼성전자'])
print(df_ex1.loc['카카오'])

