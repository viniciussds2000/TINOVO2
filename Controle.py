from view import Patio_1

class Control ():
    def __init__(self):

        self.janela = Patio_1(self)
        self.janela.mainloop()

    def btn_venda(self):
        Tela_venda()