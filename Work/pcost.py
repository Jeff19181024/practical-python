# pcost.py
#
# Exercise 1.27
import sys

#print(sum)

def portfolio_cost(filename):
    sum = 0
    with open(filename) as file:
        next(file)
        for line in file:
            tmp = line.split(',')
            try:
                sum = sum + int(tmp[1]) * float(tmp[2])
            except ValueError:
                print('Error in', line)

    return sum
    

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
