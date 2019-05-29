"""Object-oriented programming example.
"""


class InfoHeadShape:
    """A class for outputting a dataframe's info, head and shape at once!
    You will need to first import pandas as pd and assign variables as seen here:

    f = pd.DataFrame()
    example = f
    example = InfoHeadShape(f)"""

    def __init__(self, df):
        self.df = df

    def read_df(self):
        """User Input of csv file."""
        import pandas as pd

        csv = input("Paste path to CSV here: ")
        """paste path without ''. """
        self.df = pd.read_csv(csv)

    def df_info(self):
        """Show dataframe info."""
        print(self.df.info())

    def df_head(self):
        """How dataframe head."""
        print(self.df.head())

    def df_shape(self):
        """Shows dataframe shape."""
        print(self.df.shape)
        pass
