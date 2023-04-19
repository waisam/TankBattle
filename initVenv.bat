@echo off
@rem 开启本地化设置，开启变量延迟扩展
setlocal enabledelayedexpansion
@rem 准备两个接收变量
set python_major_version=
set python_minor_version=
@rem 调用函数获取python的大版本和小版本
call :GetPythonVer
@rem 检查当前python版本是否适用
if %python_major_version% NEQ 3 (echo python的大版本必须是: 3. & exit /b 0)
if %python_minor_version% LSS 7 (echo python的小版本必须符合：7 ≤ 小版本 ≤ 10. & exit /b 0)
if %python_minor_version% GTR 10 (echo python的小版本必须符合：7 ≤ 小版本 ≤ 10. & exit /b 0)
@rem 初始化python虚拟环境
python -m venv venv
@rem 使用`call`命令激活虚拟环境，否则批处理程序会在执行完下一个语句后退出
call venv\Scripts\activate
@rem 安装必要的依赖包
python -m pip install --require-virtualenv -r requirements.txt
echo 项目初始化完成！
exit /b 0
@rem
:GetPythonVer
for /f "tokens=2" %%v in ('python -V 2^>^&1') do (
    echo 当前使用的python版本是：%%v
    set version=%%v
    for /f "tokens=1,2 delims=." %%j in ('echo !version!') do (
        set python_major_version=%%j
        set python_minor_version=%%k
    )
    exit /b 0
)