"""HomeTask_13.

write class for bank card.
Class should reflect card lifecycle,
card operations etc.
use CVV, PIN, Name, Surname , end date,
card_num as initial params
class should have in addition to common logic
some class attributes, as minimum one class method and
as minimum  one staticmethod, two or more getters/setters
do not forget about block ""if __name__ == '__main__':""
"""

from datetime import datetime


class BankCard:
    """BankCard lifecycle class."""

    def __init__(self, card_num, cvv, pin, name, surname, end_date):
        """Initialize the data."""
        self.card_num = card_num
        self.cvv = cvv
        self.pin = pin
        self.name = name
        self.surname = surname
        self.end_date = self.end_date = datetime.strptime(end_date, '%m/%y')
        self.is_blocked = False

    @classmethod
    def generate_card_number(cls, self):
        """Generate a card number."""
        return self.generate_card_number()

    @staticmethod
    def validate_card_num(card_num):
        """Validate a card number."""
        if len(card_num) == 16 and card_num.isdigit():
            return True
        return False

    def block_card(self):
        """Initialize the status_card."""
        self.is_blocked = True

    def unblock_card(self):
        """Initialize the status_card."""
        self.is_blocked = False

    def is_expired(self):
        """Initialize the status_card."""
        return datetime.now() > self.end_date

    # Getters
    def get_card_num(self):
        """Initialize the card_num."""
        return self.card_num

    def get_name(self):
        """Initialize the name."""
        return self.name

    # Setters
    def set_pin(self, new_pin):
        """Initialize the pin."""
        self.pin = new_pin

    def set_cvv(self, new_cvv):
        """Initialize the cvv."""
        self.cvv = new_cvv


if __name__ == '__main__':
    card = BankCard('1234567812345678', '806', '7609', 'Name',
                    'Surname', '08/22')

    print('Card Number:', card.get_card_num())
    print('Name:', card.get_name())

    card.set_pin('2345')
    card.set_cvv('123')

    print('Updated PIN:', card.pin)
    print('Updated CVV:', card.cvv)

    print('Is Card Expired?', card.is_expired())

    card.block_card()
    print('Is Card Blocked?', card.is_blocked)

    card.unblock_card()
    print('Is Card Blocked?', card.is_blocked)
