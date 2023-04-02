from domains.Citizen import Citizen
from domains.Marriage_certificate import Marriage_certificate
class Management:
    def __init__(self):
        self.citizen = {}
        self.marriage = {}
        self.divorce = {}
        self.birth = {}
        self.death = {}
    def add_citizen(self):
        name=input("Name: ")
        id=input("ID: ")
        DoB=input("Date of birth: ")
        nationality= ("Nationality: ")
        place_of_origin=input("Place of origin: ")
        place_of_residence=input("Place of residence: ")
        marriage=input("Marriage status: ")
        while marriage!="married" and marriage!="single":
            print("Invalid input.")
            marriage=input("Marriage status: ")
        if marriage=="single":
            spouse="None"
        else:
            spouse=input("Spouse: ")
        self.citizen[id]= Citizen(name,id,DoB,nationality,place_of_origin,place_of_residence,marriage,spouse)

    def add_marriage(self):
        husband_name=input("Name of the first Citizen: ")
        while husband_name not in self.citizen:
            print ("The first Citizen does not exist.")
            husband_name=input("Name of the first Citizen: ")
        husband_id=input("ID of the first Citizen: ")
        while husband_id not in self.citizen:
            print ("The first Citizen does not exist.")
            husband_id=input("ID of the first Citizen: ")
        wife_name=input("Name of the second Citizen: ")
        while wife_name not in self.citizen:
            print ("The second Citizen does not exist.")
            wife_name=input("Name of the second Citizen: ")
        wife_id=input("ID of the second Citizen: ")
        while wife_id not in self.citizen:
            print ("The second Citizen does not exist.")
            wife_id=input("ID of the second Citizen: ")
        marriage_date=input("Date of marriage: ")
        marriage_place=input("Place of marriage: ")
        self.marriage_certificate[husband_id]=Marriage_certificate(husband_name,husband_id,wife_name,wife_id,marriage_date,marriage_place)
        self.citizen[husband_id].marriage="married"
        self.citizen[husband_id].spouse=wife_name
        self.citizen[wife_id].marriage="married"
        self.citizen[wife_id].spouse=husband_name
    def print_marriage_certificate(self):
        print("Marriage certificate:")
        print("Husband's name: ", self.husband.name)
        print("Husband's ID: ", self.husband.id)
        print("Wife's name: ", self.wife.name)
        print("Wife's ID: ", self.wife.id)
        print("Date of marriage: ", self.marriage_date)
        print("Place of marriage: ", self.marriage_place)
    def print_divorce_certificate(self):
        print("Divorce certificate:")
        print("Husband's name: ", self.husband.name)
        print("Husband's ID: ", self.husband.id)
        print("Wife's name: ", self.wife.name)
        print("Wife's ID: ", self.wife.id)
        print("Date of divorce: ", self.divorce_date)
    def add_divorce(self):
        husband=Citizen()
        wife=Citizen()
        husband.name = input("Name of the first Citizen: ")
        while husband.name not in self.Citizen:
            print ("The first Citizen does not exist.")
            husband.name = input("Name of the first Citizen: ")
        husband.id = input("ID of the first Citizen: ")
        while husband.id not in self.Citizen:
            print ("The first Citizen does not exist.")
            husband.id = input("ID of the first Citizen: ")
        if husband.marriage == "single":
            print ("The first Citizen is not married.")
            return
        wife.name = input("Name of the second Citizen: ")
        while wife.name not in self.Citizen:
            print ("The second Citizen does not exist.")
            wife.name = input("Name of the second Citizen: ")
        wife.id = input("ID of the second Citizen: ")
        while wife.id not in self.Citizen:
            print ("The second Citizen does not exist.")
            wife.id = input("ID of the second Citizen: ")
        if wife.marriage == "single":
            print ("The second Citizen is not married.")
            return
        divorce_date = input("Date of divorce: ")
        self.divorce = {husband, wife, divorce_date}
        husband.marriage = "single"
        wife.marriage = "single"
        husband.spouse = "None"
        wife.spouse = "None"
        husband.marriage_certificate = {}
        wife.marriage_certificate = {}
        self.Citizen[Citizen.id] = Citizen
        print ("Divorce added.")

    def birth_declaration(self):
        print("Enter the following information:")
        Citizen.name = input("Name: ")
        Citizen.id = input("ID: ")
        Citizen.DoB = input("Date of birth: ")
        Citizen.Place_of_birth = input("Place of birth: ")
        self.father = input("Father's name: ")
        self.father_id = input("Father's ID: ")
        self.mother = input("Mother's name: ")
        self.mother_id = input("Mother's ID: ")
        self.birth_certificate = input("Birth certificate: ")
        self.birth = {Citizen.name, Citizen.id, Citizen.DoB, Citizen.Place_of_birth, self.father, self.father_id, self.mother, self.mother_id, self.birth_certificate}
        self.Citizen[Citizen.id] = Citizen
        print ("Birth added.")
    def death_declaration(self):
        print("Enter the following information:")
        Citizen.name = input("Name: ")
        Citizen.id = input("ID: ")
        Citizen.DoB = input("Date of birth: ")
        Citizen.place_of_origin = input("Place of origin: ")
        Citizen.place_of_residence = input("Place of residence: ")
        self.reasion_of_death = input("Reason of death: ")
        self.date_of_death = input("Date of death: ")
        self.place_of_death = input("Place of death: ")
        self.death_certificate = input("Death certificate: ")
        self.death = {Citizen.name, Citizen.id, Citizen.DoB, Citizen.place_of_origin, Citizen.place_of_residence, self.reasion_of_death, self.date_of_death, self.place_of_death, self.death_certificate}
        self.Citizen[Citizen.id] = Citizen
        print ("Death added.")

    def change_name(self):
        self.search_citizen()
        new_name = input("Enter the new name: ")
        print("The name is changed to ", new_name)
        self.Citizen[Citizen.id].name = new_name
    def print_citizen(self, citizen):
        print("Name: ", citizen.name)
        print("ID: ", citizen.id)
        print("Date of birth: ", citizen.DoB)
        print("Nationality: ", citizen.nationality)
        print("Place of origin: ", citizen.place_of_origin)
        print("Place of residence: ", citizen.place_of_residence)
        print("Marriage status: ", citizen.marriage)
        if citizen.marriage == "married":
            print("Spouse: ", citizen.spouse)

    def search_citizen(self):
        if not self.citizen:
            print("No citizen found.")
            return
        citizen_id=input("Enter the ID of the citizen: ")
        if citizen_id not in self.citizen:
            print("Citizen not found.")
            return
        self.print_citizen(self.citizen[citizen_id])

    def search_marriage(self):
        print("Enter the following information: ")
        husband_name = input("Name of the first Citizen: ")
        husband_id = input("ID of the first Citizen: ")
        wife_name = input("Name of the second Citizen: ")
        wife_id = input("ID of the second Citizen: ")
        while self.marriage == {self.husband, self.wife}:
            print("The marriage is found.")
        else:
            self.print_citizen(self.marriage)

    def search_birth(self, Citizen):
        print("Enter the following information: ")
        name = input("Name: ")
        id = input("ID: ")
        if self.birth == {Citizen.name, Citizen.id}:
            print("The birth is found.")
        else:
            print("The birth is not found.")

    def search_death(self, Citizen):
        print("Enter the following information:")
        name = input("Name: ")
        id = input("ID: ")
        if self.death == {Citizen.name, Citizen.id}:
            print("The death is found.")
        else:
            print("The death is not found.")

    def search_divorce(self):
        print("Enter the following information:")
        self.husband = input("Husband's name: ")
        self.husband_id = input("Husband's ID: ")
        self.wife = input("Wife's name: ")
        self.wife_id = input("Wife's ID: ")
        if self.divorce == {self.husband, self.wife}:
            print("The divorce is found.")
        else:
            print("The divorce is not found.")

    def delete_Citizen(self):
        print("Enter the following information:")
        Citizen.name = input("Name: ")
        Citizen.id = input("ID: ")
        if self.Citizen[Citizen.id] == Citizen:
            del self.Citizen[Citizen.id]
            print("The Citizen is deleted.")
        else:
            print("The Citizen is not found.")

    def delete_marriage(self):
        print("Enter the following information:")
        self.husband = input("Husband's name: ")
        self.husband_id = input("Husband's ID: ")
        self.wife = input("Wife's name: ")
        self.wife_id = input("Wife's ID: ")
        if self.marriage == {self.husband, self.wife}:
            del self.marriage
            print("The marriage is deleted.")
        else:
            print("The marriage is not found.")

    def delete_birth(self, Citizen):
        print("Enter the following information:")
        Citizen.name = input("Name: ")
        Citizen.id = input("ID: ")
        if self.birth == {Citizen.name, Citizen.id}:
            del self.birth
            print("The birth is deleted.")
        else:
            print("The birth is not found.")

    def delete_death(self):
        print("Enter the following information:")
        Citizen.name = input("Name: ")
        Citizen.id = input("ID: ")
        if self.death == {Citizen.name, Citizen.id}:
            del self.death
            print("The death is deleted.")
        else:
            print("The death is not found.")

    def delete_divorce(self):
        print("Enter the following information:")
        self.husband = input("Husband's name: ")
        self.husband_id = input("Husband's ID: ")
        self.wife = input("Wife's name: ")
        self.wife_id = input("Wife's ID: ")
        if self.divorce == {self.husband, self.wife}:
            del self.divorce
            print("The divorce is deleted.")
        else:
            print("The divorce is not found.")

    def update_Citizen(self):
        print("Enter the following information:")
        Citizen.name = input("Name: ")
        Citizen.id = input("ID: ")
        if self.Citizen[Citizen.id] == Citizen:
            Citizen.name = input("Name: ")
            Citizen.id = input("ID: ")
            Citizen.DoB = input("Date of birth: ")
            Citizen.place_of_origin = input("Place of origin: ")
            Citizen.place_of_residence = input("Place of residence: ")
            self.Citizen[Citizen.id] = Citizen
            print("The Citizen is updated.")
        else:
            print("The Citizen is not found.")

    def update_marriage(self):
        print("Enter the following information:")
        self.husband = input("Husband's name: ")
        self.husband_id = input("Husband's ID: ")
        self.wife = input("Wife's name: ")
        self.wife_id = input("Wife's ID: ")
        if self.marriage == {self.husband, self.wife}:
            self.husband = input("Husband's name: ")
            self.husband_id = input("Husband's ID: ")
            self.wife = input("Wife's name: ")
            self.wife_id = input("Wife's ID: ")
            self.marriage = {self.husband, self.wife}
            print("The marriage is updated.")
        else:
            print("The marriage is not found.")

    def update_birth(self):
        print("Enter the following information:")
        Citizen.name = input("Name: ")
        Citizen.id = input("ID: ")
        if self.birth == {Citizen.name, Citizen.id}:
            Citizen.name = input("Name: ")
            Citizen.id = input("ID: ")
            Citizen.DoB = input("Date of birth: ")
            Citizen.place_of_origin = input("Place of origin: ")
            Citizen.place_of_residence = input("Place of residence: ")
            self.birth = {Citizen.name, Citizen.id, Citizen.DoB, Citizen.place_of_origin, Citizen.place_of_residence}
            print("The birth is updated.")
        else:
            print("The birth is not found.")

    def update_death(self):
        print("Enter the following information:")
        Citizen.name = input("Name: ")
        Citizen.id = input("ID: ")
        if self.death == {Citizen.name, Citizen.id}:
            Citizen.name = input("Name: ")
            Citizen.id = input("ID: ")
            Citizen.DoB = input("Date of birth: ")
            Citizen.place_of_origin = input("Place of origin: ")
            Citizen.place_of_residence = input("Place of residence: ")
            self.death = {Citizen.name, Citizen.id, Citizen.DoB, Citizen.place_of_origin, Citizen.place_of_residence}
            print("The death is updated.")
        else:
            print("The death is not found.")

    def update_divorce(self):
        print("Enter the following information:")
        self.husband = input("Husband's name: ")
        self.husband_id = input("Husband's ID: ")
        self.wife = input("Wife's name: ")
        self.wife_id = input("Wife's ID: ")
        if self.divorce == {self.husband, self.wife}:
            self.husband = input("Husband's name: ")
            self.husband_id = input("Husband's ID: ")
            self.wife = input("Wife's name: ")
            self.wife_id = input("Wife's ID: ")
            self.divorce = {self.husband, self.wife}
            print("The divorce is updated.")
        else:
            print("The divorce is not found.")
    def list_Citizen(self):
        print(self.Citizen)

    #main
    def menu(self):
        while True:
            while True:
                print("1. Add a citizen")
                print("2. Add a marriage")
                print("3. Add a birth")
                print("4. Add a death")
                print("5. Add a divorce")
                print("6. Delete a Citizen")
                print("7. Delete a marriage")
                print("8. Delete a birth")
                print("9. Delete a death")
                print("10. Delete a divorce")
                print("11. Update a Citizen")
                print("12. Update a marriage")
                print("13. Update a birth")
                print("14. Update a death")
                print("15. Update a divorce")
                print("16. Exit")
                print("17. List of Citizens")
                choice = input("Enter your choice: ")
                if choice == "1":
                    self.add_citizen()
                elif choice == "2":
                    self.add_marriage()
                elif choice == "3":
                    self.add_birth()
                elif choice == "4":
                    self.add_death()
                elif choice == "5":
                    self.add_divorce()
                elif choice == "6":
                    self.delete_Citizen()
                elif choice == "7":
                    self.delete_marriage()
                elif choice == "8":
                    self.delete_birth()
                elif choice == "9":
                    self.delete_death()
                elif choice == "10":
                    self.delete_divorce()
                elif choice == "11":
                    self.update_Citizen()
                elif choice == "12":
                    self.update_marriage()
                elif choice == "13":
                    self.update_birth()
                elif choice == "14":
                    self.update_death()
                elif choice == "15":
                    self.update_divorce()
                elif choice == "16":
                    print("Thank you for using this program")
                    return
                elif choice == "17":
                    self.list_Citizen()
                else:
                    print("Invalid choice")