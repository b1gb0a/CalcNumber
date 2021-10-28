array_char = ['а', 'б', 'в', 'г', 'д', 'е', 'е', 'ж', 'з', 'и', 'й',
              'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
              'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


# Возврат соответствующего числа для символа
def get_number_char(char: str) -> int:
    for idx in range(len(array_char)):
        if char == array_char[idx]:
            return idx + 1
    return 0


def build_matrix(text: str):
    array_strings = text.lower().split()
    array_strings.append(text)
    count_strings = len(array_strings)
    mass_result = [[0 for j in range(5)] for i in range(count_strings)]

    for i in range(count_strings):
        mass_result[i][4] = array_strings[i]

    return mass_result


def calc_one_number(num: int) -> int:
    return 0


def calc_taro_number(num: int) -> int:
    return 0


def calc_sum_char(input_matrix):
    for i in range(len(input_matrix)):
        input_matrix[i][0] = len(input_matrix[i][4])
        sum_char: int = 0
        for ch in input_matrix[i][4]:
            sum_char = sum_char + get_number_char(ch)
        input_matrix[i][1] = sum_char
        input_matrix[i][2] = calc_taro_number(sum_char)
        input_matrix[i][3] = calc_one_number(sum_char)


if __name__ == '__main__':
    inputText = input("Введите предложение: ")
    matrix_result = build_matrix(inputText)
    calc_sum_char(matrix_result)
    sumResult: int = 0

    print("Вывод")
