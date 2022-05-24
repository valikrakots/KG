# Вариант 11
# LAB <--> XYZ <--> HSV
from tkinter import *
from tkinter import messagebox, colorchooser
import colorsys

import numpy
from skimage import color
from colormath.color_objects import LabColor, XYZColor, HSVColor
from colormath.color_conversions import convert_color

MainWindow = Tk()
MainWindow.title("Ракоть Валентин, 3 курс, 12 группа, Вариант 11")
MainWindow.attributes("-fullscreen", True)
MainWindow["bg"] = "#FFDEAD"
state = 1
previous = 1

varL = DoubleVar()
varL.set(0.0)
varA = DoubleVar()
varA.set(0.0)
varB = DoubleVar()
varB.set(0.0)

varX = DoubleVar()
varX.set(0.0)
varY = DoubleVar()
varY.set(0.0)
varZ = DoubleVar()
varZ.set(0.0)

varH = DoubleVar()
varH.set(0.0)
varS = DoubleVar()
varS.set(0.0)
varV = DoubleVar()
varV.set(0.0)


# canvas = Canvas(width=300,
#                 height=300,
#                 bg="black",
#                 highlightbackground="#DAA520")
# canvas.place(relx=0.03, rely=0.2)

labLAB_L = Label(text="L",
                font=("Times New Roman", "36"),
                bg="#FFDEAD")
labLAB_L.place(relx=0.57, rely=0.1)
textL = Entry(MainWindow,
               width=7,
               bd=5,
               font=("Times New Roman", "32"),
               textvariable=varL)
textL.place(relx=0.77, rely=0.101)
labLAB_A = Label(text="A",
                font=("Times New Roman", "36"),
                bg="#FFDEAD")
labLAB_A.place(relx=0.57, rely=0.18)
textA = Entry(MainWindow,
               width=7,
               bd=5,
               font=("Times New Roman", "32"),
               textvariable=varA)
textA.place(relx=0.77, rely=0.176)
labLAB_B = Label(text="B",
                font=("Times New Roman", "36"),
                bg="#FFDEAD")
labLAB_B.place(relx=0.57, rely=0.26)
textB = Entry(MainWindow,
               width=7,
               bd=5,
               font=("Times New Roman", "32"),
               textvariable=varB)
textB.place(relx=0.77, rely=0.251)



labXYZ_X = Label(text="X",
                font=("Times New Roman", "36"),
                bg="#FFDEAD")
textX = Entry(MainWindow,
               width=7,
               bd=5,
               font=("Times New Roman", "32"),
               textvariable=varX,
               state=DISABLED)
textX.place(relx=0.77, rely=0.423)
labXYZ_X.place(relx=0.57, rely=0.42)
labXYZ_Y = Label(text="Y",
                font=("Times New Roman", "36"),
                bg="#FFDEAD")
labXYZ_Y.place(relx=0.57, rely=0.5)
textY = Entry(MainWindow,
               width=7,
               bd=5,
               font=("Times New Roman", "32"),
               textvariable=varY,
               state=DISABLED)
textY.place(relx=0.77, rely=0.498)
labXYZ_Z = Label(text="Z",
                font=("Times New Roman", "36"),
                bg="#FFDEAD")
labXYZ_Z.place(relx=0.57, rely=0.58)
textZ = Entry(MainWindow,
               width=7,
               bd=5,
               font=("Times New Roman", "32"),
               textvariable=varZ,
               state=DISABLED)
textZ.place(relx=0.77, rely=0.573)


labHSV_H = Label(text="H",
                font=("Times New Roman", "36"),
                bg="#FFDEAD")
labHSV_H.place(relx=0.57, rely=0.74)
textH = Entry(MainWindow,
               width=7,
               bd=5,
               font=("Times New Roman", "32"),
               textvariable=varH,
               state=DISABLED)
textH.place(relx=0.77, rely=0.74)

labHSV_S = Label(text="S",
                font=("Times New Roman", "36"),
                bg="#FFDEAD")
labHSV_S.place(relx=0.57, rely=0.82)
textS = Entry(MainWindow,
               width=7,
               bd=5,
               font=("Times New Roman", "32"),
               textvariable=varS,
               state=DISABLED)
textS.place(relx=0.77, rely=0.815)
labHSV_V = Label(text="V",
                font=("Times New Roman", "36"),
                bg="#FFDEAD")
labHSV_V.place(relx=0.57, rely=0.9)
textV = Entry(MainWindow,
               width=7,
               bd=5,
               font=("Times New Roman", "32"),
               textvariable=varV,
               state=DISABLED)
textV.place(relx=0.77, rely=0.89)


def SetLAB_Foo():
    global state
    state = 1
    textV["state"] = DISABLED
    textH["state"] = DISABLED
    textS["state"] = DISABLED
    textX["state"] = DISABLED
    textY["state"] = DISABLED
    textZ["state"] = DISABLED
    textL["state"] = NORMAL
    textA["state"] = NORMAL
    textB["state"] = NORMAL


def SetXYZ_Foo():
    global state
    state = 2
    textV["state"] = DISABLED
    textH["state"] = DISABLED
    textS["state"] = DISABLED
    textL["state"] = DISABLED
    textA["state"] = DISABLED
    textB["state"] = DISABLED
    textX["state"] = NORMAL
    textY["state"] = NORMAL
    textZ["state"] = NORMAL


def SetHSV_Foo():
    global state
    state = 3
    textX["state"] = DISABLED
    textY["state"] = DISABLED
    textZ["state"] = DISABLED
    textL["state"] = DISABLED
    textA["state"] = DISABLED
    textB["state"] = DISABLED
    textH["state"] = NORMAL
    textS["state"] = NORMAL
    textV["state"] = NORMAL


btnLAB = Button(text="LAB",
               bg="#DAA520",
               fg="#000000",
               font=("Times New Roman", "36"),
               bd=10,
               command=SetLAB_Foo)
btnLAB.place(relx=0.4, rely=0.1)

btnXYZ = Button(text="XYZ",
               bg="#DAA520",
               fg="#000000",
               font=("Times New Roman", "36"),
               bd=10,
               command=SetXYZ_Foo)
btnXYZ.place(relx=0.4, rely=0.42)


btnHSV = Button(text="HSV",
               bg="#DAA520",
               fg="#000000",
               font=("Times New Roman", "36"),
               bd=10,
               command=SetHSV_Foo)
btnHSV.place(relx=0.4, rely=0.73)


def convert():
    global varL
    global varA
    global varB
    global varX
    global varY
    global varZ
    global varH
    global varS
    global varV
    global state
    global previous
    btnConvert["text"] = "Retry"
    if state == 1:
        previous = state
        state = 4
        btnHSV["state"] = DISABLED
        btnXYZ["state"] = DISABLED
        btnLAB["state"] = DISABLED
        textL["state"] = DISABLED
        textA["state"] = DISABLED
        textB["state"] = DISABLED
        l = varL.get()
        a = varA.get()
        b = varB.get()
        lab = LabColor(l,a,b)
        xyz = convert_color(lab,XYZColor)
        hsv = convert_color(lab, HSVColor)
        varX.set(round(xyz.xyz_x,3))
        varY.set(round(xyz.xyz_y,3))
        varZ.set(round(xyz.xyz_z,3))
        varH.set(round(hsv.hsv_h,3))
        varS.set(round(hsv.hsv_s,3))
        varV.set(round(hsv.hsv_v,3))
    elif state == 2:
        previous = state
        state = 4
        btnHSV["state"] = DISABLED
        btnXYZ["state"] = DISABLED
        btnLAB["state"] = DISABLED
        textX["state"] = DISABLED
        textY["state"] = DISABLED
        textZ["state"] = DISABLED
        x = varX.get()
        y = varY.get()
        z = varZ.get()
        xyz = XYZColor(x,y,z)
        lab = convert_color(xyz, LabColor)
        hsv = convert_color(xyz, HSVColor)
        varL.set(round(lab.lab_l))
        varA.set(round(lab.lab_a))
        varB.set(round(lab.lab_b))
        varH.set(round(hsv.hsv_h))
        varS.set(round(hsv.hsv_s))
        varV.set(round(hsv.hsv_v))
    elif state == 3:
        previous = state
        btnHSV["state"] = DISABLED
        btnXYZ["state"] = DISABLED
        btnLAB["state"] = DISABLED
        textV["state"] = DISABLED
        textH["state"] = DISABLED
        textS["state"] = DISABLED
        state = 4
        h = varH.get()
        s = varS.get()
        v = varV.get()
        hsv = HSVColor(h,s,v)
        lab = convert_color(hsv, LabColor)
        xyz = convert_color(hsv, XYZColor)
        varL.set(round(lab.lab_l))
        varA.set(round(lab.lab_a))
        varB.set(round(lab.lab_b))
        varX.set(round(xyz.xyz_x))
        varY.set(round(xyz.xyz_y))
        varZ.set(round(xyz.xyz_z))
    else:
        btnHSV["state"] = NORMAL
        btnXYZ["state"] = NORMAL
        btnLAB["state"] = NORMAL
        varL.set(0)
        varA.set(0)
        varB.set(0)
        varX.set(0)
        varY.set(0)
        varZ.set(0)
        varH.set(0)
        varS.set(0)
        varV.set(0)
        btnConvert["text"] = "Convert"
        if previous == 1:
            SetLAB_Foo()
        elif previous == 2:
            SetXYZ_Foo()
        else:
            SetHSV_Foo()





btnConvert = Button(text="Convert",
                 bg="#DAA520",
                 fg="#000000",
                 font=("Times New Roman", "36"),
                 bd=10,
                 command=convert)
btnConvert.place(relx=0.03, rely=0.65)

btnExit = Button(text="Выход",
                 bg="#DAA520",
                 fg="#000000",
                 font=("Times New Roman", "36"),
                 bd=10,
                 command=MainWindow.quit)
btnExit.place(relx=0.03, rely=0.82)


# labChosenColor = Label(text="Выбранный цвет:",
#                   font=("Times New Roman", "28"),
#                   bg="#FFDEAD")
# labChosenColor.place(relx=0.04, rely=0.14)
#
#
# colorDialog = colorchooser.Chooser(MainWindow)
#
# def openColorDialog():
#     global varR
#     global varG
#     global varB
#     global varX
#     global varY
#     global varZ
#     global varH
#     global varS
#     global varV
#     color = colorDialog.show()
#     messagebox.showinfo("Заметка", "Выбранный вами цвет: " + color[1] + "\n" +
#                                 "R = " + str(color[0][0]) + " , G = " + str(color[0][1]) + " , B = " + str(color[0][2]))
#     varR.set(int(color[0][0]))
#     varG.set(int(color[0][1]))
#     varB.set(int(color[0][2]))
#     xyz_list = FromRgbToXYZ(varR.get(), varG.get(), varB.get())
#     varX.set(xyz_list[0])
#     varY.set(xyz_list[1])
#     varZ.set(xyz_list[2])
#     hsv_list = FromRgbToHSV(varR.get(), varG.get(), varB.get())
#     varH.set(hsv_list[0])
#     varS.set(hsv_list[1])
#     varV.set(hsv_list[2])
#     canvas.config(bg=color[1])
#
# btnChooseColor = Button(text="Выбрать цвет из палитры",
#                         bg="#DAA520",
#                         fg="#000000",
#                         font=("Times New Roman", "36"),
#                         bd=10,
#                         command=openColorDialog)
# btnChooseColor.pack()
# btnChooseColor.place(relx=0.17, rely=0.82)
#
# def FromRGBtoColorHex(R, G, B):
#     return '#%02x%02x%02x' % (int(R.get()), int(G.get()), int(B.get()))
#
# def g(x):
#     if x >= 0.04045:
#         return ((x + 0.055)/1.055) ** 2.4
#     else:
#         return x/12.92
#
# def FromRgbToXYZ(R, G, B):
#     xyz_list = []
#     Rn = g(R / 255)*100
#     Gn = g(G / 255)*100
#     Bn = g(B / 255)*100
#     X = Bn * 0.180437 + Gn * 0.357576 + Rn * 0.412456
#     Y = Bn * 0.072175 + Gn * 0.715152 + Rn * 0.212673
#     Z = Bn * 0.950304 + Gn * 0.119192 + Rn * 0.0193339
#     if X > 100.0 or Y > 100.0 or Z > 100.0:
#         labWarning.place(relx=0.28, rely=0.1)
#     else:
#         labWarning.place_forget()
#     xyz_list.append(X)
#     xyz_list.append(Y)
#     xyz_list.append(Z)
#     return xyz_list
#
# def FromXYZtoRgb(X, Y, Z):
#     X /= 100
#     Y /= 100
#     Z /= 100
#     R = 3.2404542 * X - 1.5371385 * Y - 0.4985314 * Z
#     G = -0.9692660 * X + 1.8760108 * Y + 0.0415560 * Z
#     B = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
#     R *= 255
#     G *= 255
#     B *= 255
#     rgb_list = [R, G, B]
#     if rgb_list[0] > 255.0 or rgb_list[1] > 255.0 or rgb_list[2] > 255.0:
#         labWarning.place(relx=0.28, rely=0.1)
#     else:
#         labWarning.place_forget()
#     return rgb_list
#
# def FromRgbToHSV(R, G, B):
#     hsv_list = list(colorsys.rgb_to_hsv(R, G, B))
#     hsv_list[0] *= 100
#     hsv_list[1] *= 100
#     hsv_list[2] *= (100 / 255)
#     return hsv_list
#
# def FromHSVtoRgb(H, S, V):
#     H /= 100
#     S /= 100
#     V /= (100/255)
#     rgb_list = list(colorsys.hsv_to_rgb(H, S, V))
#     return rgb_list
#
# def changeColorFromRGB(scaleInfo):
#     global canvas
#     global varR
#     global varG
#     global varB
#     global varX
#     global varY
#     global varZ
#     global varH
#     global varS
#     global varV
#     xyz_list = FromRgbToXYZ(varR.get(), varG.get(), varB.get())
#     varX.set(xyz_list[0])
#     varY.set(xyz_list[1])
#     varZ.set(xyz_list[2])
#     hsv_list = FromRgbToHSV(varR.get(), varG.get(), varB.get())
#     varH.set(hsv_list[0])
#     varS.set(hsv_list[1])
#     varV.set(hsv_list[2])
#     canvas.config(bg=FromRGBtoColorHex(varR, varG, varB))
#
# def changeColorFromXYZ(scaleInfo):
#     global canvas
#     global varR
#     global varG
#     global varB
#     global varX
#     global varY
#     global varZ
#     global varH
#     global varS
#     global varV
#     rgb_list = FromXYZtoRgb(varX.get(), varY.get(), varZ.get())
#     varR.set(rgb_list[0])
#     varG.set(rgb_list[1])
#     varB.set(rgb_list[2])
#     hsv_list = FromRgbToHSV(varR.get(), varG.get(), varB.get())
#     varH.set(hsv_list[0])
#     varS.set(hsv_list[1])
#     varV.set(hsv_list[2])
#     canvas.config(bg=FromRGBtoColorHex(varR, varG, varB))
#
# def changeColorFromHSV(scaleInfo):
#     global canvas
#     global varR
#     global varG
#     global varB
#     global varX
#     global varY
#     global varZ
#     global varH
#     global varS
#     global varV
#     rgb_list = FromHSVtoRgb(varH.get(), varS.get(), varV.get())
#     varR.set(rgb_list[0])
#     varG.set(rgb_list[1])
#     varB.set(rgb_list[2])
#     xyz_list = FromRgbToXYZ(varR.get(), varG.get(), varB.get())
#     varX.set(xyz_list[0])
#     varY.set(xyz_list[1])
#     varZ.set(xyz_list[2])
#     canvas.config(bg=FromRGBtoColorHex(varR, varG, varB))
#
#
#
#
# btnSetR_Flag = True
#
# def SetR_Foo():
#     global varR
#     global btnSetR_Flag
#     if btnSetR_Flag:
#         textR.config(state="normal")
#         btnSetR.config(text="Подтвердить R")
#         btnSetR_Flag = False
#     else:
#         changeColorFromRGB("SetR_Foo")
#         textR.config(state="disabled")
#         btnSetR.config(text="Задать точное R")
#         btnSetR_Flag = True
#
# btnSetR = Button(text="Задать точное R",
#                         bg="#DAA520",
#                         fg="#000000",
#                         font=("Times New Roman", "14"),
#                         bd=10,
#                         command=SetR_Foo,
#                         padx=5,
#                         pady=5)
# btnSetR.place(relx=0.81, rely=0.101)
#
# btnSetG_Flag = True
#
# def SetG_Foo():
#     global varG
#     global btnSetG_Flag
#     if btnSetG_Flag:
#         textG.config(state="normal")
#         btnSetG.config(text="Подтвердить G")
#         btnSetG_Flag = False
#     else:
#         changeColorFromRGB("SetG_Foo")
#         textG.config(state="disabled")
#         btnSetG.config(text="Задать точное G")
#         btnSetG_Flag = True
#
# btnSetG = Button(text="Задать точное G",
#                         bg="#DAA520",
#                         fg="#000000",
#                         font=("Times New Roman", "14"),
#                         bd=10,
#                         command=SetG_Foo,
#                         padx=5,
#                         pady=5)
# btnSetG.pack()
# btnSetG.place(relx=0.81, rely=0.176)
#
#
#
# btnSetB_Flag = True
#
# def SetB_Foo():
#     global varB
#     global btnSetB_Flag
#     if btnSetB_Flag:
#         textB.config(state="normal")
#         btnSetB.config(text="Подтвердить B")
#         btnSetB_Flag = False
#     else:
#         changeColorFromRGB("SetB_Foo")
#         textB.config(state="disabled")
#         btnSetB.config(text="Задать точное B")
#         btnSetB_Flag = True
#
# btnSetB = Button(text="Задать точное B",
#                         bg="#DAA520",
#                         fg="#000000",
#                         font=("Times New Roman", "14"),
#                         bd=10,
#                         command=SetB_Foo,
#                         padx=5,
#                         pady=5)
# btnSetB.pack()
# btnSetB.place(relx=0.81, rely=0.251)
#
# labXYZ = Label(text="XYZ",
#                font=("Times New Roman", "48"),
#                bg="#FFDEAD")
# labXYZ.pack()
# labXYZ.place(relx=0.67, rely=0.33)
#
#
#
# btnSetX_Flag = True
#
# def SetX_Foo():
#     global varX
#     global btnSetX_Flag
#     if btnSetX_Flag:
#         textX.config(state="normal")
#         btnSetX.config(text="Подтвердить X")
#         btnSetX_Flag = False
#     else:
#         changeColorFromXYZ("SetX_Foo")
#         textX.config(state="disabled")
#         btnSetX.config(text="Задать точное X")
#         btnSetX_Flag = True
#
# btnSetX = Button(text="Задать точное X",
#                         bg="#DAA520",
#                         fg="#000000",
#                         font=("Times New Roman", "14"),
#                         bd=10,
#                         command=SetX_Foo,
#                         padx=5,
#                         pady=5)
# btnSetX.pack()
# btnSetX.place(relx=0.81, rely=0.423)
#
#
#
# btnSetY_Flag = True
#
# def SetY_Foo():
#     global varY
#     global btnSetY_Flag
#     if btnSetY_Flag:
#         textY.config(state="normal")
#         btnSetY.config(text="Подтвердить Y")
#         btnSetY_Flag = False
#     else:
#         changeColorFromXYZ("SetY_Foo")
#         textY.config(state="disabled")
#         btnSetY.config(text="Задать точное Y")
#         btnSetY_Flag = True
#
# btnSetY = Button(text="Задать точное Y",
#                         bg="#DAA520",
#                         fg="#000000",
#                         font=("Times New Roman", "14"),
#                         bd=10,
#                         command=SetY_Foo,
#                         padx=5,
#                         pady=5)
# btnSetY.pack()
# btnSetY.place(relx=0.81, rely=0.498)
#
#
#
# btnSetZ_Flag = True
#
# def SetZ_Foo():
#     global varZ
#     global btnSetZ_Flag
#     if btnSetZ_Flag:
#         textZ.config(state="normal")
#         btnSetZ.config(text="Подтвердить Z")
#         btnSetZ_Flag = False
#     else:
#         changeColorFromXYZ("SetZ_Foo")
#         textZ.config(state="disabled")
#         btnSetZ.config(text="Задать точное Z")
#         btnSetZ_Flag = True
#
# btnSetZ = Button(text="Задать точное Z",
#                         bg="#DAA520",
#                         fg="#000000",
#                         font=("Times New Roman", "14"),
#                         bd=10,
#                         command=SetZ_Foo,
#                         padx=5,
#                         pady=5)
# btnSetZ.pack()
# btnSetZ.place(relx=0.81, rely=0.573)
#
# labHSV = Label(text="HSV",
#                font=("Times New Roman", "48"),
#                bg="#FFDEAD")
# labHSV.pack()
# labHSV.place(relx=0.67, rely=0.65)
#


#
# scrollH = Scale(bg="#DAA520",
#                 activebackground="#B8860B",
#                 fg="#000000",
#                 highlightbackground="#DAA520",
#                 bd=3,
#                 orient=HORIZONTAL,
#                 sliderlength=20,
#                 length=256,
#                 width=20,
#                 to=100,
#                 relief="ridge",
#                 troughcolor="#FFF8DC",
#                 command=changeColorFromHSV,
#                 variable=varH)
# scrollH.pack()
# scrollH.place(relx=0.62, rely=0.743)
##
# btnSetH_Flag = True
#
# def SetH_Foo():
#     global varH
#     global btnSetH_Flag
#     if btnSetH_Flag:
#         textH.config(state="normal")
#         btnSetH.config(text="Подтвердить H")
#         btnSetH_Flag = False
#     else:
#         changeColorFromHSV("SetH_Foo")
#         textH.config(state="disabled")
#         btnSetH.config(text="Задать точное H")
#         btnSetH_Flag = True
#
# btnSetH = Button(text="Задать точное H",
#                         bg="#DAA520",
#                         fg="#000000",
#                         font=("Times New Roman", "14"),
#                         bd=10,
#                         command=SetH_Foo,
#                         padx=5,
#                         pady=5)
# btnSetH.pack()
# btnSetH.place(relx=0.81, rely=0.74)
#
#
# scrollS = Scale(bg="#DAA520",
#                 activebackground="#B8860B",
#                 fg="#000000",
#                 highlightbackground="#DAA520",
#                 bd=3,
#                 orient=HORIZONTAL,
#                 sliderlength=20,
#                 length=256,
#                 width=20,
#                 to=100,
#                 relief="ridge",
#                 troughcolor="#FFF8DC",
#                 command=changeColorFromHSV,
#                 variable=varS)
# scrollS.pack()
# scrollS.place(relx=0.62, rely=0.823)
#
#
# btnSetS_Flag = True
#
# def SetS_Foo():
#     global varS
#     global btnSetS_Flag
#     if btnSetS_Flag:
#         textS.config(state="normal")
#         btnSetS.config(text="Подтвердить S")
#         btnSetS_Flag = False
#     else:
#         changeColorFromHSV("SetS_Foo")
#         textS.config(state="disabled")
#         btnSetS.config(text="Задать точное S")
#         btnSetS_Flag = True
#
# btnSetS = Button(text="Задать точное S",
#                         bg="#DAA520",
#                         fg="#000000",
#                         font=("Times New Roman", "14"),
#                         bd=10,
#                         command=SetS_Foo,
#                         padx=5,
#                         pady=5)
# btnSetS.place(relx=0.81, rely=0.815)
#
#
#
# btnSetV_Flag = True
#
# def SetV_Foo():
#     global varV
#     global btnSetV_Flag
#     if btnSetV_Flag:
#         textV.config(state="normal")
#         btnSetV.config(text="Подтвердить V")
#         btnSetV_Flag = False
#     else:
#         changeColorFromHSV("SetV_Foo")
#         textV.config(state="disabled")
#         btnSetV.config(text="Задать точное V")
#         btnSetV_Flag = True
#
# btnSetV = Button(text="Задать точное V",
#                         bg="#DAA520",
#                         fg="#000000",
#                         font=("Times New Roman", "14"),
#                         bd=10,
#                         command=SetV_Foo,
#                         padx=5,
#                         pady=5)
# btnSetV.place(relx=0.81, rely=0.89)

MainWindow.mainloop()