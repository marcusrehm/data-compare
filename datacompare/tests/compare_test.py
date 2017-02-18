import pytest
import pandas as pd
import numpy as np
import datacompare as cp


def test_compare_datasets_with_same_column_names():
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

    df_result = cp.compare_datasets(df1, df2, df1_keys, df2_keys)
    assert len(df_result) == 5
    assert df_result['result'].where(df_result['result'] == 'equals').count() == 1
    assert df_result['result'].where(df_result['result'] == 'left_only').count() == 1
    assert df_result['result'].where(df_result['result'] == 'right_only').count() == 1


def test_compare_datasets_with_different_column_names():
    df1 = pd.DataFrame({'A': ['A0', 'A1', 'A6', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})
    df2 = pd.DataFrame({'Z': ['A0', 'A1', 'A6', 'A7'],
                        'N': ['B0', 'B5', 'B6', 'B7'],
                        'C': ['C0', 'C5', 'C2', 'C7'],
                        'W': ['D0', 'D5', 'D2', 'D7']})

    df1_keys = ['A']
    df2_keys = ['Z']
    df1_columns_to_compare = ['B', 'D']
    df2_columns_to_compare = ['N', 'W']

    df_result = cp.compare_datasets(df1, df2, df1_keys, df2_keys,
                                    df1_columns_to_compare,
                                    df2_columns_to_compare)
    print df_result.head()
    assert len(df_result) == 5
    assert df_result['result'].where(df_result['result'] == 'equals').count() == 1
    assert df_result['result'].where(df_result['result'] == 'left_only').count() == 1
    assert df_result['result'].where(df_result['result'] == 'right_only').count() == 1
