def make_calculations(first_no, second_no, math_operation):
    if math_operation == '1':
        print(f"Dodaje {first_no} i {second_no}")
        return first_no + second_no
    elif math_operation == '2':
        print(f"Odejmuję {first_no} i {second_no}")
        return first_no - second_no
    elif math_operation == '3':
        print(f"Mnożę {first_no} i {second_no}")
        return first_no * second_no
    elif math_operation == '4':
        print(f'Dzielę {first_no} i {second_no}')
        return first_no / second_no


def choose_operation(prompt_user):
    user_answer = input(prompt_user)
    accepted_chars = {'1', '2', '3', '4'}
    verified_answer = ""

    for char in user_answer:
        if char in accepted_chars:
            verified_answer += char

    if len(verified_answer) > 1 or user_answer is not verified_answer:
        yes_or_no = input(f"Podano niepoprawną odpowiedź, czy chiałeś wybrać {verified_answer[0]} ? [t/n] : ")
        if yes_or_no == 't' or yes_or_no == 'T':
            return verified_answer[0]
        else:
            print(f"Podana odpowiedź : {user_answer} jest błędna, program zakończony.")
            exit(1)


if __name__ == "__main__":
    math_operation = choose_operation("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    user_input = input("Podaj składnik 1. ")
    first_number = float(user_input)

    user_input = input("Podaj składnik 2. ")
    second_number = float(user_input)

    result = make_calculations(first_number, second_number, math_operation)

    print(f"Wynik to {result}")
