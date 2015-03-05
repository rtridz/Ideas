import datetime,contacts,notification
people=contacts.get_all_people()
delta=datetime.timedelta(days=7)
for i in people:
    if i.birthday - datetime.datetime.now() == delta:
        notification.schedule('До дня рождения контакта ' + i.full_name +  ' осталась неделя!')