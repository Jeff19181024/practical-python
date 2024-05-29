# report.py
#
# Exercise 2.4

import csv
from pprint import pprint

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []
    total_cost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                record['shares'] = int(record['shares'])
                record['price'] = float(record['price'])
                total_cost += record['shares'] * record['price']
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
            portfolio.append(record)
    return portfolio, total_cost


def read_prices(filename):
    h = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                h[row[0]] = float(row[1])
            except IndexError:
                print('reach the bottom')
    return h

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfolio_filename, prices_filename):
    port, cost = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    report = []
    for row in port:
        tmp = row['name'], row['shares'], prices[row['name']], prices[row['name']] - row['price'] 
        report.append(tmp)

    print_report(report)


