import pickle
import os


class Contacts:
    def __init__(self, name, number):
        self.name = name
        self.number = number

def read(phonebook):
    with open(phonebook, 'rb') as f:
        try:
            pickle.load(f)
        except EOFError:
            return []

def save(data, phonebook):
    with open(phonebook, "wb") as f:
        pickle.dump(data, f)

def add(data: Contacts):
    with open("hhh", 'rb') as f:
        is_file_empty = os.path.getsize("hhh") == 0
        if not is_file_empty:
            list_contacts = pickle.load(f)
        else:
            list_contacts = []

        try:
            with open("hhh", 'wb') as f:
                list_contacts.append(data)
                pickle.dump(list_contacts, f)
                print("contct added")
        except EOFError:
            return "contact not added"


        # a = read(phonebook)
        # a.append(data)
        # save(a, phonebook)

#conta = Contacts(name="dan", number="0707727199")
#a = add(conta)
with open("hhh", 'rb') as fl:
    c = pickle.load(fl)
    print(c)
    for i in c:
        print(i.name)

