import os
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
