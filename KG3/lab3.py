import numpy as np
import matplotlib.pyplot as plt
import serial
from drawnow import drawnow
import datetime, time
import Image, ImageDraw # модули из PIL
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

MainWindow = tk.Tk()
MainWindow.attributes("-fullscreen", True)
MainWindow["bg"] = "#FF7F50"

def lum(c): #цвет пиксела RGB -> значение яркости
	#формула, которая обычно используется для определения яркости
	return int(0.3*c[0] + 0.59*c[1] + 0.11*c[2])
def r(c): #цвет пиксела RGB -> значение R
	return c[0]
def g(c): #цвет пиксела RGB -> значение G
	return c[1]
def b(c): #цвет пиксела RGB -> значение B
	return c[2]
def drawhist(hname, H, harr):
	""" Рисуем диаграмму, сохраняем в файл в текущую папку
	hname - имя файла
	H - высота рисунка
	harr - массив с высотами столбиков в гистограмме
	"""
	W = len(harr) #кол-во элементов массива
	hist = Image.new("RGB", (W, H), "white") #создаем рисунок в памяти
	draw = ImageDraw.Draw(hist) #объект для рисования на рисунке
	maxx = float(max(harr)) #высота самого высокого столбика
	if maxx == 0: #столбики равны 0
		draw.rectangle(((0, 0), (W, H)), fill="black")
	else:
		for i in range(W):
			draw.line(((i, H),(i, H-harr[i]/maxx*H)), fill="black") #рисуем столбики
	del draw #удаляем объект
	hist.save(hname) #сохраняем рисунок в файл
# список с функциями и префиксами названий файлов
fnlist = [(lum, "luminosity_"), (r, "r_channel_"), (g, "g_channel_"), (b, "b_channel_")]
fname = raw_input("input file name: ") #Ввод имени файла, гистограмму кот. нужно построить
im = Image.open(fname) #открываем файл
# получаем список вида [(n1, c1), (n2, c2), ...], где
# c - цвет пиксела в RGB
# n - количество пикселов, имеющих данный цвет
clrs = im.getcolors(im.size[0]*im.size[1])
# ширина, высота гистограммы.
# Ширину менять не стоит, т.к. все ф-и отображаются в [0..255]
W, H = 256, 100
for fn, hname in fnlist: #перебираем все функции
	harr = [0 for i in range(W)] #создаем массив [0, 0, 0, ...] длины W
	for n, c in clrs: #перебираем список созданный выше
		index = fn(c) #fn - отображение цвета в яркость или выделение цветового канала
		#индексы элементов массива показывают значения яркости и прочего. Диапазон [0..255]
		#значения элементов массива = количество пикселов с опред. значением яркости и т.д.
		harr[index] += n
	drawhist(hname + "hist.png", H, harr) #рисуем гистограмму
# Нарисовали гистограммы по яркости и каналам, теперь
# Рисуем гистограмму RGB
rharr = [0 for i in range(W)]
gharr = list(rharr)
bharr = list(rharr)
for n, c in clrs:
	rharr[r(c)] += n
	gharr[g(c)] += n
	bharr[b(c)] += n
harr = [(rharr[i] + gharr[i] + bharr[i])/3 for i in range(W)]
drawhist("RGB_hist.png", H, harr)
k = 6.0 #коэффициент фильтрации + 1
filter_K = 1 + k

#вывод выборки в графическое окно
def cur_graf():
    plt.title("BMP280")
    plt.ylim( 100450, 100510 )
    plt.plot(nw, lw1,  "r.-", label='измеренное')
    plt.plot(nw, lw1f, "b.-", label='фильтрованное')
    plt.legend(loc='best')
    plt.ylabel(r'$давление, Па$')
    plt.xlabel(r'$номер \ измерения$')
    plt.grid(True)
#вывод всех списков в графическое окно
def all_graf():
    plt.close()
    fig=plt.figure()
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
    ax.set_title("датчик BMP280\n" +
                  str(count_v) + "-й эксперимент " +
                  "(" + now.strftime("%d-%m-%Y %H:%M") + ")")
    ax.set_ylabel(r'$давление, Па$')
    ax.set_xlabel(r'$номер \ измерения$' +
                   '; (период опроса датчика: {:.6f}, c)'.format(Ts))
    ax.text(0.95, 0.03,
        "Коэффициент фильтра: " + str(filter_K) + "\n",
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=14)
    plt.plot( n, l1,  "r-", label='измеренное')
    plt.plot( n, l1f, "b-", label='фильтрованное')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()
#определяем количество измерений
# общее количество измерений
str_m   = input("введите количество измерений: ")
m = eval(str_m)
# количество элементов выборки
mw  = 16
#настроить параметры последовательного порта
ser = serial.Serial()
ser.baudrate = 9600
port_num = input("введите номер последовательного порта: ")
ser.port = 'COM' + port_num
ser
#открыть последовательный порт
try:
    ser.open()
    ser.is_open
    print("соединились с: " + ser.portstr)
except serial.SerialException:
    print("нет соединения с портом: " + ser.portstr)
    raise SystemExit(1)
#определяем списки
l1  = [] # для значений давления
l1f = [] # для фильтрованных значений давления
t1  = [] # для значений моментов времени
lw1 = [] # для значений выборки давления
lw1f= [] # для фильтрованных значений выборки давления
n   = [] # для значений моментов выборки
nw  = [] # для значений выборки моментов времени
#подготовить файлы на диске для записи
filename = 'count.txt'
in_file = open(filename,"r")
count = in_file.read()
count_v = eval(count) + 1
in_file.close()
in_file = open(filename,"w")
count = str(count_v)
in_file.write(count)
in_file.close()
filename = count + '_' + filename
out_file = open(filename,"w")
#вывод информации для оператора на консоль
print("\nпараметры:\n")
print("n - номер измерения;")
print("P - давление, Па;")
print("\nизмеряемые значения величины давления\n")
print('{0}{1}\n'.format('n'.rjust(4),'P'.rjust(10)))
#считывание данных из последовательного порта
#накопление списков
#формирование текущей выборки
#вывод значений текущей выборки в графическое окно
i = 0
while i < m:
    n.append(i)
    nw.append(n[i])
    if i >= mw:
        nw.pop(0)
    line1 = ser.readline().decode('utf-8')[:-2]
    t1.append(time.time())
    if line1:
        l1.append(eval(line1))
        lw1.append(l1[i])
        if i :
            l1f.append( (l1f[i-1]*(filter_K - 1) + l1[i])/filter_K ) #(6)
            lw1f.append(l1f[i])
        else :
            l1f.append(l1[i])
            lw1f.append(l1f[i])
        if i >= mw:
            lw1.pop(0)
            lw1f.pop(0)
    print('{0:4d} {1:10.2f} {2:10.2f}'.format(n[i],l1[i],l1f[i]) )
    drawnow(cur_graf)
    i += 1
#закрыть последовательный порт
ser.close()
ser.is_open
time_tm = t1[m - 1] - t1[0]
print("\nпродолжительность времени измерений: {0:.3f}, c".format(time_tm))
Ts = time_tm / (m - 1)
print("\nпериод опроса датчика: {0:.6f}, c".format(Ts))
#запись таблицы в файл
print("\nтаблица находится в файле {}\n".format(filename))
for i in np.arange(0,len(n),1):
    count = str(n[i]) + "\t" + str(l1[i]) + "\n"
    out_file.write(count)
#закрыть файл с таблицей
out_file.close()
out_file.closed
#получить дату и время
now = datetime.datetime.now()
#вывести график в графическое окно
all_graf()
end = input("\nнажмите Ctrl-C, чтобы выйти ")