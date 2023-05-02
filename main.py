import os
if os.name == 'nt':
    # Windows系统设置pillow为image provider，避免窗口启动后闪退。
    os.environ['KIVY_IMAGE'] = 'pil'
from kivy.config import Config
Config.setall('kivy', {
    'default_font': [
        # 解决无法显示中文字体的问题
        '仿宋_GB2312', os.path.join(os.getcwd(), 'data/fonts/仿宋_GB2312.ttf')],
})
Config.set('input', 'mouse', 'mouse,disable_multitouch')
from cn.tank.mainframe import TankBattleApp

if __name__ == '__main__':
    TankBattleApp().run()
