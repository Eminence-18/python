CORRECT_AMOUNT_MSG = "correct amount"
INCORRECT_AMOUNT_MSG = "incorrect amount"

def check_swords_for_army(number_of_swords, number_of_soldiers):
    result = INCORRECT_AMOUNT_MSG
    if number_of_swords == number_of_soldiers:
      result = CORRECT_AMOUNT_MSG
    print(result)
    return result
