array_char = ['а', 'б', 'в', 'г', 'д', 'е', 'е', 'ж', 'з', 'и', 'й',
              'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
              'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


# Возврат соответствующего числа для символа
def get_number_char(char: str) -> int:
    for idx in range(len(array_char)):
        if char == array_char[idx]:
            return idx + 1
    return 0


# Создание матрицы для расчетов
def build_matrix(text: str):
    lower_text = text.lower()
    array_strings = lower_text.split()
    array_strings.append(lower_text)
    count_strings = len(array_strings)
    mass_result = [[0 for j in range(5)] for i in range(count_strings)]

    for i in range(count_strings):
        mass_result[i][4] = array_strings[i]

    return mass_result


# Подсчет числа по правилу одного
def calc_one_number(num: int) -> int:
    if num < 10:
        return num

    while num > 9:
        result = 0
        for number in str(num):
            result = result + int(number)
        num = result

    return num


# Подсчет числа по правилу Таро
def calc_taro_number(num: int) -> int:
    if num < 22:
        return num

    while num > 21:
        result = 0
        for number in str(num):
            result = result + int(number)
        num = result

    return num


# Подсчет чисел для матрицы
def calc_sum_char(input_matrix):
    for i in range(len(input_matrix)):
        input_matrix[i][0] = len(input_matrix[i][4])
        sum_char: int = 0
        for ch in input_matrix[i][4]:
            sum_char = sum_char + get_number_char(ch)
        input_matrix[i][1] = sum_char
        input_matrix[i][2] = calc_taro_number(sum_char)
        input_matrix[i][3] = calc_one_number(sum_char)


def print_matrix(matrix):
    header_strings = ['Число букв', 'Общая сумма', 'По правилу Таро', 'По правилу одного', 'Строка']
    print("{:═>12}{:═>14}{:═>18}{:═>20}{:═>20}".format('╦', '╦', '╦', '╦', ''))
    print("{:<10s} ║ {:<11s} ║ {:<15s} ║ {:<17s} ║ {:s}".format(*header_strings))
    print("{:═>12}{:═>14}{:═>18}{:═>20}{:═>20}".format('╬', '╬', '╬', '╬', ''))
    for i in range(len(matrix)):
        print("{:^10d} ║ {:^11d} ║ {:^15d} ║ {:^17d} ║ {:s}".format(*matrix[i]))


if __name__ == '__main__':
    input_text = input("Введите предложение: ")
    matrix_result = build_matrix(input_text)
    calc_sum_char(matrix_result)
    sum_result: int = 0

    print_matrix(matrix_result)
