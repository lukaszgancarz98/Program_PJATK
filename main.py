from __future__ import print_function
import csv
import numpy as np
import pandas as pd
import c3d
import sys
import matplotlib.pyplot as plt


def odczyt(plik):
    reader = c3d.Reader(open(plik + '.c3d', 'rb'))
    # print(reader)
    # for i, points, analog in reader.read_frames():
    #     print('frame {}: point {}, analog {}'.format(
    #         i, points.shape, analog.shape))
    return "success"


def convert(plik):
    global fields
    inputf = sys.stdin
    output = sys.stdout
    if plik != '-':
        inputf = open(plik+'.c3d', 'rb')
        output = open(plik.replace('.c3d', '.csv'), 'w')
        # plt.figure(figsize=(15,3))
        # plt.plot(0, 0)
        # plt.show()
    for frame_no, points, analog in c3d.Reader(inputf).read_frames(copy=False):
        fields = [frame_no]
        lista = []
        # print(points[0])
        df = pd.DataFrame(lista)
        # markernumber = input()
        for x, y, z, err, cam in points:
            fields.append(str(x))
            fields.append(str(y))
            fields.append(str(z))
            # df.loc[, :] = fields
    # print(fields)
    # print(type(fields))
    # plikz = pd.DataFrame(fields)
    # print(plikz)
    # print(type(plikz))
    # plt.figure(figsize=(15, 3))
    # plt.plot(lista[0])
    # plt.show()
    # print(row[2] for row in plikz)
    # zapis(plikz)

def zapis(plikz):
    with open('keszkewmeszke.csv', 'w', encoding='utf-8') as csvfile:
        # fieldnames = ['klatka', 'x', 'y', 'z']
        writer = csv.writer(csvfile)
        # writer.writeheader()
        for row in plikz:
            writer.writerow(row)


print("Wprowadź nazwę pliku")
plik = input()
convert(plik)
