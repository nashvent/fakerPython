# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from faker import Faker
fake = Faker('es_MX')

f = open("datos.csv",'w')

print>>f,"nombre,direccion,compañia,celular"
for _ in range(100):
    print>>f,(fake.name()),",",fake.address(),",",fake.company(),",",fake.phone_number()
fake.simple_profile()
