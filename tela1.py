from tkinter import *
janela = Tk()
janela.geometry("400x100")
janela.title("Programa Top 2.0")

label1 = Label(janela, text="Olá, Pessoal!",
               fg="blue", bg="yellow", 
               font=("Arial",16,"bold"))
label1.grid(row=0, column=0)

label2 = Label(janela, text="Tudo bem?",
               fg="red", bg="pink",
               font=("Times New Roman",18,"italic"))
label2.grid(row=1,column=1)

botao = Button(janela, text="Sair", width=15,
               command=quit)
botao.grid(row=2, column=2)

def mensagem():
    print("Olha só, que legal")

botao_msg = Button(janela, text="Mensagem",
                   command=mensagem)
botao_msg.grid(row=2, column=1)

janela.mainloop()