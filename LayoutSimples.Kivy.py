#conding: utf-8

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

Window.size= 600, 600

class Myapp(App):
    def build(self):
        layout = FloatLayout()
        global tex
        tex = TextInput(text='Digite aqui...')
        tex.size_hint= None, None
        tex.width= 500
        tex.height= 500
        tex.x= 200
        tex.y= 300    
       
        bt = Button(text='Enviar!')
        bt.size_hint=None, None
        bt.width= 200
        bt.height= 50
        bt.x=350
        bt.y=200
        bt.on_press= self.click

        
       
        layout.add_widget(tex)
        layout.add_widget(bt)

        return layout
    
    def click(self):
        print(tex.text)




      

app = Myapp()
app.title= 'Aplicativo'
app.run()