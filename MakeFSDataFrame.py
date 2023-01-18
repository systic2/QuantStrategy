import requests
import pandas as pd


def make_fs_dataframe(firm_code):
    fs_url = f"https://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode={firm_code}&cID=&MenuYn=Y&ReportGB=D" \
             "&NewMenuID=103&stkGb=701"
    fs_page = requests.get(fs_url)
    fs_tables = pd.read_html(fs_page.text)

    # print(fs_tables[0])
    temp_df = fs_tables[0]
    temp_df = temp_df.set_index(temp_df.columns[0])
    temp_df = temp_df[temp_df.columns[:4]]
    temp_df = temp_df.loc[['매출액', '영업이익', '당기순이익']]
    # print(temp_df)
    temp_df2 = fs_tables[2]
    temp_df2 = temp_df2.set_index(temp_df2.columns[0])
    temp_df2 = temp_df2.loc[['자산', '부채', '자본']]
    # print(temp_df2)

    temp_df3 = fs_tables[4]
    temp_df3 = temp_df3.set_index(temp_df3.columns[0])
    temp_df3 = temp_df3.loc[['영업활동으로인한현금흐름']]
    # print(temp_df3)
    fs_df = pd.concat([temp_df, temp_df2, temp_df3])

    return fs_df


result = make_fs_dataframe("A005380")
print(result)
