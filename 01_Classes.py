# Python Object-Oriented Programming.


class Employee:

    def __init__(self, first, last, pay):
        """
        initiative method '__init__'
        "self" is a instance
        """
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    """Each method within a class take instance(self) as a first argument """

    def fullname(self):
        """
        another 'method' within a class.
        """
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1)
# print(emp_2)

# print(emp_1.email)  # # Instance variable 'email'
# print(emp_2.email)
# print(emp_1.first)  # # Instance variable 'first'

# print('{} {}'.format(emp_1.first, emp_1.last))  # # instance variables 'first' and 'last'.
# print(emp_1.fullname())  # # Method from Class.
# print(emp_1.fullname)  # # will print method accept return value.


""" 
Running from the class
and 'print(emp_1.fullname())'
Both are same...
"""

print(Employee.fullname(emp_1))
