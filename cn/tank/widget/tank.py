from kivy.uix.image import Image


class Tank(Image):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_stretch = True


class Player(Tank):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Enemy(Tank):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
