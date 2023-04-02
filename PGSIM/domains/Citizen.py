class Citizen:
    def __init__(self, name, id, DoB, nationality, place_of_origin, place_of_residence, marriage, spouse):
        self.name = name
        self.id = id
        self.DoB = DoB
        self.nationality = nationality
        self.place_of_origin = place_of_origin
        self.place_of_residence = place_of_residence
        self.marriage = marriage
        self.marriage_certificate = {}
        self.spouse = spouse
