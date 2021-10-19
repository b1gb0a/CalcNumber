array_char = ['а', 'б', 'в', 'г', 'д', 'е', 'е', 'ж', 'з', 'и', 'й',
              'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
              'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


def get_number_char(char):
    for idx in range(len(array_char)):
        if char == array_char[idx]:
            return idx+1


if __name__ == '__main__':
    inputText = input("Введите предложение: ")

    inputText = inputText.lower()

    sumResult = 0

    for ch in inputText:
        sumResult += get_number_char(ch)

    print(str(sumResult))
