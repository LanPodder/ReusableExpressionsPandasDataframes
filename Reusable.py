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


expression1 = TableExpression()\
    .add_condition('spend', lambda x: x<10)\
    .add_condition('hour_of_day', lambda x: x<13)

expression2 = TableExpression()\
    .add_condition('spend', lambda x: x >= 20)\
    .add_condition('hour_of_day', lambda x: x >= 13)

df['combined_expressions'] = df.apply(lambda x: 'Yes' if(expression1.anymatch(x) or expression2.allmatch(x)) else 'No', axis=1)

#or even instantiate them directly inside a list if you have a ton of different expressions
expression_list = [
    TableExpression()
        .add_condition('spend', lambda x: x+2 < 10)
        .add_condition('hour_of_day', lambda x: x==12),
    TableExpression()
        .add_condition('spend', lambda x: x > 10)
        .add_condition('hour_of_day', lambda x: x == 13),
    TableExpression()
        .add_condition('spend', lambda x: x >= 20)
        .add_condition('hour_of_day', lambda x: x >= 14)
]

#and for instance check if any expression block is true for expression.allmatch
def any_expression_all_match(expression_list, x):
    for expression in expression_list:
        if(expression.allmatch(x)):
            return True
    return False

df['list_of_expr'] = df.apply(lambda x: 'Yes' if(any_expression_all_match(expression_list, x)) else 'No', axis=1)

print(df)