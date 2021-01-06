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
        accepted_chars = {'1', '2', '3', '4'}
        modified_answer = ""

        if user_answer == 'exit':
            exit(0)

        for char in user_answer:
            if char in accepted_chars:
                modified_answer += char

        if len(modified_answer) >= 1:
            if propose_correct_answer(user_answer, modified_answer[0]):
                return modified_answer[0]
            else:
                continue
        elif modified_answer == "":
            print(f"Podana odpowiedź {user_answer} jest niepoprawna. Aby zakończyć wpisz : exit")


def propose_correct_answer(user_answer, proposition):
    yes_or_no = input(f"Podana odpowiedź {user_answer} jest niepoprawna, czy chiałeś wybrać {proposition} ? [t/n] : ")
    if yes_or_no == 'exit':
        exit(0)
    elif yes_or_no == 't' or yes_or_no == 'T':
        return True
    else:
        return False


if __name__ == "__main__":
    math_operation = choose_operation("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    user_input = input("Podaj składnik 1. ")
    first_number = float(user_input)

    user_input = input("Podaj składnik 2. ")
    second_number = float(user_input)

    result = make_calculations(first_number, second_number, math_operation)

    print(f"Wynik to {result}")
