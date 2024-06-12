class User:
    domain = 'itbhu.ac.in'
    branch = 'phy'

    def __init__(self, name, gender, contact) -> None:
        self.name = name.title()
        self.gender = gender
        self.contact = contact

    def nameSplit(self):
        x = self.name.split()
        firstname = ''.join(x[:-1])
        lastname = x[-1]
        return firstname, lastname

    def __str__(self) -> str:
        return f'<{self.firstname}.{self.lastname}>'

    def __repr__(self) -> str:
        return f'User(\'{self.firstname}\', \'{self.lastname}\')'
    
class Student(User):
    year = 2022

    def __init__(self, name, gender, contact, roll) -> None:
        super().__init__(name, gender, contact)
        name1, name2 = self.nameSplit()
        self.email = f'{name1.lower().replace(' ', '')}.{name2.lower()}.{User.branch}{Student.year%100}@{User.domain}'
        self.roll = roll
