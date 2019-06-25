import pandas

# • What is an upper bound for revenue loss following the closure?

proportion = 0.00730417637315338
vendor_revenue_before_shutdown = 174497.4830410723
vendor_revenue_per_day = 1442.1279590171264
print("An upper bound on the revenue generated based on historical trends is ", vendor_revenue_per_day * (30 + 31))

# • Number of users expected to be affected by the closure?
revenue_data = pandas.read_csv('./m_mock_transaction_20190621.csv')
vendor_37_data = revenue_data[revenue_data['vendor'] == "vendor37"]
vendor_37_users = list(vendor_37_data['account'])
print("The number of vendor 37 users is ", vendor_37_users)
# Output
# The number of vendor 37 users is 1879

# current_dataframe = pandas.merge(current_dataframe, df, on='end_seconds_since_unix_epoch')

# • Is there a measurable revenue change as a result of the closure (on April 1)?
revenue_data = pandas.read_csv('./m_mock_transaction_20190621.csv')
revenue_data_per_day = revenue_data.groupby(['month', 'day']).sum()
revenue_data_per_day_average = revenue_data_per_day.mean(axis=0)['revenue']
# .sum(axis=0)['revenue']
# revenue_data_april_1 = revenue_data[(revenue_data['month'] == 4) & (revenue_data['day'] == 1)]
revenue_data_after_closure = revenue_data[(revenue_data['month'] > 3)]
revenue_data_after_closure_per_day = revenue_data_after_closure.groupby(['month', 'day']).sum()
revenue_data_after_closure_per_day_average = revenue_data_after_closure_per_day.mean(axis=0)['revenue']
print("The revenue data per day average is ", revenue_data_per_day_average)
print("The revenue data per day average on or after April 1 is  ", revenue_data_after_closure_per_day_average)
print("Revenue was affected by the closure since it is only 3 quarters of what it was on average!")

# •    How about regionally?
# For every region there is certain to be change.
# I suppose we could focus on the amount of change for regions that correspond to vendor37, but this is slightly more complex

# Output:
# An upper bound on the revenue generated based on historical trends is  87969.8055000447
# The revenue data per day average is 224939.5117704075
# The revenue data per day average on or after April 1 is 187350.48360307404
# Revenue was affected by the closure since it is only 3 quarters of what it was on average!