import pickle


class Contact:
    def __init__(self, name, phone_number,address=None, email=None):
        self.name = name
        self.phone_number = phone_number


    def __str__(self):
        return f"{self.name} --> {self.phone_number}"


#phone_book = "conts"
def show_all_contacts(phonebook):
    a = read_Phonebook(phonebook)
    list_tuple = []
    if len(a) == 0:
        print("there is no contacts in contact book")
    else:
        #print(a)
        for i in a:
            list_tuple.append((i.name, i.phone_number))
        print(list_tuple)

def add_contact(phonebook):
    data = input_contact()
    phonebook_data = read_Phonebook(phonebook)
    phonebook_data.append(data)
    print("Entry made")
    save(phonebook_data, phonebook)

    #if phonebook_data.get(data.phone_number):
        #raise ValueError("contact alrady exists")
    #if data.phone_number in phonebook_data:
        #raise ValueError("contacts exists")
    #else:
    #phonebook_data.append(data)
    #print("Entry added")
    #save(data, phonebook)

def delete_contact(phonebook):
    a = read_Phonebook(phonebook)
    if len(a) == 0:
        print("the contact list is empty")
    else:
        list_of_names = [contact.name for contact in a]
        name_to_be_deleted = input("Enter name to be deleted: ")
        if name_to_be_deleted in list_of_names:
            for i in a:
                if i.name == name_to_be_deleted:
                    a.remove(i)
                    print("contact removed")
                    save(a, phonebook)

        else:
            print("name does not exist")

def search(phonebook):
    a = read_Phonebook(phonebook)
    if len(a) == 0:
        print("contact book is empty")
        return "contact list is empty"
    else:
        all_names = all_names_in_phonebook()
        search_name = input("Enter name to search: ")
        if search_name not in all_names:
            print("name does not exist in phonebook")
            return "name does not exist in phonebook"
        else:
            for i in a:
                if i.name == search_name:
                    print(f"contact name {i.name}, contact number is {i.phone_number}")

def make_change_to_name(phonebook):
    a = read_Phonebook(phonebook)
    name_to_change = input("enter the name to be changed: ")
    if does_contact_exist(name_to_change, phonebook):
        for i in a:
            if name_to_change == i.name:
                i.name = input("enter the new name:  ")
                break
        save(a,phonebook)
    else:
        print("Name does not exist")

def change_number(phonebook):
    a = read_Phonebook(phonebook)
    name_to_change = input("enter the name to be changed: ")
    if does_contact_exist(name_to_change, phonebook):
        for i in a:
            if name_to_change == i.name:
                i.phone_number = input("enter the new number:  ")
                break
        save(a, phonebook)
    else:
        print("contact does not exist does not exist")







def read_Phonebook(phonebook):
    try:
        with open(phonebook, 'rb') as f:
            try:
                c = pickle.load(f)
                return c
            except EOFError:
                return []
    except IOError:
        print("the phonebook does not exist")

def save(data, phonebook):
    with open(phonebook, "wb") as f:
        pickle.dump(data, f)

def input_contact():
    c_name = input("Enter your name: ")
    c_phone_number = input("Enter your phone_number: ")

    contact = Contact(name=c_name, phone_number=c_phone_number)
    return contact

phonebook = "cons"
#a = delete_contact(phonebook)
#f = [con.name for con in b]
#print(f)
"""" print all the names in contacts"""
def all_names_in_phonebook():
    phonebook = "cons"
    c = read_Phonebook(phonebook)
    k = [p.name for p in c]
    #print(k)
    return k

def does_contact_exist(name, phonebook):
    return name in all_names_in_phonebook()

print("options are: 'a' to add contacts, 'd' to delete contact, 's' to stop the program,/"
      " 'p' to search for contacts, 'c' to change name, ch to change number and show to show all contacts")
while True:
    option = input("enter the choice you want: ")
    if option == 's':
        break
    elif option == "show":
        show_all_contacts(phonebook)
    elif option == 'a':
        add_contact(phonebook)
    elif option == 'd':
        delete_contact(phonebook)
    elif option == 'p':
        search(phonebook)
    elif option == 'c':
        make_change_to_name(phonebook)
    elif option == "ch":
        change_number(phonebook)
    else:
        print("youv entered the wrong choice")



#add_contact(phonebook)
#search(phonebook)
#a = delete_contact(phonebook)
#make_change_to_name(phonebook)
#print(all_names_in_phonebook())
