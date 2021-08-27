from __future__ import print_function
import csv
import pandas as pd
import c3d
import matplotlib.pyplot as plt

reader = c3d.Reader(open('ok1.c3d', 'rb'))
list_of_markers = reader.point_labels

def read_frames(marker_no):
  print('Wybrano marker: ', list_of_markers[int(marker_no)])
  # for frame_no, points, analog in reader.read_frames():
  #   if int(frame_stop) > frame_no + 1:
  #       type(points[int(marker_no)][:3])
    # print(points[marker_no][:3])
    # x_LFHD = list_of_frames(0, 0)


def list_of_frames(marker_no, frames_start, frame_stop):
  list_of = []
  global axis
  global list_of_markers
  # print('Wybrano marker: ', list_of_markers[int(marker_no)])
  count = 0
  for frame_no, points, analog in reader.read_frames():
    if count <= int(frame_stop):
        list_of.append(points[int(marker_no)][int(axis)])
        count += 1
  integrate(frames_start, frame_stop, list_of)
  return list_of

def daneodczyt(plik):
    inputf = open(plik + '.c3d', 'rb')
    data = []
    global frames
    for frame_no, points, analog in c3d.Reader(inputf).read_frames(copy=False):
        fields = [frame_no]
        frames = frame_no
        for x, y, z, err, cam in points:
            fields.append(str(x))
            fields.append(str(y))
            fields.append(str(z))
        data.append(fields)
    zapis_dane(plik, data)
    print("Zapisano")


def integrate(frames_start, frame_stop, list_of):
    dx = 1
    integr = 0
    # i = int(frame_stop) - 1
    print(list_of[int(frames_start)], "start")
    print(list_of[int(frame_stop)], "stop")
    for x in range(int(frames_start), int(frame_stop)):
        x = x * dx + 0
        fx1 = list_of[int(x)]
        x += dx
        fx2 = list_of[int(x)]
        integr += 0.5 * dx * (fx1 + fx2)
    print("Wynik całkowania dla markera " + marker_no + " : " + str(integr))
    zapiswynik(marker_no, integr, frames_start, frame_stop)
    return integr


def zapis_dane(plik, fields):
    column = []
    for z in list_of_markers:
        column.append(z + ' os X')
        column.append(z + ' os Y')
        column.append(z + ' os Z')
    column.insert(0, 'frame')
    df = pd.DataFrame(fields, columns=column)
    df.to_csv('dane_' + plik + '.csv', sep=';')


def zapiswynik(marker_no, integr, frames_start, frame_stop):
    print(axis)
    if int(axis) == 0:
        with open('wynik_całkowania_os_x_'+ list_of_markers[int(marker_no)] + '.csv', 'w', encoding='utf-8') as csv_file:
            new_list = [str(list_of_markers[int(marker_no)])]
            wynik = [str(integr)]
            start = ["Od klatki: ", str(frames_start)]
            stop = ["Do klatki: ", str(frame_stop)]
            writer = csv.writer(csv_file)
            writer.writerow(new_list)
            writer.writerow(start)
            writer.writerow(stop)
            writer.writerow(wynik)
    if int(axis) == 1:
        with open('wynik_całkowania_os_y_'+ list_of_markers[int(marker_no)] + '.csv', 'w', encoding='utf-8') as csv_file:
            new_list = [str(list_of_markers[int(marker_no)])]
            wynik = [str(integr)]
            start = ["Od klatki: ", str(frames_start)]
            stop = ["Do klatki: ", str(frame_stop)]
            writer = csv.writer(csv_file)
            writer.writerow(new_list)
            writer.writerow(start)
            writer.writerow(stop)
            writer.writerow(wynik)
    if int(axis) == 2:
        with open('wynik_całkowania_os_z_'+ list_of_markers[int(marker_no)] + '.csv', 'w', encoding='utf-8') as csv_file:
            new_list = [str(list_of_markers[int(marker_no)])]
            start = ["Od klatki: ", str(frames_start)]
            stop = ["Do klatki: ", str(frame_stop)]
            wynik = ["Wynik: ", str(integr)]
            writer = csv.writer(csv_file)
            writer.writerow(start)
            writer.writerow(stop)
            writer.writerow(new_list)
            writer.writerow(wynik)
while True:
    print("Wprowadź nazwę pliku")
    plik = input()
    print("Wybierz działanie: ")
    print("1 -- Dane z pliku")
    print("2 -- Całkowanie")
    print("3 -- Wyjście z aplikacji")
    wybor = input()
    if int(wybor) == 2:
        print("Wprowadź numer markeru")
        marker_no = input()
        read_frames(marker_no)
        print("Wprowadz początek przedziału")
        frames_start = input()
        print("Wprowadź koniec przedziału")
        frame_stop = input()
        print("Wybierz oś:")
        print("0 - x")
        print("1 - y")
        print("2 - z")
        axis = input()
        list_of_frames(marker_no, frames_start, frame_stop)
    elif int(wybor) == 1:
        daneodczyt(plik)
    elif int(wybor) == 3:
        exit()
