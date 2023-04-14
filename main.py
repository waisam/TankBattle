import os
if os.name == 'nt':
    # Windows系统设置pillow为image provider，避免窗口启动后闪退。
    os.environ['KIVY_IMAGE'] = 'pil'
from cn.tank.MainFrame import TankBattleApp

if __name__ == '__main__':
    TankBattleApp().run()
