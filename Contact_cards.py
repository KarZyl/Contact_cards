class Card:
    def __init__(self, name, surname, company, position, email):
       self.name = name
       self.surname = surname
       self.company = company
       self.position = position
       self.email = email


card_1 = Card(name="Lauren", surname="McLain", company="Brooks Fashions", position="Line installer", email="LaurenBMcLain@teleworm.us")
card_2 = Card(name="Robin", surname="Moore", company="Pomeroy's", position="Mathematical statistician", email="RobinRMoore@teleworm.us")
card_3 = Card(name="John", surname="Harmon", company="The Sample", position="Nurse aide", email="JohnTHarmon@armyspy.com")
card_4 = Card(name="Albert", surname="Cannon", company="Kragen Auto Parts", position="Sawing machine operator", email="AlbertDCannon@armyspy.com")
card_5 = Card(name="Margarito", surname="Kennedy", company="Komerci", position="Nuclear technician", email="MargaritoWKennedy@rhyta.com")

List = []

List.append(card_1)
List.append(card_2)
List.append(card_3)
List.append(card_4)
List.append(card_5)  

  
for a in List:
    print(a.name, a.surname, a.email)