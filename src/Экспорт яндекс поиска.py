# -*- coding: utf-8 -*-
from grab import Grab

g = Grab()
words = 'grab, python'
lst = []

#go to url (moscow region: rstr=-213) (page: p=0) with keywords: text=
url = 'http://yandex.ru/yandsearch?p={0}&text={1}'
#добавляем ключевые слова к ссылке
param = words.replace(" ", "").split(',')
param2 = '%2C+'.join(str(elem) for elem in param)

#открываем файл в который будем записывать полученные ссылки
with open('somefile.txt', 'wt') as f:
    #записываем результаты поиска с первых 3 страниц
    for page in range(3):
        #итоговая ссылка
        fullurl = url.format(page, param2)
        g.go(fullurl)
        #находим class ссылки firebug'ом и начинаем их искать
        for i in g.doc.select('//a[@class="b-link serp-item__title-link"]'):
            if g.doc.select('//a[@class="b-link serp-item__title-link"]').exists():
                # последний пункт задания, составляем список
                lst.append({'page': page+1, 'title': i.text(), 'url': i.attr('href')})
                # сохраняем ссылки в файл
                f.write(i.attr('href'))
                f.write('\n')
print(lst)