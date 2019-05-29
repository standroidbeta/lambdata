"""Object-oriented programming example.
"""


class InfoHeadShape:
    """A class for outputting a dataframe's info, head and shape at once!"""

    import pandas as pd
    import numpy as np

    def __init__(self, df):
        self.df = df

    def read_df(self, df_input):
        """User Input of csv file."""
        df_input = input("Enter path to CSV file here:")
        df = df_input

    def df_info(self, df):
        """Show dataframe info."""
        print(df.info())

    def df_head(self, df):
        """How dataframe head."""
        print(df.head())

    def df_shape(self, df):
        """Shows dataframe shape."""
        print(df.shape)
        pass
