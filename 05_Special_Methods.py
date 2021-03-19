""" Special Dander Methods"""


class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

""" Both are same"""
# print(emp_1.__str__())
# print(emp_1.__repr__())

""" Dander __add__ method"""
# print(emp_1 + emp_2)

""" Dander __len__ method"""
# print(len(emp_1))

""" Knowledge"""
# print(1+2)
# print('a'+'b')
# # Both are same, that's how work in background
# print(int.__add__(1,2))
# print(str.__add__('a','b'))


# print(len('word'))
# print('word'.__len__()) # Dander len method
