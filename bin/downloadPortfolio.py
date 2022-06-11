from tinkoff.invest.channels import create_channel
from tinkoff.invest.grpc.instruments_pb2 import INSTRUMENT_ID_TYPE_FIGI
from tinkoff.invest.services import Services


def get_portfolio_positions(token, account_id):
    portfolio = get_portfolio(token=token, account_id=account_id)
    return portfolio.positions


def map_figi_with_ticker_for_positions(positions, token):
    ticker_position_map = {}
    for position in positions:
        ticker_position_map[position.figi] = get_instrument_ticker(position.figi, token=token)
    return ticker_position_map


def get_instrument_ticker(figi, token):
    channel = create_channel()
    service = Services(channel, token)
    response = service.instruments.get_instrument_by(id_type=INSTRUMENT_ID_TYPE_FIGI, id=figi)
    return response.instrument.ticker


def portfolio_total_amounts(token, account_id):
    portfolio = get_portfolio(token=token, account_id=account_id)
    total_book = {'BONDS': [portfolio.total_amount_bonds.units, portfolio.total_amount_bonds.currency],
                  'CASH': [portfolio.total_amount_currencies.units, portfolio.total_amount_currencies.currency],
                  'ETF': [portfolio.total_amount_etf.units, portfolio.total_amount_etf.currency],
                  'FUTURES': [portfolio.total_amount_futures.units, portfolio.total_amount_futures.currency],
                  'SHARES': [portfolio.total_amount_shares.units, portfolio.total_amount_shares.currency]}
    return total_book


def get_portfolio_cash(token, account_id):
    return get_portfolio(token=token, account_id=account_id).total_amount_currencies


def get_portfolio(token, account_id):
    channel = create_channel()
    service = Services(channel, token)
    return service.operations.get_portfolio(account_id=account_id)
