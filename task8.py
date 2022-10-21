money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05


def lifetime(money_cap, sal, sp, inc):

    month = 0   # количество месяцев, которое можно прожить
    sum_cash = money_cap

    while True:
        sum_cash += sal - sp*((1+inc)**month)

        if sum_cash < 0:
            break
        else:
            month += 1

    print(month)

    pass


lifetime(money_capital, salary, spend, increase)
