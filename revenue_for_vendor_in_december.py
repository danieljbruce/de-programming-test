import pandas

revenue_data = pandas.read_csv('./m_mock_transaction_20190621.csv')

vendor_37_data_in_december = revenue_data[(revenue_data['vendor'] == "vendor37") & (revenue_data["month"] == 12)]
print(vendor_37_data_in_december)