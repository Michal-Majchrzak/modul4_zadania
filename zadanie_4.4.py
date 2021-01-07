def make_calculations(numbers_list, math_operation):
    result = 0

    if math_operation == 3 and 0 in numbers_list:
        return 0

    if math_operation == 4 and 0 in numbers_list[1:]:
        print("Nie dzielimy przez 0!")
        return "Błąd - dzielenie przez 0."

    for index, number in enumerate(numbers_list):
        if index == 0:
            result = numbers_list[index]
            continue
        elif math_operation == 1:
            result += number
        elif math_operation == 2:
            result -= number
        elif math_operation == 3:
            result *= number
        elif math_operation == 4:
            result /= number

    return result


def choose_operation(prompt_user):
    while True:
        user_answer = input(prompt_user)

        if user_answer == 'exit':
            exit(0)

        numbers_only = 0
        if user_answer != '':
            numbers_only = int(''.join(char for char in user_answer if char.isdigit()))

        if 4 >= numbers_only >= 1:
            return numbers_only
        else:
            print(f"Podana odpowiedź {user_answer} jest niepoprawna. Aby zakończyć wpisz : exit")


def numbers_only_input(prompt_user):
    accepted_chars = {'-', '.', ','}

    while True:
        user_answer = input(prompt_user)

        if user_answer == 'exit':
            exit(0)

        semi_acceptable_answer = ''.join(char for char in user_answer if char.isdigit() or char in accepted_chars)
        semi_acceptable_answer = semi_acceptable_answer.replace(',', '.')

        if semi_acceptable_answer != '':
            is_negative = (semi_acceptable_answer[0] == '-')
            number_elements = semi_acceptable_answer.rsplit('.', maxsplit=1)
            acceptable_answer = ''

            if len(number_elements) == 1:
                acceptable_answer = ''.join(char for char in number_elements[0] if char.isdigit())
            else:
                acceptable_answer = ''.join(char for char in number_elements[0] if char.isdigit())
                acceptable_answer += '.' + number_elements[1]

            if is_negative:
                return -float(acceptable_answer)
            else:
                return float(acceptable_answer)
        else:
            print(f"Podana odpowiedź {user_answer} jest niepoprawna. Aby zakończyć wpisz : exit")


def collect_numbers(prompt_user):
    user_answer = input(prompt_user)

    if user_answer == 'exit':
        exit(0)

    only_digits = ''.join(char for char in user_answer if char.isdigit())

    if only_digits == '':
        print(f"Nie wybrano żadnych cyfr. Przyjmuję standardowe 2 elementy.")
        only_digits = 2
    elif int(only_digits) <= 1:
        print(f"Wybrano 1 lub mniej elementów. Przyjmuję standardowe 2 elementy.")
        only_digits = 2
    else:
        only_digits = int(only_digits)

    numbers_list = []
    for element in range(1, only_digits+1):
        numbers_list.append(numbers_only_input(f"Podaj składnik {element} "))

    return numbers_list


if __name__ == "__main__":
    math_operation = choose_operation("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    elements_list = collect_numbers("Proszę podać ilość elementów : ")
    calulations_result = make_calculations(elements_list, math_operation)

    print(f"Wynik to {calulations_result}")
