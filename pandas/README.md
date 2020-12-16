# Difference between 2 rows

Assume you have a dataframe (`df`) like



start_date_time  end_date_time
2018-03-14       2018-03-15
2018-03-15       2018-03-16
2018-03-16       2018-03-17
2018-03-17       2018-03-18
2018-03-18       2018-03-19
2018-03-20       2018-03-21


And you want to calculate the difference between two rows, you can use the `diff` method

`df.diff()`

start_date_time  end_date_time
NaT              NaT
1 days           1 days
1 days           1 days
1 days           1 days
1 days           1 days
1 days           1 days
2 days           2 days
