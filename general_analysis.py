import pandas

# •    Before closure – what did revenue look like for vendor37?
# •    Proportion of total revenue

revenue_data = pandas.read_csv('./m_mock_transaction_20190621.csv')
# is_2002 =  gapminder['year']==2002
# gapminder[is_2002]
vendor_37_data = revenue_data[revenue_data['vendor'] == "vendor37"]
vendor_37_data_early = vendor_37_data[vendor_37_data["month"] < 4]

vendor_revenue = vendor_37_data_early.sum(axis=0)['revenue']
total_revenue = revenue_data.sum(axis=0)['revenue']
proportion = vendor_revenue / total_revenue

print("Vendor revenue is ", vendor_revenue)
print("Total revenue is ", total_revenue)
print("Proportion is ", proportion)

# Output:
# Vendor revenue is  174497.4830410723
# Total revenue is  23890097.134351883
# Proportion is  0.00730417637315338