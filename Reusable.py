import pandas as pd
from TableExpression import TableExpression

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
expression = TableExpression()
expression.add_condition('hour_of_day', lambda x: x>12)
expression.add_condition('spend', lambda x: x>10)

df['Overspend midday'] = df.apply(lambda x: 'Yes' if(expression.allmatch(x)) else 'No', axis=1)

#you can even combine multiple expression blocks:

expression1 = TableExpression()
expression2 = TableExpression()

expression1.add_condition('spend', lambda x: x<10)
expression1.add_condition('hour_of_day', lambda x: x<13)

expression2.add_condition('spend', lambda x: x >= 20)
expression2.add_condition('hour_of_day', lambda x: x >= 13)

df['combined_expressions'] = df.apply(lambda x: 'Yes' if(expression1.anymatch(x) or expression2.allmatch(x)) else 'No', axis=1)
print(df)