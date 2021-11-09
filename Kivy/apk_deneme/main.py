from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder 
from kivy.uix.label import Label
Builder.load_file('main.kv')
class index(Screen):
    pass
sm = ScreenManager()
sm.add_widget(index(name='index'))
class TestApp(App):
    def build(self):
        return Label(text="Hello Kivy!")
if __name__ == '__main__':
    TestApp().run()