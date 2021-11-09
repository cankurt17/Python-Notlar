

from kivymd.app import  MDApp
from kivymd.uix.screen import Screen
from  kivy.lang import Builder
from  helper import navigation_helper
from  kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

Window.size=(300,500)

class HomeScreen(Screen):
    pass
class SettingsScreen(Screen):
    pass
class DataScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(HomeScreen(name='homeScreen'))

class Sulama(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.hue = "A700"
        screen = Screen()
        screen = Builder.load_string(navigation_helper)
        return screen

Sulama().run()