import openpyxl
import pandas as pd
import operator

file_path = '/Users/systic/PycharmProjects/QuantStrategy/마법공식 데이터.xlsx'

per_sh = pd.read_excel(file_path, sheet_name='PER', engine='openpyxl')
per_sh_fix = per_sh[per_sh['PER'] > 0]
sorted_per = per_sh_fix.sort_values(by="PER", ascending=True)
# print(sorted_per)

per_rank = {}
for i in range(0, len(sorted_per)):
    per_rank[sorted_per.iloc[i][0]] = i + 1

# print(per_rank)

roa_sh = pd.read_excel(file_path, sheet_name='ROA', engine='openpyxl')

roa_sh_fix = roa_sh.dropna()
sorted_roa = roa_sh_fix.sort_values(by='ROA(영업이익)(%)', ascending=False)
# print(sorted_roa)
roa_rank = {}
for i in range(0, len(sorted_roa)):
    roa_rank[sorted_roa.iloc[i][0]] = i + 1
# print(roa_rank)

total_rank = {}
for name in roa_rank.keys():
    if name in per_rank.keys():
        total_rank[name] = per_rank[name] + roa_rank[name]

sorted_total = sorted(total_rank.items(), key=operator.itemgetter(1))

magic_rank = {}
for num, firm in enumerate(sorted_total):
    magic_rank[firm[0]] = num + 1

print(magic_rank)
