from __future__ import print_function
import csv
import numpy as np
import pandas as pd
import c3d
import sys
import matplotlib.pyplot as plt

reader = c3d.Reader(open('ok1.c3d', 'rb'))
list_of_markers = reader.point_labels


def read_frames(marker_no, frame_stop):
  print('Wybrano marker: ', list_of_markers[int(marker_no)])
  for frame_no, points, analog in reader.read_frames():
    if int(frame_stop) > frame_no + 1:
        type(points[int(marker_no)][:3])
    # print(points[marker_no][:3])
    # x_LFHD = list_of_frames(0, 0)


def list_of_frames(marker_no, frame_stop):
  list_of = []
  global axis
  global list_of_markers
  print('Wybrano marker: ', list_of_markers[int(marker_no)])
  count = 0
  for frame_no, points, analog in reader.read_frames():
    if count < int(frame_stop):
        list_of.append(points[int(marker_no)][int(axis)])
        count += 1
  integrate(frame_stop, list_of)
  return list_of

def daneodczyt(plik):
    inputf = open(plik + '.c3d', 'rb')
    data = []
    for frame_no, points, analog in c3d.Reader(inputf).read_frames(copy=False):
        fields = [frame_no]
        for x, y, z, err, cam in points:
            fields.append(str(x))
            fields.append(str(y))
            fields.append(str(z))
            data = fields
    zapis_dane(plik, data)


def integrate(frame_stop, list_of):
    dx = (int(frame_stop) - 0) / int(frame_stop)
    integr = 0
    i = int(frame_stop) - 1
    for x in range(i):
        x = x * dx + 0
        fx1 = list_of[int(x)]
        x += dx
        fx2 = list_of[int(x)]
        integr += 0.5 * dx * (fx1 + fx2)
    zapiswynik(marker_no, integr)
    return integr


def zapis_dane(plik, fields):
    column = []
    for z in list_of_markers:
        column.append(z + ' os X')
        column.append(z + ' os Y')
        column.append(z + ' os Z')
    print(type(column))
    column.insert(0, 'frame')
    df_data = pd.DataFrame(fields)
    df_data_trans = df_data.T
    df_data_trans.columns = column
    df_data_trans.to_csv('dane_' + plik + '.csv', sep=';')


def zapiswynik(marker_no, integr):
    print(axis)
    if int(axis) == 0:
        with open('wynik_całkowania_os_x_'+ list_of_markers[int(marker_no)] + '.csv', 'w', encoding='utf-8') as csv_file:
            new_list = [str(list_of_markers[int(marker_no)])]
            wynik = [str(integr)]
            writer = csv.writer(csv_file)
            writer.writerow(new_list)
            writer.writerow(wynik)
    if int(axis) == 1:
        with open('wynik_całkowania_os_y_'+ list_of_markers[int(marker_no)] + '.csv', 'w', encoding='utf-8') as csv_file:
            new_list = [str(list_of_markers[int(marker_no)])]
            wynik = [str(integr)]
            writer = csv.writer(csv_file)
            writer.writerow(new_list)
            writer.writerow(wynik)
    if int(axis) == 2:
        with open('wynik_całkowania_os_z_'+ list_of_markers[int(marker_no)] + '.csv', 'w', encoding='utf-8') as csv_file:
            new_list = [str(list_of_markers[int(marker_no)])]
            wynik = [str(integr)]
            writer = csv.writer(csv_file)
            writer.writerow(new_list)
            writer.writerow(wynik)



print("Wprowadź nazwę pliku")
plik = input()
print("Wprowadź numer markeru")
marker_no = input()
print("Wprowadź ilość klatek")
frame_stop = input()
read_frames(marker_no, frame_stop)
print("Wybierz oś:"
      "0 - x"
      "1 - y"
      "2 - z")
axis = input()
list_of_frames(marker_no, frame_stop)
daneodczyt(plik)
