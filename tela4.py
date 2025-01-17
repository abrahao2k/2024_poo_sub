from tkinter import *

def somar():
    try:
        v1 = float(entry_v1.get())
        v2 = float(entry_v2.get())
        soma = v1 + v2
        entry_res.delete(0,END)
        entry_res.insert(0,str(soma))
    except:
        entry_res.delete(0,END)
        entry_res.insert(0,"Operação inválida!")

janela = Tk()
janela.geometry("220x110")
janela.title("Somador")

label_v1 = Label(janela,text="Valor 1: ")
label_v1.grid(row=0,column=0)

entry_v1 = Entry(janela, width=20)
entry_v1.grid(row=0,column=1)

label_v2 = Label(janela, text="Valor 2: ")
label_v2.grid(row=1,column=0)

entry_v2 = Entry(janela, width=20)
entry_v2.grid(row=1,column=1)

botao_somar = Button(janela,text="SOMAR",command=somar)
botao_somar.grid(row=2,column=1)

label_res = Label(janela,text="Resultado: ")
label_res.grid(row=3,column=0)

entry_res = Entry(janela,width=20)
entry_res.grid(row=3,column=1)

janela.mainloop()