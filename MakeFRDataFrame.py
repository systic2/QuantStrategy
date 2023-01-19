import requests
import pandas as pd

def make_fr_dataframe(firm_code):
    fr_url = f'https://comp.fnguide.com/SVO2/ASP/SVD_FinanceRatio.asp?pGB=1&gicode={firm_code}' \
             f'&cID=&MenuYn=Y&ReportGB=D&NewMenuID=104&stkGb=701'
    fr_page = requests.get(fr_url)
    fr_tables = pd.read_html(fr_page.text)

    temp_df = fr_tables[0]
    temp_df = temp_df.set_index(temp_df.columns[0])
    temp_df = temp_df.loc[
        [
            '유동비율계산에 참여한 계정 펼치기',
            '부채비율계산에 참여한 계정 펼치기',
            '영업이익률계산에 참여한 계정 펼치기',
            'ROA계산에 참여한 계정 펼치기',
            'ROIC계산에 참여한 계정 펼치기'
        ]
    ]
    temp_df.index = ['유동비율', '부채비율', '영업이익률', 'ROA', 'ROIC']
    return temp_df