from MakeFSDataFrame import *


def change_df(firm_code, dataframe):
    for num, col in enumerate(dataframe.columns):
        temp_df = pd.DataFrame({firm_code: dataframe[col]})
        temp_df = temp_df.T
        temp_df.columns = [[col] * len(dataframe), temp_df.columns]
        if num == 0:
            total_df = temp_df
        else:
            total_df = pd.merge(total_df, temp_df, how='outer', left_index=True, right_index=True)
    return total_df
