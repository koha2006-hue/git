from domains.Citizen import Citizen

class Marriage_certificate:
    def __init__(self, husband, wife, marriage_date, marriage_place):
        self.husband = husband
        self.wife = wife
        self.marriage_date = marriage_date
        self.marriage_place = marriage_place

    def print_marriage_certificate(self):
        print("Marriage certificate:")
        print("Husband's name: ", self.husband.name)
        print("Husband's ID: ", self.husband.id)
        print("Wife's name: ", self.wife.name)
        print("Wife's ID: ", self.wife.id)
        print("Date of marriage: ", self.marriage_date)
        print("Place of marriage: ", self.marriage_place)
