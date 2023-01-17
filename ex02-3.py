import pandas as pd
import operator
import openpyxl

file_path = '/Users/systic/PycharmProjects/QuantStrategy/마법공식 데이터.xlsx'

# df = pd.read_excel(file_path, sheet_name='PER')
# print(df)

per_data = pd.read_excel(file_path, sheet_name='PER', index_col=0)
# print(per_data)
filtered_per = per_data[per_data['PER'] > 0]
# print(filtered_per)
sorted_per = filtered_per.sort_values(by='PER')
# print(sorted_per)
ranked_per = sorted_per['PER'].rank()
# print(ranked_per)
sorted_per['PER랭킹'] = sorted_per['PER'].rank()
# print(sorted_per)

roa_data = pd.read_excel(file_path, sheet_name='ROA', index_col=0)
# print(roa_data)
filtered_roa = roa_data.dropna()
# print(filtered_roa)
filtered_roa.columns = ['ROA']
# print(filtered_roa)
sorted_roa = filtered_roa.sort_values(by='ROA', ascending=False)
sorted_roa['ROA랭킹'] = sorted_roa['ROA'].rank(ascending=False)
# print(sorted_roa)
total_df = pd.merge(sorted_per, sorted_roa, how='inner', left_index=True, right_index=True)
# print(total_df)
total_df['종합 랭크'] = (total_df['PER랭킹'] + total_df['ROA랭킹']).rank()
sorted_total = total_df.sort_values(by='종합 랭크')
print(sorted_total)