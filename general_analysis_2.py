import pandas

# •    Revenue / transactions per day through vendor37
# •    Regional usage details

revenue_data = pandas.read_csv('./m_mock_transaction_20190621.csv')
# is_2002 =  gapminder['year']==2002
# gapminder[is_2002]
vendor_37_data = revenue_data[revenue_data['vendor'] == "vendor37"]
vendor_37_data_early = vendor_37_data[vendor_37_data["month"] < 4]
vendor_revenue = vendor_37_data_early.sum(axis=0)['revenue']
print("Revenue per day (based on March, February, January and December) with no payments in December is ", vendor_revenue / (31+28+31+31))
regional_revenue_for_vendor_37 = vendor_37_data_early.groupby(['country_code']).sum(axis=0)['revenue']
print("Regional usage:")
print(regional_revenue_for_vendor_37)

# Output:
# Revenue per day (based on March, February, January and December) with no payments in December is  1442.1279590171264
# Regional usage:
# country_code
# country11       514.777510
# country119       96.858065
# country120       25.775117
# country124      124.705000
# country139      356.637187
# country141      124.705000
# country144       96.544871
# country16     16477.240869
# country168      249.409999
# country176      124.705000
# country18       138.563423
# country180       25.775117
# country181      249.409999
# country182     1223.183866
# country185      107.227188
# country194     2180.773248
# country196       16.941232
# country20      1022.203334
# country206      650.780274
# country207      509.267833
# country209      124.705000
# country211      492.335331
# country214    16390.610407
# country217    10587.316353
# country228      148.095104
# country28        96.544871
# country30       221.563065
# country32        96.858065
# country33        31.336235
# country35        96.544871
# country45     49904.493372
# country51      9763.318842
# country52      2510.068124
# country57       560.720072
# country6         25.775117
# country60       310.999247
# country61       521.599748
# country66     57643.564788
# country71       124.705000
# country85       406.140300
# country9        124.705000
# Name: revenue, dtype: float64