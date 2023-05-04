from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from cn.tank.script import mobile_runtime
from cn.tank.widget.tank import Player, Enemy


class Arena(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.player1 = Player(source='media/image/player1_up.png')
        self.add_widget(widget=self.player1)

        if not mobile_runtime:
            # 非移动端，监听键盘事件
            self._keyboard = Window.request_keyboard(self.on_keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_key_down)
            self._keyboard.bind(on_key_up=self.on_key_up)
            self.pressed_keys = set()

        Clock.schedule_interval(self.p1_move_schedule, 0)

    def p1_move_schedule(self, duration):
        """P1移动功能

        :Param duration:
        """
        if not mobile_runtime:
            if len(self.pressed_keys) == 0:
                return

            fp_source = self.player1.source
            x, y = self.player1.pos
            width, height = self.player1.size
            if 'w' in self.pressed_keys and y < Window.height - height:
                fp_source = 'media/image/player1_up.png'
                y += 20
            elif 's' in self.pressed_keys and y > 0:
                fp_source = 'media/image/player1_down.png'
                y -= 20
            elif 'a' in self.pressed_keys and x > 0:
                fp_source = 'media/image/player1_left.png'
                x -= 20
            elif 'd' in self.pressed_keys and x < Window.width - width:
                fp_source = 'media/image/player1_right.png'
                x += 20

            self.player1.source = fp_source
            self.player1.pos = x, y

    def on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_key_down)
        self._keyboard.unbind(on_key_up=self.on_key_up)
        self._keyboard = None

    def on_touch_move(self, event):
        """
        触屏移动事件

        :Parameters event: 事件对象
        """
        print(event.id)
        print(event.button)
        print(event.device)
        print(event.opos)
        print(event.ppos)

    def on_touch_up(self, event):
        """
        触屏释放事件

        :Parameters event: 事件对象
        """
        print(event)

    def on_key_down(self, keyboard, keycode, keytext, modifiers):
        print(keytext)
        self.pressed_keys.add(keytext)

    def on_key_up(self, keyboard, keycode):
        self.pressed_keys.discard(keycode[1])
