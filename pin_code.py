tions = {
    '0': '08',
    '1': '124',
    '2': '2153',
    '3': '326',
    '4': '4157',
    '5': '52684',
    '6': '6359',
    '7': '748',
    '8': '87590',
    '9': '968'
}


def pin_one_digit(count_odo):
    current_bit = original_pin[len(count_odo)]  # запоминает текущий разряд введенного пинкода для передачи в цикл
    for p in options[str(current_bit)]:
        if len(count_odo) + 1 == len(original_pin):
            # print(count_odo + p)
            result_list.append(count_odo + p)
        elif len(count_odo) < len(original_pin):
            res = count_odo + p
            pin_one_digit(res)
    result_string = ' '.join(result_list)
    return f'Количество возможных пинкодов:{len(result_list)}\n{result_string}'


result_list = []
original_pin = input('введите пинкод: ')
print(pin_one_digit(''))

'''
    if len(count_odo) + 1 == len(original_pin):
        digit_num = len(short_pin) + 1
        for p in options[str(digit_num)]:
            print(short_pin + p)
    elif len(short_pin) < len(original_pin):
        digit_num = len(short_pin) + 1
        for p in options[str(digit_num)]:
            res = short_pin + p
            pin_one_digit(res)
    elif len(short_pin) >= len(original_pin):
        print('Ошибка! Слишком длинный пинкод')


# '''
