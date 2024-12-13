#  create function that's read data from excel sheet and print it

def read_data_from_excel():
    """ read data from excel """
    import pandas as pd
    df = pd.read_excel('data.xlsx')
    print(df)