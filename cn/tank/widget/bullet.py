from kivy.uix.image import Image


class Bullet(Image):
    """子弹类
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = [10, 10]  # 子弹大小

    """检测子弹是否已经超过边界，超过边界则将其移除
    """

    """实现子弹的飞行过程
    """
