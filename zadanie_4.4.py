def make_calculations(first_no, second_no, math_operation):
    if math_operation == 1:
        print(f"Dodaje {first_no} i {second_no}")
        return first_no + second_no
    elif math_operation == 2:
        print(f"Odejmuję {first_no} i {second_no}")
        return first_no - second_no
    elif math_operation == 3:
        print(f"Mnożę {first_no} i {second_no}")
        return first_no * second_no
    elif math_operation == 4:
        print(f'Dzielę {first_no} i {second_no}')
        return first_no / second_no


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


if __name__ == "__main__":
    math_operation = choose_operation("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    first_number = numbers_only_input("Podaj składnik 1. ")
    second_number = numbers_only_input("Podaj składnik 2. ")
    result = make_calculations(first_number, second_number, math_operation)

    print(f"Wynik to {result}")
