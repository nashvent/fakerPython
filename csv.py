# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from faker import Faker
fake = Faker('es_MX')

import csv
import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

#download_dir = "exampleCsv.csv"

#csv = open(download_dir, "w") 

#columnTitleRow = "nombre,empresa,direccion,telefono\n"
#csv.write(columnTitleRow)


#for _ in range(10):
 #   name = fake.name()
  #  company = fake.company()
   # address=fake.address()
    #phone=fake.phone_number()
    #row = name + "," + company+","+address+","+phone+ "\n"
    #csv.write(row)

worksheet.write('A1', 'nombre')
worksheet.write('B1', 'empresa')
worksheet.write('C1', 'direccion')
worksheet.write('D1', 'telefono')
for x in range(2,4000):
    worksheet.write('A'+str(x),fake.name())
    worksheet.write('B'+str(x),fake.company())
    worksheet.write('C'+str(x),fake.address())
    worksheet.write('D'+str(x),fake.phone_number())
    

workbook.close()

    
