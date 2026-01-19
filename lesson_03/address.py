
class Address:
    def __init__(self, index, city, street, house, apt):
        self.index =index
        self.city = city
        self.street = street
        self.house = house
        self.apt = apt

    def __str__(self):
          return(f" {self.index}, {self.city}, {self.street}, {self.house}, {self.apt}")
