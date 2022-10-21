salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

def how_much_money(sal, sp, time, inc):

     sum_spend = 0

     for i in range(months):
          sum_spend += sp * ((1 + inc) ** i)

     need_money = abs(sal * time - sum_spend)

     print(round(need_money))

how_much_money(salary, spend, months, increase)
