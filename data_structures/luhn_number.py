from __future__ import annotations


class LuhnNumber:

    def __init__(self, number: int):
        self.number = number

    def __eq__(self, other):

        if self is other:
            return True

        if not isinstance(other, self.__class__):
            return False

        return self.number == other.number

    def checksum(self) -> int:
        """Calculates the checksum of a number"""

        n = [int(char) for char in str(self.number)]
        sum_of_digits = 0

        for idx, num in enumerate(n[::-1]):

            if idx % 2 == 0:
                sum_of_digits += num
                continue

            double_num = num * 2
            if double_num > 9:
                double_num -= 9
            sum_of_digits += double_num

        return sum_of_digits

    def is_valid(self) -> bool:
        """Checks whether or not a number is a valid Luhn number"""

        return self.checksum() % 10 == 0

    @classmethod
    def create_luhn(cls, number: int) -> LuhnNumber:
        """Given a number, creates a valid Luhn number by adding one digit to the end of given number"""

        luhn = cls(number)
        if luhn.checksum() % 10 == 0:
            return luhn

        new_number = number * 10
        required = 10 - (cls(new_number).checksum() % 10)

        return cls(new_number + required)


luhn_number = LuhnNumber(79927398713)

assert luhn_number.checksum() == 70
assert luhn_number.is_valid() is True
assert LuhnNumber.create_luhn(7992739871) == LuhnNumber(79927398713)
