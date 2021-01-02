def check_for_palindrome(word=""):
    """
        Check if given word (string) is a palindrome.
        :param word: String to evaluate
        :return: boolean True or False
    """
    lowercase_word = word.lower()
    reversed_word = lowercase_word[::-1]
    if lowercase_word == reversed_word:
        return True
    else:
        return False
