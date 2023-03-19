
#Define new class
class Card:
    def __init__(self, name, surname, company, position, email):
       self.name = name
       self.surname = surname
       self.company = company
       self.position = position
       self.email = email
    def __str__(self):
        return f'{self.name} {self.surname} {self.email}'

#Create database manually using Fake Name Generator
card_1 = Card(name="Lauren", surname="McLain", company="Brooks Fashions", position="Line installer", email="LaurenBMcLain@teleworm.us")
card_2 = Card(name="Robin", surname="Moore", company="Pomeroy's", position="Mathematical statistician", email="RobinRMoore@teleworm.us")
card_3 = Card(name="John", surname="Harmon", company="The Sample", position="Nurse aide", email="JohnTHarmon@armyspy.com")
card_4 = Card(name="Albert", surname="Cannon", company="Kragen Auto Parts", position="Sawing machine operator", email="AlbertDCannon@armyspy.com")
card_5 = Card(name="Margarito", surname="Kennedy", company="Komerci", position="Nuclear technician", email="MargaritoWKennedy@rhyta.com")

#Add one position using Faker:
from faker import Faker
fake = Faker()
Name1 = fake.name()
Name1 = Name1.split(" ")
card_F = Card(name=Name1[0], surname=Name1[1], company=fake.company(), position=fake.job(), email=fake.email())

#Print Name, Surname and Email from each contact card
List = [card_1, card_2, card_3, card_4, card_5, card_F]

def show_contacts():
    for a in List:
      print(a.name, a.surname, a.email, a.company)

#Sorted contact_cards by name, surname and email adress
def by_name():
    for a in sorted(List, key=lambda Card: Card.name):
        print(a.name, a.surname, a.email)
  
def by_surname():
    for a in sorted(List, key=lambda Card: Card.surname):
        print(a.surname, a.name, a.email)

def by_email():
    for a in sorted(List, key=lambda Card: Card.email):
        print(a.email, a.name, a.surname)

# Define classes based on "Card" inheritance
class BaseContact(Card):
    def __init__(self, number,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number = number
        self._label_length = len(self.name) + len(self.surname)
    
    @property
    def label_length(self):
        return self._label_length

    @label_length.setter
    def label_length(self, value):
        self._label_length = value

    def __str__(self):
        return f'{self.name} {self.surname} {self.email} {self.number}'


class BusinessContact(BaseContact):
    def __init__(self,work_number,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.work_number = work_number
        # Variables
        self._label_length = len(self.name) + len(self.surname)
    
    @property
    def label_length(self):
        return self._label_length

    @label_length.setter
    def label_length(self, value):
        self._label_length = value

    def __str__(self):
        return f'{self.name} {self.surname} {self.email} {self.position} {self.company} {self.work_number}'

#Input name to show private or corporate contact data      
def contact():
        print("Kontaktuję się z:  ")
        choice = input("Wpisz imię kontaktu  ")
        for a in BaseContact_list:
            if a.name == choice:
                print(f"Wybieram numer{a.number} i dzwonię do {a.name} {a.surname}")
        for a in BusinessContact_list:
            if a.name == choice:
                print(f"Wybieram numer {a.work_number} i dzwonię do {a.name} {a.surname}, {a.position} w {a.company}")


#Input which, Private (P) or Corporate (F), and how many fake contacts to ganerate
BaseContact_list = []
BusinessContact_list = []

def Create_contacts():
    type = input("Podaj typ wizytówki Podstawowa (P), Firmowa (F)")
    if type == "P":
        quantity = int(input("Podaj ilość wizytówek do wygenerowania "))
        for a in range (0, quantity):
            Name2 = fake.name()
            Name2 = Name2.split(" ")
            Basecard = BaseContact(name=Name2[0], surname=Name2[1], company=0, position=0, email=fake.email(), number=fake.phone_number())
            BaseContact_list.append(Basecard)
            print(Basecard)
        return BaseContact_list
    elif type == "F":
        quantity = int(input("Podaj ilość wizytówek do wygenerowania "))
        for a in range (0, quantity):
            Name3 = fake.name()
            Name3 = Name3.split(" ")
            Businesscard = BusinessContact(name=Name3[0], surname=Name3[1], number=0, email=fake.email(), position=fake.job(), company=fake.company(), work_number=fake.phone_number())
            BusinessContact_list.append(Businesscard)
            print(Businesscard)
        return BusinessContact_list
    else:
        print("Wybrano niewlaściwy znak")


#Run : create fake contacts and show data of one of them
Create_contacts()
contact()
