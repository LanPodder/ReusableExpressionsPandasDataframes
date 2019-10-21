import pandas as pd

"""
The idea is, we have some columns in a table/dataframe
and we want to create new columns which receive a value based
on specific conditions. We want to realise this in a reusable manner.
Those conditions are expressions on existing columns.
We can have multiple expressions on multiple columns.
Example:

Hour of Day |   Budget    | Spend | Overspend midday (hour>12 and spend>10)
    11      |     100     |  20   |   No
    12      |     100     |  5    |   No
    13      |     100     |  10   |   No
    14      |     100     |  20   |   Yes

"""

df = pd.DataFrame(
    [
        [11, 100, 20],
        [12, 100, 5],
        [13, 100, 10],
        [14, 100, 20],
        [15, 100, 5],
    ],
    columns=['hour_of_day', 'budget', 'spend']
    )

df['Overspend midday'] = df.apply(lambda x: 'Yes' if(x['hour_of_day']>12 and x['spend']>10) else 'No', axis=1)
print(df)