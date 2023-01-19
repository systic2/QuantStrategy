import requests
import pandas as pd


def make_invest_dataframe(firm_code):
    invest_url = f'https://comp.fnguide.com/SVO2/ASP/SVD_Invest.asp?pGB=1&gicode={firm_code}' \
                 f'&cID=&MenuYn=Y&ReportGB=D&NewMenuID=105&stkGb=701'

    invest_page = requests.get(invest_url)
    invest_tables = pd.read_html(invest_page.text)

    temp_df = invest_tables[3]
    temp_df = temp_df.set_index(temp_df.columns[0])
    temp_df = temp_df.loc[
        [
            'PER계산에 참여한 계정 펼치기',
            'PCR계산에 참여한 계정 펼치기',
            'PSR계산에 참여한 계정 펼치기',
            'PBR계산에 참여한 계정 펼치기',
            '총현금흐름',
        ]
    ]
    temp_df.index = ['PER', 'PCR', 'PSR', 'PBR', '총현금흐름']
    return temp_df
