def monthlyPaymentPlan(principal, interest, year):
    p = int(principal)
    y = int(year)
    r = float(interest)

    r = (r * 0.01) / 12
    y = y * 12
    return int((p * r * (1 + r) ** y) / ((1 + r) ** y - 1))

print(monthlyPaymentPlan(10000000, 2.8, 4)) # should print 220460