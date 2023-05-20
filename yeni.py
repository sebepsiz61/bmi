from tkinter import *
from tkinter import messagebox

pencere = Tk()
pencere.title('Vücut Kitle İndex Hesaplama')
pencere.minsize(width=300 , height=200)



yazi = Label(text="Vücut Kitle İndex Hesaplama")
yazi.config(bg="silver")
yazi.config(fg="black")
kg = Label(text="Kilonuzu Girin (kg)")
uzun = Label(text="Boyunuzu Girim (cm)")
boy1 = Entry(width=10)

kilo1 = Entry(width=10)

def hesapla():
    while True:
        try:
            boy = float(boy1.get())/100
            kilo = float(kilo1.get())
            hesap = kilo / (boy * boy)
            hesap =round(hesap, 1)


            if type (hesap) == float :

                if hesap < 18.5:
                    messagebox.showinfo('Vücut kitle hesaplama',f"Vücut kitle indeksiniz: {hesap}, zayıfsınız")
                    break
                elif hesap < 25:
                    messagebox.showinfo('Vücut kitle hesaplama',f"Vücut kitle indeksiniz: {hesap}, kilonuz normal")
                    break
                elif hesap < 30:
                    messagebox.showinfo('Vücut kitle hesaplama',f"Vücut kitle indeksiniz: {hesap}, kilonuz biraz fazla")
                    break
                elif hesap < 35:
                    messagebox.showinfo('Vücut kitle hesaplama', f"Vücut kitle indeksiniz: {hesap}, 1. derece obezsiniz")
                    break
                elif hesap < 40:
                    messagebox.showinfo('Vücut kitle hesaplama',f"Vücut kitle indeksiniz: {hesap}, 2. derece obezsiniz")
                    break
            else:
                    messagebox.showerror('Vücut kitle hesaplama',f"Vücut kitle indeksiniz: {hesap}, 3. derece obezsiniz.")
                    break

        except :
                messagebox.showinfo('Vücut kitle hesaplama',f"Rakam girmelisiniz")
                break


buton = Button(text="Buton", command=hesapla )
buton.config(padx=10, pady=10)



yazi.pack()
uzun.pack()
boy1.pack()
kg.pack()
kilo1.pack()
buton.pack()

pencere.mainloop()