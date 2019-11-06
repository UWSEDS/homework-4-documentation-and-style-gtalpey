'''
This module contains functions used to import a csv to pandas DataFrame and to
perform
'''

import pandas as pd

# load csv to data DataFrame
def create_dataframe(url):
    '''Create a DataFrame using csv data online

    Args:
        url (str): url that points to a csv data file

    Return:
        d_f (pandas DataFrame): DataFrame of the data in url

    '''
    d_f = pd.read_csv(url)
    return d_f


# check data frame for columns in columns, at least 10 entries and that all
# datatypes are the same
def test_create_datadrame(d_f, columns):
    '''Test of df for the following attributes:
        the columns in columns
        at least 10 entries
        that all datatypes in the DataFrame are the same

    Args:
        d_f (pandas DataFrame): a DataFrame to be tested
        columns (list of strings): names of columns to check for in df

    Returns:
        a_bool (bool): True if df passes tests, False otherwise

    '''
    # set output to True, then look for conditions to turn False.
    a_bool = True
    # check whether data frame contains only the columns listed in input
    # 'columns'
    # first, sort column list alaphabetically in case columns
    # is not in same order as the columns in df
    if d_f.columns.tolist().sort() != columns.sort():
        a_bool = False
    # check number of entries in data frame
    elif len(d_f) <= 10:
        a_bool = False
    # take 'set' of dypes in df. If length is 1, all data types are the same.
    elif len(set(d_f.dtypes)) != 1:
        a_bool = False
    return a_bool
