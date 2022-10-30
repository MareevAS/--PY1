def get_count_char(str_):

    str_ = str_.lower()

    for element in str_:
        if element.isalpha():
            if element in letters_dict:
                letters_dict[element] += 1
            else:
                letters_dict[element] = 1

    return letters_dict


def get_distribution_char(dict_):

    to_percent = sum(dict_.values()) / 100

    for letter in dict_:
        dict_[letter] = dict_[letter] / to_percent

    # print(sum(dict_.values())) # сумма процентных соотношений должна быть равна 100% (равна)

    return dict_


letters_dict = {}

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
print(get_distribution_char(get_count_char(main_str)))
