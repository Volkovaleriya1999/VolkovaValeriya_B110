""" ПАТТЕРН СТРОИТЕЛЬ """

import copy
from collections import OrderedDict


class Phone:
    def __init__(self, title, os, ram, memory, **rest):
        self.title = title
        self.os = os
        self.ram = ram
        self.memory = memory
        self.__dict__.update(rest)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(self.__dict__.items())
        for i in ordered.keys():
            mylist.append(f'{i}: {ordered[i]}')
            mylist.append('\n')
        return ''.join(mylist)


class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Некорректный индификатор')
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj

phone = Phone('телефон на базе iOS', 'iOS', '32 ГБ', '128ГБ', headphones='в комплекте',
              charge='Магнитная зарядка')
cid = 'iOS'
prototype = Prototype()
prototype.register(cid, phone)

phone2 = prototype.clone(cid, title='телефон на базе Android', os='Android', ram='16ГБ', memory='64ГБ',
                         charge='USB')

for i in (phone, phone2):
    print(i)