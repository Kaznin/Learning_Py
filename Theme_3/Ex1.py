def cash(deposit, persent, years):
    return (deposit * (persent / 100) * years) + deposit

print(cash(1000, 10, 5))