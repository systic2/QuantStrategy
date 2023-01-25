from MakeCDDataFrame import *
from ChangeDataFrame import *
import time

for num, code in enumerate(code_data['종목코드']):
    try:
        print(num, code)
        time.sleep(1)
        try:
            fs_df = make_fs_dataframe(code)
        except requests.exceptions.Timeout:
            time.sleep(60)
            fs_df = make_fs_dataframe(code)
        fs_df_changed = change_df(code, fs_df)
        if num == 0:
            total_fs = fs_df_changed
        else:
            total_fs = pd.concat([total_fs, fs_df_changed])
    except ValueError:
        continue
    except KeyError:
        continue

print(total_fs)
total_fs.to_excel(r'/Users/systic/PycharmProjects/QuantStrategy/재무제표데이터.xlsx')