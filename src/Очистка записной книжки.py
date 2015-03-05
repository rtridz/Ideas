import contacts
a=contacts.get_all_people()
for i in a:
    contacts.remove_person(i)
contacts.save()