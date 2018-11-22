from tkinter import *
class Cadastro(Tk):
    def __init__(self):
        super().__init__()
        self.cadastro = Tk()
        self.cadastro.geometry("400x400")

        self.n1=Label(self,text="Nome: ")

