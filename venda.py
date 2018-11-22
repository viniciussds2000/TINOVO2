from tkinter import *

class Tela_venda(Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry("500x200")
        self.title("Vendas")
        self.transient(parent)
        self.grab_set()
        self.cad1=Label(self,text="Comprador: ")
        self.cad1.grid(row=1,column=1)

        self.cad1ed=Entry(self)
        self.cad1ed.grid(row=1,column=2)