src = not False and True or False and not True

# TODO расписать упрощение выражения
# result = true and true or false and false - избавились от отрицаний
# result = true or false - избавились от "и"
# result = true - избавились от "или"

result = True  # TODO подставить результат выражения

print(src == result)
