import pandas

revenue_data = pandas.read_csv('./m_mock_transaction_20190621.csv')

vendor_37_data = revenue_data[revenue_data['vendor'] == "vendor37"]