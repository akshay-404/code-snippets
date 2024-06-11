class User:
    domain = 'itbhu.ac.in'
    branch = 'phy'

    def __init__(self, name1, name2, contact) -> None:
        self.firstname = name1.capitalize()
        self.lastname = name2.capitalize()
        self.name = f'{self.firstname} {self.lastname}'
        self.contact = contact

    def __str__(self) -> str:
        return f'<{self.firstname}.{self.lastname}>'

    def __repr__(self) -> str:
        return f'User(\'{self.firstname}\', \'{self.lastname}\', {self.contact})'
    
class Student(User):
    pass


x = User('Akshay', 'Anil', 8848940385)
y = x


print(y)
