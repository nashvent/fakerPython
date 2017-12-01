# -*- coding: utf-8 -*-
import sys
import random 
reload(sys)
sys.setdefaultencoding('utf-8')
from faker import Faker
fake = Faker('es_MX')

import csv
import xlsxwriter

workbook = xlsxwriter.Workbook('datos.xlsx')
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
tarjetas=['Visa','Mastercard','American Express','Diners Club']
ciudad=['AMAZONAS','ÁNCASH','APURÍMAC','AREQUIPA','AYACUCHO','CAJAMARCA','CUSCO','HUANCAVELICA','HUÁNUCO','ICA','JUNÍN','LA LIBERTAD','LAMBAYEQUE','LIMA','LORETO','MADRE DE DIOS','MOQUEGUA','PASCO','PIURA','PUNO','SAN MARTÍN','TACNA','TUMBES','UCAYALI']

meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
worksheet.write('A1', 'Cliente')
worksheet.write('B1', 'Departamento')
worksheet.write('C1', 'Provincia')
worksheet.write('D1', 'Distrito')
worksheet.write('E1', 'Vendedor')
worksheet.write('F1', 'Agencia')
worksheet.write('G1', 'Tipo de Tarjeta')
worksheet.write('H1', 'Numero de tarjeta')
worksheet.write('I1', 'Monto')
worksheet.write('J1', 'Credito')
worksheet.write('K1', 'Pagos')
worksheet.write('L1', 'Año')
worksheet.write('M1', 'Mes')
worksheet.write('N1', 'Año del mes')
for x in range(2,4000):
    numTarjeta=str(random.randint(1000,9999))+str(random.randint(1000,9999))+str(random.randint(1000,9999))+str(random.randint(1000,9999))
    ciudadActual=ciudad[random.randint(0,len(ciudad)-1)]
    worksheet.write('A'+str(x),fake.name()) #Cliente
    worksheet.write('B'+str(x),ciudadActual) #Departamento
    worksheet.write('C'+str(x),ciudadActual) #Provincia
    worksheet.write('D'+str(x),ciudadActual) #Distrito
    worksheet.write('E'+str(x),fake.name()) #Vendedor
    worksheet.write('F'+str(x),fake.street_name()) #Agencia
    worksheet.write('G'+str(x),tarjetas[random.randint(0,len(tarjetas)-1)]) #Tipo de tarjeta
    worksheet.write('H'+str(x),numTarjeta) #Nro de tarjera
    worksheet.write('I'+str(x),random.randint(1000,100000)) #Monto
    worksheet.write('J'+str(x),random.randint(1000,100000)) #Credito
    worksheet.write('K'+str(x),random.randint(10,100)) #Pagos
    worksheet.write('L'+str(x),random.randint(2000, 2017)) #Año
    worksheet.write('M'+str(x),meses[random.randint(0,len(meses)-1)]) #Mes
    worksheet.write('N'+str(x),fake.day_of_month()) #Año del mes

workbook.close()

