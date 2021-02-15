""" Difference between 'REGULAR METHOD','CLASS METHODS' and 'STATIC METHODS'. """

"""
                       --While working with classes-- 
(1) 'REGULAR METHOD' automatically pass the instance as a first argument and we call that 'self'.
(2) 'CLASS METHODS'  automatically pass the CLASS as a first argument and we call that 'cls'
(3) 'STATIC METHODS' don't pass anything automatically.
"""

import datetime


class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        """ Class method as a Alternative constructor """
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

""" After raise amount"""
# Employee.set_raise_amt(1.06)

# print(Employee.raise_amt)
# print(emp_2.raise_amt)
# print(emp_1.raise_amt)

"""Adding new employees with new Class method"""
# new_str_1 = 'John-Doe-7000'
# new_str_2 = 'Steve-Smith-30000'
# new_str_3 = 'Jane-Doe-90000'
#
# new_emp_1 = Employee.from_string(new_str_1)
# new_emp_2 = Employee.from_string(new_str_2)
# new_emp_3 = Employee.from_string(new_str_3)
#
# print(new_emp_1.email)
# print(Employee.num_of_emps)  # Added new 3 employees

""" Static method"""

my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))
