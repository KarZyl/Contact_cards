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
    def contact(self):
        print(f"Wybieram numer {self.work_number} i dzwonię do {self.name} {self.surname}, {self.position} w {self.company}")

def create_contacts(contact_type, how_many_cards):
    cards = []
    if contact_type == "P":
        for _ in range (0, how_many_cards):
            name = fake.name()
            name = name.split(" ")
            basecard = BaseContact(name=name[0], surname=name[1], email=fake.email(), number=fake.phone_number())
            cards.append(basecard)           
        return cards
    elif contact_type == "B":
        for _ in range (0, how_many_cards):
            name = fake.name()
            name = name.split(" ")
            businesscard = BusinessContact(name=name[0], surname=name[1], number=0, email=fake.email(), position=fake.job(), company=fake.company(), work_number=fake.phone_number())
            cards.append(businesscard)         
        return cards

#Sort contact_cards by name, surname and email adress
def by_name():
    return sorted(cards, key=lambda Card: Card.name)

def by_surname():
    return sorted(cards, key=lambda Card: Card.surname)

def by_email():
    return sorted(cards, key=lambda Card: Card.email)

#Run : create fake contacts, sort them by name and use method contact on first of them
cards = create_contacts("B", 4)
by_name()[0].contact()
