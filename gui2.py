
from tkinter import *
import tkinter.filedialog
import os
import tkinter.scrolledtext as ScrolledText

ListaElementos = [["n","n","v","n"],["a","e","A","a"],["a","r","r","A"],["A","A","r","r"],["v","v","v","v"]]
ListaObj = []
ListaObj2 = []

ListaEstados1 = [[0,5,5,5],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
ListaEstados2 = [[0,5,5,5],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]

root = Tk()
root.title('Torre de Babilonia')
w = 970 # El largo de la ventana
h = 800 # La altura de la ventana

# Obtener el largo y alto de la ventana
ws = root.winfo_screenwidth() # Largo de la ventana
hs = root.winfo_screenheight() # Altura de la ventana

# Se calculan las coordenadas x,y de la ventana root creada
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window=Canvas(root)
window.pack(expand=True, fill=BOTH)

image1=PhotoImage(file="Imagenes/fondo.png")
window.img=image1
window.create_image(0, 0, anchor=NW, image=image1)

#b1=Button(window, text="Hello", bd=0)
#window.create_window(20,20, window=b1, anchor=NW, width=150, height=150)

#Se asignan las imagenes de la torre de babilonia a una variable
TowerFontA = PhotoImage(file="Imagenes/Font1.png")
TowerFontB = PhotoImage(file="Imagenes/Font2.png")
TowerFontC = PhotoImage(file="Imagenes/Font3.png")
TowerFontD = PhotoImage(file="Imagenes/Font4.png")

#Se asignan los colores de las bolas a variables
imageBall_Green = PhotoImage(file="Imagenes/small_ball_green.png")
imageBall_Red = PhotoImage(file="Imagenes/small_ball_red.png")
imageBall_Blue = PhotoImage(file="Imagenes/small_ball_blue.png")
imageBall_Yellow = PhotoImage(file="Imagenes/small_ball_yellow.png")
imageBall_Empty = PhotoImage(file="Imagenes/small_ball_black.png")
image_Tiny = PhotoImage(file="Imagenes/image_tiny.png")

#Crea la torre
labelTower1 = Label(window,image = TowerFontA)
window.create_window(20,290, window=labelTower1, anchor=NW, width=279, height=300)
#Crea la torre2
labelTower2 = Label(window,image = TowerFontA)
window.create_window(320,290, window=labelTower2, anchor=NW, width=279, height=300)

def funcionVacia():
    pass


#Declara los labels de cada elemento de la torre
ListaObj.append(Button(window,image = imageBall_Empty,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj.append(Button(window,image = image_Tiny     ,borderwidth=0,highlightthickness=0, command=lambda: funcionVacia()))
ListaObj.append(Button(window,image = image_Tiny     ,borderwidth=0,highlightthickness=0, command=lambda: funcionVacia()))
ListaObj.append(Button(window,image = image_Tiny     ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia()))

ListaObj.append(Button(window,image = imageBall_Red   ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj.append(Button(window,image = imageBall_Blue  ,borderwidth=0,highlightthickness=0, command=lambda: funcionVacia()))
ListaObj.append(Button(window,image = imageBall_Green ,borderwidth=0,highlightthickness=0, command=lambda: funcionVacia()))
ListaObj.append(Button(window,image = imageBall_Yellow,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))

ListaObj.append(Button(window,image = imageBall_Red   ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj.append(Button(window,image = imageBall_Blue  ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj.append(Button(window,image = imageBall_Green ,borderwidth=0,highlightthickness=0, command=lambda: funcionVacia()))
ListaObj.append(Button(window,image = imageBall_Yellow,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))

ListaObj.append(Button(window,image = imageBall_Red   ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia()))
ListaObj.append(Button(window,image = imageBall_Blue  ,borderwidth=0,highlightthickness=0, command=lambda: funcionVacia()))
ListaObj.append(Button(window,image = imageBall_Green ,borderwidth=0,highlightthickness=0, command=lambda: funcionVacia()))
ListaObj.append(Button(window,image = imageBall_Yellow,borderwidth=0,highlightthickness=0, command=lambda: funcionVacia()))

ListaObj.append(Button(window,image = imageBall_Red   ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj.append(Button(window,image = imageBall_Blue  ,borderwidth=0,highlightthickness=0, command=lambda: funcionVacia()))
ListaObj.append(Button(window,image = imageBall_Green ,borderwidth=0,highlightthickness=0, command=lambda: funcionVacia()))
ListaObj.append(Button(window,image = imageBall_Yellow,borderwidth=0,highlightthickness=0, command=lambda: funcionVacia()))

#Crea los labels de la torre
window.create_window(36 ,305, window=ListaObj[0] , anchor=NW, width=50, height=50)
window.create_window(103,305, window=ListaObj[1] , anchor=NW, width=50, height=50)
window.create_window(168,305, window=ListaObj[2] , anchor=NW, width=50, height=50)
window.create_window(233,305, window=ListaObj[3] , anchor=NW, width=50, height=50)

window.create_window(36 ,361, window=ListaObj[4] , anchor=NW, width=50, height=50)
window.create_window(103,361, window=ListaObj[5] , anchor=NW, width=50, height=50)
window.create_window(168,361, window=ListaObj[6] , anchor=NW, width=50, height=50)
window.create_window(233,361, window=ListaObj[7] , anchor=NW, width=50, height=50)

window.create_window(36 ,415, window=ListaObj[8] , anchor=NW, width=50, height=50)
window.create_window(103,415, window=ListaObj[9] , anchor=NW, width=50, height=50)
window.create_window(168,415, window=ListaObj[10], anchor=NW, width=50, height=50)
window.create_window(233,415, window=ListaObj[11], anchor=NW, width=50, height=50)

window.create_window(36 ,470, window=ListaObj[12], anchor=NW, width=50, height=50)
window.create_window(103,470, window=ListaObj[13], anchor=NW, width=50, height=50)
window.create_window(168,470, window=ListaObj[14], anchor=NW, width=50, height=50)
window.create_window(233,470, window=ListaObj[15], anchor=NW, width=50, height=50)

window.create_window(36 ,525, window=ListaObj[16], anchor=NW, width=50, height=50)
window.create_window(103,525, window=ListaObj[17], anchor=NW, width=50, height=50)
window.create_window(168,525, window=ListaObj[18], anchor=NW, width=50, height=50)
window.create_window(233,525, window=ListaObj[19], anchor=NW, width=50, height=50)

window.create_window(36 ,305, window=ListaObj[0] , anchor=NW, width=50, height=50)
window.create_window(103,305, window=ListaObj[1] , anchor=NW, width=50, height=50)
window.create_window(168,305, window=ListaObj[2] , anchor=NW, width=50, height=50)
window.create_window(233,305, window=ListaObj[3] , anchor=NW, width=50, height=50)

def CambiaEstado(estado, ListaObjetos,Posiciones,x,y):
    global v
    global ListaEstados1
    global ListaEstados2
    if (v.get() == 2 and x!=0):
        if (Posiciones [x][y]==1):
            Posiciones [x][y]=2
            ListaObjetos[4*x+y].config(image = imageBall_Blue)
        elif (Posiciones [x][y]==2):
            Posiciones [x][y]=3
            ListaObjetos[4*x+y].config(image = imageBall_Green)
        elif (Posiciones [x][y]==3):
            Posiciones [x][y]=4
            ListaObjetos[4*x+y].config(image = imageBall_Yellow)
        elif (Posiciones [x][y]==4):
            Posiciones [x][y]=0
            ListaObjetos[4*x+y].config(image = imageBall_Empty)
        elif (Posiciones [x][y]==0):
            Posiciones [x][y]=1
            ListaObjetos[4*x+y].config(image = imageBall_Red)
        if (estado == 1):
            ListaEstados1 = Posiciones
        else:
            ListaEstados2 = Posiciones
    VerificaManual()




#CARGA LA SEGUNDA TORRE DE BABILONIA
ListaObj2.append(Button(window,image = imageBall_Empty,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj2.append(Button(window,image = image_Tiny     ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj2.append(Button(window,image = image_Tiny     ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj2.append(Button(window,image = image_Tiny     ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))

ListaObj2.append(Button(window,image = imageBall_Red   ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj2.append(Button(window,image = imageBall_Blue  ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj2.append(Button(window,image = imageBall_Green ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj2.append(Button(window,image = imageBall_Yellow,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))

ListaObj2.append(Button(window,image = imageBall_Red   ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia()))
ListaObj2.append(Button(window,image = imageBall_Blue  ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj2.append(Button(window,image = imageBall_Green ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj2.append(Button(window,image = imageBall_Yellow,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))

ListaObj2.append(Button(window,image = imageBall_Red   ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj2.append(Button(window,image = imageBall_Blue  ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj2.append(Button(window,image = imageBall_Green ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj2.append(Button(window,image = imageBall_Yellow,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia()))

ListaObj2.append(Button(window,image = imageBall_Red   ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj2.append(Button(window,image = imageBall_Blue  ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj2.append(Button(window,image = imageBall_Green ,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))
ListaObj2.append(Button(window,image = imageBall_Yellow,borderwidth=0,highlightthickness=0, command=lambda:funcionVacia() ))

#Crea los labels de la torre
window.create_window(336 ,305, window=ListaObj2[0] , anchor=NW, width=50, height=50)
window.create_window(403,305, window=ListaObj2[1] , anchor=NW, width=50, height=50)
window.create_window(468,305, window=ListaObj2[2] , anchor=NW, width=50, height=50)
window.create_window(533,305, window=ListaObj2[3] , anchor=NW, width=50, height=50)

window.create_window(336 ,361, window=ListaObj2[4] , anchor=NW, width=50, height=50)
window.create_window(403,361, window=ListaObj2[5] , anchor=NW, width=50, height=50)
window.create_window(468,361, window=ListaObj2[6] , anchor=NW, width=50, height=50)
window.create_window(533,361, window=ListaObj2[7] , anchor=NW, width=50, height=50)

window.create_window(336 ,415, window=ListaObj2[8] , anchor=NW, width=50, height=50)
window.create_window(403,415, window=ListaObj2[9] , anchor=NW, width=50, height=50)
window.create_window(468,415, window=ListaObj2[10], anchor=NW, width=50, height=50)
window.create_window(533,415, window=ListaObj2[11], anchor=NW, width=50, height=50)

window.create_window(336 ,470, window=ListaObj2[12], anchor=NW, width=50, height=50)
window.create_window(403,470, window=ListaObj2[13], anchor=NW, width=50, height=50)
window.create_window(468,470, window=ListaObj2[14], anchor=NW, width=50, height=50)
window.create_window(533,470, window=ListaObj2[15], anchor=NW, width=50, height=50)

window.create_window(336 ,525, window=ListaObj2[16], anchor=NW, width=50, height=50)
window.create_window(403,525, window=ListaObj2[17], anchor=NW, width=50, height=50)
window.create_window(468,525, window=ListaObj2[18], anchor=NW, width=50, height=50)
window.create_window(533,525, window=ListaObj2[19], anchor=NW, width=50, height=50)

window.create_window(336 ,305, window=ListaObj2[0] , anchor=NW, width=50, height=50)
window.create_window(403,305, window=ListaObj2[1] , anchor=NW, width=50, height=50)
window.create_window(468,305, window=ListaObj2[2] , anchor=NW, width=50, height=50)
window.create_window(533,305, window=ListaObj2[3] , anchor=NW, width=50, height=50)



#MODO AUTOMATICO----------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------

dirNameInicial=""
dirNameFinal=""

#Funcion que solicita la ruta de los archivos
def SolicitaRuta(opcion):
    global dirNameFinal
    global dirNameInicial
    if (opcion == 1):
        dirNameInicial = tkinter.filedialog.askopenfilename(title = "Configuración inicial",initialdir='./' )
    else:
        dirNameFinal = tkinter.filedialog.askopenfilename(title = "Configuración final",initialdir='./' )
    


#Boton que carga la ruta del archivo inicial
buttonConfInicial = Button(root, text="Carga configuración inicial", command=lambda :SolicitaRuta(1),state="disabled",width = 20)
window.create_window(10,35, window=buttonConfInicial , anchor=NW)


#Boton que carga la ruta del archivo final
buttonConfFinal = Button(root, text="Carga configuración final", command=lambda :SolicitaRuta(2),state="disabled",width = 20)
window.create_window(10,65, window=buttonConfFinal , anchor=NW)


#Boton que llama a la función generar para realizar operacion para el modo automatico
buttonSolucionAutomatico = Button(root, text="Cargar en torres",state="disabled",width = 20)
window.create_window(10,97, window=buttonSolucionAutomatico , anchor=NW)





#-----------------------------------------------------------------------------------------------------------------------------

global v
v = IntVar()


#------------------------------------------------------------------------------------------------------------------------------
# Se agregan las dimensiones a la ventana y su localizacion en pantalla
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.mainloop() # Crea la ventana
