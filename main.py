from kivy.app import App
from kivy.lang import Builder




class ColecaoHW(App):
    def build(self):
        self.title='Catálogo HotWheels'
        return Builder.load_file('tela.kv')


ColecaoHW().run()
