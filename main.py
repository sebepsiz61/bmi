from tkinter import *


pencere = Tk()
pencere.title('Python ??')
pencere.minsize(width=500 , height=600)
pencere.config(padx=20, pady=20)

yazi = Label(text="YAZIM")
yazi.config(bg="silver")
yazi.config(fg="black")
yazi.config(padx=20, pady=20)

yazi.pack()

def buton_tikla():
    #print("tıkla")
    print(yazi1.get("1.0", END))

Buton = Button(text="Buton" ,command=buton_tikla)
Buton.config(padx=10, pady=10)
Buton.pack()

onay = Entry(width=10, )
#onay.focus()
onay.pack()

yazi1 = Text(width=10, height=5)
#yazi1.focus()
yazi1.pack()

def surukle(value):
    print(value)

surukle = Scale(from_=0,to=100, command=surukle)
surukle.focus()
surukle.pack()

def box():
    print(box.get())

box = Spinbox(from_=0, to=50, command=box)
box.pack()

def sec_Buton():
    print(buton_sec.get())

buton_sec = IntVar()
sec = Checkbutton(text="seç", variable=buton_sec, command=sec_Buton)
sec.pack()

def rsec():
    print(radio1.get())
radio1 = IntVar()

rbuton = Radiobutton(text="1. Seçenek", value=10, variable=radio1,command=rsec)
rbuton2 = Radiobutton(text="2. Seçenek", value=20, variable=radio1,command=rsec)
rbuton.pack()
rbuton2.pack()

def liste_sec(event):
    print(liste.get(liste.curselection()))

liste = Listbox()
lliste = ["Onur", "Emine", "Şevval", "Ecrin"]
for i in range(len(lliste)):
    liste.insert(i,lliste[i])

liste.bind('<<ListboxSelect>>',liste_sec)
liste.pack()

pencere.mainloop()