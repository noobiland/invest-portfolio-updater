from downloadPortfolio import get_portfolio_positions, map_figi_with_ticker_for_positions, portfolio_total_amounts, \
    get_portfolio_cash
from excelManager import update_total_report, update_positions_report
from propertiesReader import get_token, get_account_id, get_positions_report_file_name, get_total_report_file_name


def main():
    token = get_token()
    account_id = get_account_id()
    positions_report_file_name = get_positions_report_file_name()
    total_report_file_name = get_total_report_file_name()

    portfolio_positions = get_portfolio_positions(token=token, account_id=account_id)

    update_positions_report(positions_report_file_name=positions_report_file_name,
                            portfolio_positions=portfolio_positions,
                            figi_ticker_map=map_figi_with_ticker_for_positions(portfolio_positions, token=token),
                            cash=get_portfolio_cash(token=token, account_id=account_id))

    update_total_report(total_report_file_name=total_report_file_name,
                        total_book=portfolio_total_amounts(token=token, account_id=account_id))


if __name__ == '__main__':
    main()
