import pytest
import pandas as pd
from datacompare import compare as cp


def test_compare_datasets():
    df1 = pd.DataFrame({'A': ['A0', 'A1', 'A6', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})
    df2 = pd.DataFrame({'A': ['A0', 'A1', 'A6', 'A7'],
                        'B': ['B0', 'B5', 'B6', 'B7'],
                        'C': ['C0', 'C5', 'C2', 'C7'],
                        'D': ['D0', 'D5', 'D2', 'D7']})

    df1_keys = ['A']
    df2_keys = ['A']
    df1_columns_to_compare = ['B']
    df2_columns_to_compare = ['B']
    df1_columns_to_compare = list(column + '_x' for column in df1.columns.difference(df1_keys))
    df2_columns_to_compare = list(column + '_y' for column in df2.columns.difference(df2_keys))

    df_result = cp.compare_datasets(df1, df2, df1_keys, df2_keys,
                                    df1_columns_to_compare,
                                    df2_columns_to_compare)

    assert len(df_result) == 5
    assert df_result['equals'].where(df_result['equals']).count() == 1
    assert df_result['only_in_df1'].where(df_result['only_in_df1']).count() == 1
    assert df_result['only_in_df2'].where(df_result['only_in_df2']).count() == 1
