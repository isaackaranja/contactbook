import pickle
import os

class Contacts:
    def __init__(self, name, phone_number, e_mail, location=None):
        self.name = name
        self.phone_number = phone_number
        self.email = e_mail
        self.location = location

    def __str__(self):
        return f"{self.name} {self.phone_number}"



def add_contacts():
    person = input_contact()
    with open("list_of_contacts", 'rb') as f:
        size = os.path.getsize("list_of_contacts") == 0
        if size:
            with open("list_of_contacts", 'ab') as f:
                contact_list = []
                #person = input_contact()
                contact_list.append(person)
                pickle.dump(contact_list, f)
                return "contact added"

        else:
            with open("list_of_contacts", 'rb') as f:
                contact_list = []
                items = pickle.load(f)
                for item in items:
                    if item.phone_number == person.phone_number:
                        return "number already exists"
                    else:
                        with open("list_of_contacts", 'ab') as f:
                            contact_list.append(person)
                            pickle.dump(contact_list, f)
                            return "contact added"

def delete_contact(contact: Contacts):
    pass








        # with open("list_of_contacts", 'wb') as f:
        #     contact_list = []
        #     person = self.input_contact()
        #     contact_list.append(person)
        #     pickle.dump(contact_list, f)
        # with open("list_of_contacts", 'rb') as f:
        #     print(f.read())




def input_contact():
    c_name = input("Enter your name: ")
    c_phone_number = input("Enter your phone_number: ")
    c_email = input("Enter your email address: ")
    c_location = input("Enter you region: ")

    contact = Contacts(name=c_name, phone_number=c_phone_number, e_mail=c_email, location=c_location)
    return contact


#a = add_contacts()
#print(a)
with open("list_of_contacts", 'rb') as f:
    j = pickle.load(f)
    print(j)




