class Employee:
    """A class variables"""
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1
        # self.num_of_emps += 1  <-- if you do that, you can't track total no of emp.

    def fullname(self):
        """ 'self' is a instance and taken first argument by every methods within a class. """
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        """accessing 'class variable' though instance('self')"""
        self.pay = int(self.pay * self.raise_amount)

        """accessing 'class variable' though class it-self"""
        # self.pay = int(self.pay * Employee.raise_amount)

        # self.pay = int(self.pay * 1.04)


# print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
emp_3 = Employee('Bil', 'Gates', 290000)

""" We accessed The value of variable 'num_of_emps' with class it-self. And raise that value though class also not with 
instance. SO we can track total no of emp. Now....."""
# print(Employee.num_of_emps)

""" printing instance variable 'pay' """
# print(emp_1.pay)
""" now applying raise in it, which is a method in class """
emp_1.apply_raise()
# print(emp_1.pay)

""" Using class variable in global scope"""
""" Can accesses though class it-self as well as both instances """
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(emp_1.__dict__)
# print(Employee.__dict__)

"""Changing value of raise amount of whole class"""
Employee.raise_amount = 1.05

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

""" Changing value of raise amount of particular employ"""
# emp_1.raise_amount = 1.06
# # print(emp_1.__dict__)  # now emp_1 also containing raise amount variable in it dict.
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)  # Value only changed for this employ only.
# print(emp_2.raise_amount)
