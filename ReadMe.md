The idea is, we have some columns in a table/dataframe
and we want to create new columns which receives a value based
on specific conditions. We want to realise this in a reusable manner.
Those conditions are expressions on existing columns.
We can have multiple expressions on multiple columns.
Example:

Hour of Day |   Budget    | Spend | Overspend midday (hour>12 and spend>10)  
    11      |     100     |  20   |   No  
    12      |     100     |  5    |   No  
    13      |     100     |  10   |   No  
    14      |     100     |  20   |   Yes  


For that i created two examples. One that pretty much uses the hardcode approach
and one that utilizes objects and functional programming to create a reusable solution
