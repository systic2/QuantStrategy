from ChangeDataFrame import *
from MakeFRDataFrame import *
from MakeInvestDataFrame import *

firmcode_list = ['A005930', 'A005380', 'A035420', 'A003550', 'A034730']

for num, code in enumerate(firmcode_list):
    fs_df = make_fs_dataframe(code)
    fs_df_changed = change_df(code, fs_df)
    if num == 0:
        total_fs = fs_df_changed
    else:
        total_fs = pd.concat([total_fs, fs_df_changed])
print(total_fs)

for num, code in enumerate(firmcode_list):
    fr_df = make_fr_dataframe(code)
    fr_df_changed = change_df(code, fr_df)
    if num == 0:
        total_fr = fr_df_changed
    else:
        total_fr = pd.concat([total_fr, fr_df_changed])
print(total_fr)

for num, code in enumerate(firmcode_list):
    invest_df = make_invest_dataframe(code)
    invest_df_changed = change_df(code, invest_df)
    if num == 0:
        total_invest = invest_df_changed
    else:
        total_invest = pd.concat([total_invest, invest_df_changed])
print(total_invest)
