import pandas

# •    How does the spending (ARPU) of vendor37 users after closure compare to the spending of the users of other vendors?
# To solve this problem we use the following process:
# Get list of vendor37 users
# Calculate spending before
# Calculate spending after

revenue_data = pandas.read_csv('./m_mock_transaction_20190621.csv')
vendor_37_data = revenue_data[revenue_data['vendor'] == "vendor37"]
vendor_37_users = list(vendor_37_data['account'])
total_users = list(revenue_data['account'])
print("The number of vendor 37 users is ", len(vendor_37_users))
print("The number of total users is ", len(total_users))
print("The proportion of vendor 37 users is ", len(vendor_37_users) / len(total_users))

# The number of vendor 37 users is  1879
# The number of total users is  729200
# The proportion of vendor 37 users is  0.0025767964893033462

revenue_data_early = revenue_data[revenue_data["month"] < 4]
revenue_data_late = revenue_data[revenue_data["month"] >= 4]
revenue_data_early_vendor_37_users = revenue_data_early[revenue_data_early['account'].isin(vendor_37_users)].sum(axis=0)['revenue']
revenue_data_early_other_users = revenue_data_early[-revenue_data_early['account'].isin(vendor_37_users)].sum(axis=0)['revenue']
revenue_data_late_vendor_37_users = revenue_data_late[revenue_data_late['account'].isin(vendor_37_users)].sum(axis=0)['revenue']
revenue_data_late_other_users = revenue_data_late[-revenue_data_late['account'].isin(vendor_37_users)].sum(axis=0)['revenue']
print("Before April 1st the revenue for vendor 37 users was ", revenue_data_early_vendor_37_users)
print("Before April 1st the revenue for non vendor 37 users was ", revenue_data_early_other_users)
print("On or after April 1st the revenue for vendor 37 users was ", revenue_data_late_vendor_37_users)
print("On or after April 1st the revenue for non vendor 37 users was ", revenue_data_late_other_users)
print("Vendor37 users spent the following proportion of total revenue before closure: ", revenue_data_early_vendor_37_users/revenue_data_early_other_users)
print("Vendor37 users spent the following proportion of total revenue after closure: ", revenue_data_late_vendor_37_users/revenue_data_late_other_users)

# Before April 1st the revenue for vendor 37 users was  194205.37664692578
# Before April 1st the revenue for non vendor 37 users was  23695891.757704634
# On or after April 1st the revenue for vendor 37 users was  13472.825412197373
# On or after April 1st the revenue for non vendor 37 users was  17035421.18248418
# Vendor37 users spent the following proportion of total revenue before closure:  0.00819574036852952
# Vendor37 users spent the following proportion of total revenue after closure:  0.0007908712833029413

# To answer the business question, the spending of vendor 37 users after the closure is smaller than the spending of other users (per user) since 0.0007908712833029413 < 0.0025767964893033462
# The vendor 37 users actually spend more than other users before the closure though.

# •    Is there any indication that vendor37 users have migrated to new vendors?

# Yes, but only a tenth of them since 0.0007908712833029413 is only about a tenth of 0.00819574036852952

