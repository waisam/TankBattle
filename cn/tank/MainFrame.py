from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from kivy.uix.widget import Widget


class MainFrame(GridLayout, Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 2
        self.button = Button(text='Start Game', font_size=80)
        self.button.set_top(30)
        self.button.set_right(40)
        self.button.bind(on_press=self.click_callback)
        self.cover = AsyncImage(source='media/image/cover.png')
        self.cover.add_widget(self.button)
        self.add_widget(self.cover)

    def click_callback(self, widget):
        self.remove_widget(widget)


class TankBattleApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Welcome to Tank Battle World!")

    def build(self):
        return MainFrame()
