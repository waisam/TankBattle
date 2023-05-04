from kivy.utils import platform


def run_with_mobile_device():
    """
    判断当前运行平台是不是移动端

    :Returns: 移动端返回`True`，否则返回`False`
    """
    if platform in {'android', 'ios'}:
        return True
    else:
        return False


mobile_runtime: bool = run_with_mobile_device()
