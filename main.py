#importar o App
#Importar o Builder

from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("tela.kv")

class ColecaoHW(App):
    def build(self):
        return GUI
    
ColecaoHW().run()
