import pandas as pd

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