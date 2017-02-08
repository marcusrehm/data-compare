import pandas as pd


def equals_condition(df1_columns_to_compare, df2_columns_to_compare):
    condition = []
    for col_x, col_y in zip(df1_columns_to_compare, df2_columns_to_compare):
        condition.append(col_x + ' == ' + col_y)
    return ' and '.join(condition)


def not_exists_condition(df_columns_to_compare):
    condition = []
    for col in df_columns_to_compare:
        condition.append(col)
    return ' + '.join(condition) + ' != ' + ' + '.join(condition)


def compare_datasets(df1, df2, df1_keys, df2_keys,
                     df1_columns_to_compare,
                     df2_columns_to_compare):
    df_result = pd.merge(df1, df2, how='outer', left_on=df1_keys, right_on=df2_keys)
    df_result.eval('equals = ' + equals_condition(df1_columns_to_compare, df2_columns_to_compare), inplace=True)
    df_result.eval('only_in_df1 = ' + not_exists_condition(df2_columns_to_compare), inplace=True)
    df_result.eval('only_in_df2 = ' + not_exists_condition(df1_columns_to_compare), inplace=True)
    return df_result
