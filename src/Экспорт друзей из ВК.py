import vk,datetime,contacts
vkapi=vk.API('Application_id','Login','Password')

def convertdate(date):
    date=date.split('.')
    if len(date)==2:
        return datetime.datetime.combine(datetime.date(1604,int(date[1]),int(date[0])),datetime.time(0, 0))
    else:
        return datetime.datetime.combine(datetime.date(int(date[2]),int(date[1]),int(date[0])),datetime.time(0, 0))

a=vkapi.friends.get(fields='contacts,bdate')
a=a['items']
for i in a:
    Temp=contacts.Person()
    Temp.last_name= i['last_name']
    Temp.first_name = i['first_name']
    if 'mobile_phone' in i.keys():
        try:
            Temp.phone=[('mobile',i['mobile_phone'])]
        except:
            pass
    if 'home_phone' in i.keys():
        try:
            Temp.phone.append(('home',i['home_phone']))
        except:
            pass
    Temp.url = [('vk','http://vk.com/id'+str(i['id']))]
    if 'bdate' in i.keys():
        Temp.birthday =convertdate(i['bdate'])
    contacts.add_person(Temp)
    contacts.save()