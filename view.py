from tkinter import *
from venda import Tela_venda

class Patio_1(Tk):
    def __init__(self, controle):
        super().__init__()

        self.controle=controle
        self["bg"] = "beige"
        self.geometry("400x400")
        self.title("Concessionaria TINOVO ")

        self.headfont = ("Arial", "20", "bold")

        self.head = Label(self, text="Concessionaria", font=self.headfont,bg="beige")


        self.bt = Button(self, width=10, height=3, text="UNO",command=self.btn_venda)
        self.bt2 = Button(self, width=10, height=3, text="Hilux")
        self.bt3 = Button(self, width=10, height=3, text="UP")
        self.bt4 = Button(self, width=10, height=3, text="KA")
        self.bt5 = Button(self, width=10, height=3, text="CORSA")

        self.head.grid(row=1,column=1,padx=1,pady=20)
        self.bt.grid(row=3,column=0, padx= 1, pady=10)
        self.bt2.grid(row=3,column=1,padx= 1, pady=10)
        self.bt3.grid(row=3,column=2, padx= 1, pady=10)
        self.bt4.grid(row=4,column=0, padx= 1, pady=10)
        self.bt5.grid(row=4,column=1, padx= 1, pady=10)

    def btn_venda(self):
        Tela_venda()







