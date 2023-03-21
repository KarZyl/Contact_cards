from faker import Faker
fake = Faker()

class BaseContact:
     def __init__(self, name, surname, email, number):
       self.name = name
       self.surname = surname
       self.email = email
       self.number = number
       # Variables
       self._label_length = len(self.name) + len(self.surname)
     def __str__(self):
         return f'{self.name} {self.surname} {self.email} {self.number}'
     @property
     def label_length(self):
         return self._label_length
     @label_length.setter
     def label_length(self, value):
         self._label_length = value
     def contact(self):
         print(f"Wybieram numer {self.number} i dzwonię do {self.name} {self.surname}")


class BusinessContact(BaseContact):
    def __init__(self,company, position, work_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.work_number = work_number
        # Variables
        self._label_length = len(self.name) + len(self.surname)
    def __str__(self):
        return f'{self.name} {self.surname} {self.email} {self.position} {self.company} {self.work_number}'
    @property
    def label_length(self):
        return self._label_length
    @label_length.setter
    def label_length(self, value):
        self._label_length = value
    def contact(self):
        print(f"Wybieram numer {self.work_number} i dzwonię do {self.name} {self.surname}, {self.position} w {self.company}")


baseContact_list = []
businessContact_list = []

def create_contacts(contact_type, how_many_cards):
    if contact_type == BaseContact:
        for a in range (0, how_many_cards):
            name2 = fake.name()
            name2 = name2.split(" ")
            basecard = BaseContact(name=name2[0], surname=name2[1], email=fake.email(), number=fake.phone_number())
            baseContact_list.append(basecard)
            print(basecard)
        return baseContact_list
    elif contact_type == BusinessContact:
        for a in range (0, how_many_cards):
            name3 = fake.name()
            name3 = name3.split(" ")
            businesscard = BusinessContact(name=name3[0], surname=name3[1], number=0, email=fake.email(), position=fake.job(), company=fake.company(), work_number=fake.phone_number())
            businessContact_list.append(Businesscard)
            print(businesscard)
        return businessContact_list


#Run : create fake contacts and use method contact on first of them
create_contacts(BusinessContact, 4)
businessContact_list[0].contact()


#Sort contact_cards by name, surname and email adress- not used in current code version
def by_name():
    for a in sorted(List, key=lambda Card: Card.name):
        print(a.name, a.surname, a.email)
  
def by_surname():
    for a in sorted(List, key=lambda Card: Card.surname):
        print(a.surname, a.name, a.email)

def by_email():
    for a in sorted(List, key=lambda Card: Card.email):
        print(a.email, a.name, a.surname)
