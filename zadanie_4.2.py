def check_for_palindrome(potential_palindrome=""):
    """
        Check if given string is a palindrome.
        :param potential_palindrome: String to evaluate
        :return: boolean True or False
    """
    str_to_evaluate = ""

    for char in potential_palindrome:
        if char.isalnum():
            str_to_evaluate += char.lower()

    reversed_str_to_evaluate = str_to_evaluate[::-1]

    if str_to_evaluate == reversed_str_to_evaluate:
        return True
    else:
        return False
