# mortgage.py
#
# Exercise 1.7

p = 500000
r = 0.05
payment = 2684.11
ex = payment + float(input("extra here"))
total = 0
i = 1
mb = int(input("start month"))
mu = int(input("end here"))
m = 0

while p > 0:
    if mb <= i <= mu:
        p = p * (1 + r/12) - ex
        total = total + ex
        i = i + 1
    else:
        p = p * (1 + r/12) - payment
        total = total + payment
    m = m + 1
    print(m, total, p)

print("Total paid", total)
print("months", m)