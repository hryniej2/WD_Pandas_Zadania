import numpy as np
import pandas as pd
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
zadanie = pd.read_excel(xlsx, header = 0)
# print(zadanie)
zadanie.to_excel('zadanie1.xlsx', sheet_name="arkusz_pierwszy")

## zadanie 2

#1
# a = zadanie [zadanie ['Liczba'] < 1000]
# print(a)

#2
# b = zadanie[zadanie['Imie']=='JAKUB']
# print(b)

#3
# c = zadanie['Liczba'].sum()
# print(c)

#4
# d = zadanie[(zadanie['Rok'] > 2006) & (zadanie['Rok'] < 2011)]['Liczba'].sum()
# print(d)

#5
# e = zadanie[(zadanie['Rok'] == 2000) & (zadanie['Plec'] == 'M')]['Liczba'].sum()
# print(e)

#6

# f = zadanie.groupby(['Rok','Plec']).max()
# print(f)



## zad 3

zadanie1 = pd.read_csv('zamowienia.csv', header=0, sep=";", decimal=',')
# print(zadanie1)
zadanie1.to_csv('plik.csv', index=False)

#1
# a = zadanie1['Sprzedawca']
# b = a.drop_duplicates()
# print(b)

#2

# b = zadanie1.sort_values(by='Utarg', ascending=False)['Utarg'][0:5]
# print(b)

#3

# c = zadanie1.groupby(['Sprzedawca']).size().reset_index(name='ilosc')
# print(c)

#4

# d = zadanie1.groupby(['Kraj']).size().reset_index(name='Suma')
# print(d)
