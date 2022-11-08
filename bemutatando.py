from tkinter import *
from tkinter import messagebox
ablak = Tk()
ablak.title('Beadandó - FJ702U')
ablak.geometry("800x400")

def tisztit():
    textBox.delete(1.0, END)
    messagebox.showinfo(" ", "Tiszta lett a lap!")

def kilepes():
    ablak.destroy()
    messagebox.showinfo(" ", "Kiléptél!")

def mentes():
    txt_file = open('proba.txt', "w", encoding='utf-8')
    txt_file.write(textBox.get(1.0,END))
    messagebox.showinfo("", "Sikeres mentés!")

szoveg = Label(ablak,fg='red', text='Írj be a valamit!', font=('Arial',60))
szoveg.pack()

textBox = Text(ablak, width=50, height=5, font=("Arial",30))
textBox.pack()

gomb_kilepes = Button(ablak, text='Kilépés', command=kilepes ,width=15)
gomb_kilepes.pack(side=TOP)

gomb_tiszta = Button(ablak, text='Üres lap', command=tisztit, width=15)
gomb_tiszta.pack(side=TOP)

gomb_mentes = Button(ablak,text='Mentés txt. fájlba',command=mentes, width=15)
gomb_mentes.pack(side=TOP)

ablak.mainloop()