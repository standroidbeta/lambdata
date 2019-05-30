"""Object-oriented programming example.

Example use:

In: import oop_example
In: from oop_example import CSVLoad

In: example = CSVLoad()
In: example = CSVLoad.read_df
In: example(CSVLoad)

Out: Paste path to CSV here: >? /home/seek/Documents/GitHub/hp_df_clean.csv

In: from oop_example import InfoShapeHead
In: df_example = InfoHeadShape
In: df_example.df_ish(CSVLoad)

Out:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 78095 entries, 0 to 78094
Data columns (total 39 columns):
Unnamed: 0    78095 non-null int64
Class         78095 non-null int64
User          78095 non-null int64
X0            78095 non-null float64
Y0            78095 non-null float64
Z0            78095 non-null float64
X1            78095 non-null float64
Y1            78095 non-null float64
Z1            78095 non-null float64
X2            78095 non-null float64
Y2            78095 non-null float64
Z2            78095 non-null float64
X3            78095 non-null float64
Y3            78095 non-null float64
Z3            78095 non-null float64
X4            78095 non-null float64
Y4            78095 non-null float64
Z4            78095 non-null float64
X5            78095 non-null float64
Y5            78095 non-null float64
Z5            78095 non-null float64
X6            78095 non-null float64
Y6            78095 non-null float64
Z6            78095 non-null float64
X7            78095 non-null float64
Y7            78095 non-null float64
Z7            78095 non-null float64
X8            78095 non-null float64
Y8            78095 non-null float64
Z8            78095 non-null float64
X9            78095 non-null float64
Y9            78095 non-null float64
Z9            78095 non-null float64
X10           78095 non-null float64
Y10           78095 non-null float64
Z10           78095 non-null float64
X11           78095 non-null float64
Y11           78095 non-null float64
Z11           78095 non-null float64
dtypes: float64(36), int64(3)
memory usage: 23.2 MB
None
(78095, 39)
   Unnamed: 0  Class  User         X0         Y0 ...   Y10  Z10  X11  Y11  Z11
0           1      1     0  54.263880  71.466776 ...   2.9  2.9  2.9  2.9  2.9
1           2      1     0  56.527558  72.266609 ...   2.9  2.9  2.9  2.9  2.9
2           3      1     0  55.849928  72.469064 ...   2.9  2.9  2.9  2.9  2.9
3           4      1     0  55.329647  71.707275 ...   2.9  2.9  2.9  2.9  2.9
4           5      1     0  55.142401  71.435607 ...   2.9  2.9  2.9  2.9  2.9
[5 rows x 39 columns]

"""


class CSVLoad:
    """Class to Load CSV Dataset into a DataFrame"""

    def __init__(self):

        import pandas as pd

        df = pd.DataFrame()

        self.df = df

    def read_df(self):
        """User Input of csv file."""

        import pandas as pd

        csv = input("Paste path to CSV here: ")
        """paste path without ''. """
        self.df = pd.read_csv(csv)
        self.df = self.df


class InfoShapeHead(CSVLoad):
    """A class for outputting a DataFrame's info, shape, and head all at once!"""

    def df_ish(self):
        """Show DataFrame info."""
        print(self.df.info())
        """Shows DataFrame shape."""
        print(self.df.shape)
        """How DataFrame head."""
        print(self.df.head())
        pass
