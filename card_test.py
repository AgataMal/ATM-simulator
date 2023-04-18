from card import Card
import unittest
from user import User


class UnitTests(unittest.TestCase):

    def test_valid_pin_code(self):
        visa_card = Card(1234, User("Jan", "Kowal"))
        self.assertTrue(visa_card.check_pin_code(1234)) #to do! validation to 4 digits
