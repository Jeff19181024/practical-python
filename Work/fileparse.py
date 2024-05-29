# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        if delimiter:
            rows = csv.reader(f, delimiter=delimiter)
        else:
            rows = csv.reader(f)

        if has_headers:
            headers = next(rows)
        # Read the file headers
        records = []

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        for row in rows:
            if not row:    # Skip rows with no data
                continue
            
            if indices:
                row = [ row[index] for index in indices]

            if types:
                row = [ func(val) for func, val in zip(types, row) ]

            if not has_headers:
                records.append(tuple(row))
                continue

            record = dict(zip(headers, row))
            records.append(record)

    return records