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
    while True:
        user_answer = input(prompt_user)
        numbers_only = int(''.join(char for char in user_answer if char.isdigit()))

        if user_answer == 'exit':
            exit(0)

        if 4 >= numbers_only >= 1:
            return numbers_only
        else:
            print(f"Podana odpowiedź {user_answer} jest niepoprawna. Aby zakończyć wpisz : exit")


if __name__ == "__main__":
    math_operation = choose_operation("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    user_input = input("Podaj składnik 1. ")
    first_number = float(user_input)

    user_input = input("Podaj składnik 2. ")
    second_number = float(user_input)

    result = make_calculations(first_number, second_number, math_operation)

    print(f"Wynik to {result}")
