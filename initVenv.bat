@echo off
@rem �������ػ����ã����������ӳ���չ
setlocal enabledelayedexpansion
@rem ׼���������ձ���
set python_major_version=
set python_minor_version=
@rem ���ú�����ȡpython�Ĵ�汾��С�汾
call :GetPythonVer
@rem ��鵱ǰpython�汾�Ƿ�����
if %python_major_version% NEQ 3 (echo python�Ĵ�汾������: 3. & exit /b 0)
if %python_minor_version% LSS 7 (echo python��С�汾������ϣ�7 �� С�汾 �� 10. & exit /b 0)
if %python_minor_version% GTR 10 (echo python��С�汾������ϣ�7 �� С�汾 �� 10. & exit /b 0)
@rem ��ʼ��python���⻷��
python -m venv venv
@rem ʹ��`call`��������⻷��������������������ִ������һ�������˳�
call venv\Scripts\activate
@rem ��װ��Ҫ��������
python -m pip install --require-virtualenv -r requirements.txt
echo ��Ŀ��ʼ����ɣ�
exit /b 0
@rem
:GetPythonVer
for /f "tokens=2" %%v in ('python -V 2^>^&1') do (
    echo ��ǰʹ�õ�python�汾�ǣ�%%v
    set version=%%v
    for /f "tokens=1,2 delims=." %%j in ('echo !version!') do (
        set python_major_version=%%j
        set python_minor_version=%%k
    )
    exit /b 0
)