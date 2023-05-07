from abc import ABC, abstractmethod
from kivy.uix.image import Image
from typing import Tuple


class Tank(ABC, Image):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_stretch = True
        self.toward = None

    @abstractmethod
    def move(self):
        pass

    def __get_bullet_start_point(self) -> Tuple[float, float]:
        """利用坦克当前坐标点和坦克组件尺寸，计算坦克组件的中心坐标，
        再根据坦克当前朝向`toward`，在同方向上增加/减少坦克宽度/高
        度一半的距离，得到坦克子弹的起点坐标。

        1. 取得坦克中心坐标

        2. 取得坦克炮口坐标

        :Return: 发射子弹的坐标，即炮口坐标
        """
        return 0, 0

    def fire(self) -> None:
        """坦克射击功能

        1. 取得子弹发射坐标

        2. 绘制并添加子弹组件

        3. 让子弹飞起来
        """


class Player(Tank):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def move(self):
        """P1、P2坦克手动操作，需要监听设备的输入事件，将`arena`中的移动函数迁到此处
        """


class Enemy(Tank):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def move(self):
        """敌方坦克自动移动
        """
        pass
