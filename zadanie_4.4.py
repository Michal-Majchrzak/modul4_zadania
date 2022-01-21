import logging
import re
logging.basicConfig(level=logging.DEBUG)


def choose_operation(prompt_user):
    operation_regex = re.compile(r'^[1-4]$')
    while True:
        user_answer = input(prompt_user)
        user_answer = user_answer.strip()

        if user_answer == 'exit':
            exit(0)

        if operation_regex.match(user_answer):
            print(f'Wybrano : {user_answer}')
            return int(user_answer)
        else:
            print(f"Podana odpowiedź {user_answer} jest niepoprawna. Aby zakończyć wpisz : exit")


def collect_numbers(prompt_user):
    user_answer = input(prompt_user)
    user_answer = user_answer.strip()

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


def numbers_only_input(prompt_user):
    numbers_only_regex = re.compile(r'^[-]?\d+([,.]\d+)?$')

    while True:
        user_answer = input(prompt_user)
        user_answer = user_answer.strip()
        user_answer = user_answer.replace(',', '.')

        if user_answer == 'exit':
            exit(0)

        if numbers_only_regex.match(user_answer):
            print(f'Wprowadzono : {user_answer}')
            return float(user_answer)
        else:
            print(f"Podana odpowiedź {user_answer} jest niepoprawna. Aby zakończyć wpisz : exit")



def make_calculations(numbers_list, math_operation):

    if math_operation == 4 and 0 in numbers_list[1:]:
        logging.error("Jedna z liczb przez które próbujesz dzielić to 0.")
        return str("Błąd - dzielenie przez zero.")

    result = numbers_list[0]

    for number in numbers_list[1:]:
        if math_operation == 1:
            result += number
        elif math_operation == 2:
            result -= number
        elif math_operation == 3:
            result *= number
        elif math_operation == 4:
            result /= number

    math_op_dict = {1: "Dodaję", 2: "Odejmuję", 3: "Mnożę", 4: "Dzielę"}
    logging.info(f"{math_op_dict[math_operation]} {str(numbers_list)[1:-1]}")
    return result


if __name__ == "__main__":
    chosen_operation = choose_operation("Podaj działanie, posługując sie odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    elements_list = collect_numbers("Proszę podać ilość elementów : ")
    calculations_result = make_calculations(elements_list, chosen_operation)

    print(f"Wynik to : {calculations_result}")
