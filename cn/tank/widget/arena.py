from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from cn.tank.script import mobile_runtime
from cn.tank.widget.tank import Player, Enemy


class Arena(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.player1 = None
        self.player2 = None

        if not mobile_runtime:
            # 非移动端，监听键盘事件
            self._keyboard = Window.request_keyboard(self.on_keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_key_down)
            self._keyboard.bind(on_key_up=self.on_key_up)
            self.pressed_keys = set()

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
            if 'w' in self.pressed_keys:
                fp_source = 'media/image/player1_up.png'
                if y < Window.height - height:
                    y += 20
            elif 's' in self.pressed_keys:
                fp_source = 'media/image/player1_down.png'
                if y > 0:
                    y -= 20
            elif 'a' in self.pressed_keys:
                fp_source = 'media/image/player1_left.png'
                if x > 0:
                    x -= 20
            elif 'd' in self.pressed_keys:
                fp_source = 'media/image/player1_right.png'
                if x < Window.width - width:
                    x += 20

            self.player1.source = fp_source
            self.player1.pos = x, y

    def p2_move_schedule(self, duration):
        """P2移动功能

        :Param duration:
        """
        if not mobile_runtime:
            if len(self.pressed_keys) == 0:
                return

            sp_source = self.player2.source
            x, y = self.player2.pos
            width, height = self.player2.size
            if 'up' in self.pressed_keys:
                sp_source = 'media/image/player2_up.png'
                if y < Window.height - height:
                    y += 20
            elif 'down' in self.pressed_keys:
                sp_source = 'media/image/player2_down.png'
                if y > 0:
                    y -= 20
            elif 'left' in self.pressed_keys:
                sp_source = 'media/image/player2_left.png'
                if x > 0:
                    x -= 20
            elif 'right' in self.pressed_keys:
                sp_source = 'media/image/player2_right.png'
                if x < Window.width - width:
                    x += 20

            self.player2.source = sp_source
            self.player2.pos = x, y

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
        pass

    def on_key_down(self, keyboard, keycode, keytext, modifiers):
        if '1' == keycode[1] and self.player1 is None:
            self.player1 = Player(source='media/image/player1_up.png', pos=(Window.width * 0.35, 0))
            self.add_widget(self.player1)
            Clock.schedule_interval(self.p1_move_schedule, 0)
        elif '0' == keycode[1] and self.player2 is None:
            self.player2 = Player(source='media/image/player2_up.png', pos=(Window.width * 0.60, 0))
            self.add_widget(self.player2)
            Clock.schedule_interval(self.p2_move_schedule, 0)
        else:
            # 方向键上下左右事件中，得到的`keytext`为`None`，必须使用`keycode`才能获取到正确的值
            self.pressed_keys.add(keycode[1])

    def on_key_up(self, keyboard, keycode):
        if keycode[1] in ('0', '1'):
            # 避免遍历set
            return
        self.pressed_keys.discard(keycode[1])
