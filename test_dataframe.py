'''
This module contains functions that check a DataFrame for various
attributes.
'''
import csv_to_df

# use csv_to_df to create dataframe using Pronto data
DF = csv_to_df.create_dataframe(
    'https://data.seattle.gov/api/views/tw7j-dfaw/'
    'rows.csv?accessType=DOWNLOAD')

def test_create_dataframe():
    '''test_create_dataframe  data frame for conditions specified in homework 2
    Test of DF for the following attributes:
        the columns in columns
        at least 10 entries
        that all datatypes in the DataFrame are the same

    Errors are raised if the conditions are not met

    Args:
        none (DataFrame created above)

    Returns:
        a_bool (bool): True if df passes tests, False otherwise

    '''
    # create a slice of df and a column list to check against
    d_f_1 = DF.iloc[:, [4, 11]]
    columns1 = d_f_1.columns.tolist()

    # set output to True, then look for conditions to turn False.
    a_bool = True
    # check whether data frame contains only the columns listed in input
    # 'columns'
    # first, sort column list alaphabetically in case columns is not in same
    # order as the columns in df
    if d_f_1.columns.tolist().sort() != columns1.sort():
        a_bool = False
        raise NameError('Columns in data frame do not match supplied'
                        'columns list')
    # check number of entries in data frame
    if len(d_f_1) <= 10:
        a_bool = False
        raise ValueError('Less than 10 lines in dataframe')

    # take 'set' of dypes in df. If length is 1, all data types are the same.
    if len(set(d_f_1.dtypes)) != 1:
        a_bool = False
        raise TypeError('Columns contain different data types')

    return a_bool

# test dataframe for atleast one row
def test_dataframe_length():
    '''Redundant function to test that the DataFrame above has at least one
    line.
    '''
    if DF.empty:
        raise ValueError('dataframe empty!')

def test_dataframe_nan():
    '''check DataFrame for nan values, raise ValueError if found'''
    # loop through columns
    for column in DF.columns.tolist():
        for i in range(len(DF[column])):
            if DF[column][i] != DF[column][i]:
                raise ValueError('NAN located in %s on line %d' %(column, i))

def test_dataframe_types():
    '''check to make sure data types within a column match'''
    # loop through columns
    for column in DF.columns.tolist():
        # find type of first entry
        data_type = type(DF[column][0])
        # loop through rows to check if the types match that of the first rows
        for i in range(len(DF[column])):
            if data_type == type(DF[column][i]):
                continue
            else:
                raise TypeError('data types in %s do not match' %column)
