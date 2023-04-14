from setuptools import setup, find_packages

setup(
    # python版本限制
    python_requires='>=3.7, <3.11',

    # 包名称
    name="cn.tank",
    # 包版本
    version='1.0',
    # 指定哪些目录下的文件被映射到哪个程序包
    packages=find_packages(),
    author='waisam, mole, rapist',
    # 简单描述
    description='A Game Named Tank Battle.',
    # 详细描述
    long_description='',
    # 适用的平台
    platforms=['nt', 'darwin'],

    # 项目主页
    url='',

    # 指明当前模块依赖哪些包，若环境中没有，则会从pypi中下载安装
    install_requires=[
        'kivy[base,media,gstreamer,angle,sdl2,glew]>=2.1.0',  # 只引入kivy的部分支持模块
        'Pillow>=9.5.0',
        'Cython>=0.29.34',
        'buildozer>=1.5.0'
    ],

    # 指明运行setup.py文件需要的包
    setup_requires=[]
)