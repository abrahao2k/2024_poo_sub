from tkinter import *

janela = Tk()

label_nome = Label(janela,text="Seu nome:")
label_nome.grid(row=0,column=0)

entry_nome = Entry(janela, width=30)
entry_nome.grid(row=0,column=1)

label_msg = Label(janela,text=" ")
label_msg.grid(row=1,column=1)

def msg():
    nome = entry_nome.get()
    label_msg.config(text = f"Seja bem vindo, {nome}.")

botao_ok = Button(janela, text="OK", command=msg)
botao_ok.grid(row=0,column=2)

janela.mainloop()