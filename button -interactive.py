# coding: utf-8



from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button




class AppMy(App):
    def build(self):
        return AppBase()
    
class AppBase(BoxLayout):
    def on_press_bt(self):
        app.root_window.remove_widget(app.root)
        app.root_window.add_widget(Tela02())


    def __init__(self, **kwargs):
        super(AppBase, self).__init__(**kwargs)
        self.orientation= "vertical"
        bt1 = Button(text="Clique")
        bt1.on_press = self.on_press_bt
        self.add_widget(bt1)
        self.add_widget(Button(text="Botão 2"))
        self.add_widget(Button(text="Botão 3"))

class Tela02(BoxLayout):
    
    def on_press_bt(self):
        app.root_window.remove_widget(app.root)
        app.root_window.add_widget(AppBase())

    def __init__(self, **kwargs):
        super(Tela02, self).__init__(**kwargs)
        self.orientation = 'vertical'
        bt = Button(text="Cheio!")
        bt.on_press = self.on_press_bt
        self.add_widget(bt)



    


if __name__ == '__main__':
    app = AppMy()
    app.run()