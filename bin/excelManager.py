import pandas as pd


def update_positions_report(positions_report_file_name, portfolio_positions, figi_ticker_map, cash):
    dictionary = {}
    for position in portfolio_positions:
        dictionary[position.figi] = {'TICKER': figi_ticker_map[position.figi],
                                     'INSTRUMENT_TYPE': position.instrument_type,
                                     'CCY': position.current_price.currency,
                                     'QUANTITY': position.quantity.units,
                                     'AVG_PRICE': position.average_position_price.units,
                                     'CURRENT_PRICE': position.current_price.units}

    df = pd.DataFrame.from_dict(dictionary, orient='index')
    df.index.name = 'FIGI'
    df.loc['CASH'] = [None, 'ccy', cash.currency, cash.units, 1, 1]
    df.to_excel(positions_report_file_name)


def update_total_report(total_report_file_name, total_book):
    df = pd.DataFrame.from_dict(total_book, orient='index', columns=['AMOUNT', 'CCY'])
    df.index.name = 'INSTRUMENT_TYPE'
    df.loc['TOTAL'] = pd.Series(df['AMOUNT'].sum(), index=['AMOUNT'])
    df.to_excel(total_report_file_name)
