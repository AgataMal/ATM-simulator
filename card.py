from user import *


class Card:
    __expiry_date = ""
    __card_number = ""
    __provider = ""
    # bank=

    def __init__(self, pin_code, owner: User):
        self.__pin_code = pin_code
        self.__owner = owner

    def check_pin_code(self, pin_code):
        return self.__pin_code == pin_code
