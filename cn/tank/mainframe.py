import os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from cn.tank.widget.arena import Arena


class MainFrame(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cover_background = Image(source='media/image/cover.png', allow_stretch=True, keep_ratio=False)
        self.start_btn = Button(font_size=50, background_normal="media/image/startgame.png",
                                size_hint=(0.2, 0.1), pos_hint={'x': 0.80, 'y': 0.80})
        self.start_btn.bind(on_press=self.start_game)
        self.add_widget(self.cover_background)
        self.add_widget(self.start_btn)
        # 背景设置
        # with self.canvas.after:
        # Color(1, 1, 1, 0.5)
        # self.background = BorderImage(source='media/image/cover.png', pos=self.pos, size=self.size)
        # """炫技嫌疑，lambda可替换为常规函数"""
        # self.bind(pos=lambda x, w: self.background.__setattr__('pos', w),
        #           size=lambda y, size: self.background.__setattr__('size', size))

    def start_game(self, widget):
        self.remove_widget(self.start_btn)
        self.remove_widget(self.cover_background)
        self.add_widget(Arena())


class TankBattleApp(App):

    def get_application_config(self, defaultpath='%(datadir)s/%(appname)s.ini'):
        """
        重写获取配置文件路径的函数，覆盖父类的实现，自定义配置文件路径。
        默认路径为项目根目录下的`data`目录
        :param defaultpath: 丢弃此参数
        :return: 配置文件绝对路径
        """
        defaultpath = '%(datadir)s/%(appname)s.ini' % {'datadir': os.path.join(os.getcwd(), 'data'),
                                                       'appname': self.name}
        return super().get_application_config(defaultpath)

    def build(self):  # 返回一个组件
        root = MainFrame()
        return root

    def build_config(self, config):
        """
        初始化默认配置
        :param config: ConfigParser对象。与`self.config`是同一对象。
        """
        config.setdefaults('graphics', {
            'fullscreen': 1,
            'maxfps': 60,
            'show_cursor': 0,
            'rotation': 0
        })
        config.setdefaults('system', {
            'log_enable': 1,
            'log_level': 'info'
        })

    def build_settings(self, settings):  # default settings `kivy/data/settings_kivy.json`
        self.use_kivy_settings = False  # do not use the kivy default settings
        settings.add_json_panel('TankBattle', self.config, 'data/settings.json')

    def on_start(self):  # 应用启动时触发
        print("Welcome to Tank Battle World!")

    def on_stop(self):  # 关闭应用时触发
        print('Tank Battle Exit.')

    def on_pause(self):  # 暂停应用时触发
        pass

    def on_resume(self):  # 应用从暂停状态恢复时触发，但不保证能正确触发
        pass
