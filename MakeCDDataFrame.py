import pandas as pd
import openpyxl


def make_code(x):
    x = str(x)
    return 'A' + '0'*(6-len(x)) + x


path = r'/Users/systic/PycharmProjects/QuantStrategy/data_4236_20230125.xlsx'
code_data = pd.read_excel(path, engine='openpyxl')
code_data = code_data[['종목코드', '종목명']]
code_data['종목코드'] = code_data['종목코드'].apply(make_code)

print(code_data)

