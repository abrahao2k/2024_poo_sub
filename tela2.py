from tkinter import *
janela = Tk()

label = Label(janela,text="LEGAL")
label.grid(row=0,column=0)

def aumentar():
    label.config(text = label.cget("text") + "L")

botao = Button(janela,text="Aumentar", command=aumentar)
botao.grid(row=1,column=0)

janela.mainloop()