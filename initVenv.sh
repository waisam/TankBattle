#!/bin/bash

# 推断兼容的Python版本
deduceCompatiblePython() {

  local Python_Version
  # 管道`|`只传递标准输出的内容，因此使用`2>&1`
  # 将标准错误(文件描述符`2`)重定向到标准输出(文件描述符`1`)
  # 将标准错误和标准输出都传递给下一个命令
  # awk从标准输出的第二列`$2`获取版本号
  # 再以.作为分割，取前2部分拼接，组成格式如`3.10`的字符串
  Python_Version=$(python3 --version 2>&1 | awk '{print $2}' | awk -F. '{print $1"."$2}')
  echo "current python environment is $Python_Version" >&2

  local notFound=true;
  while $notFound; do
    echo "Version $Python_Version trying to compatible." >&2
    if [[ $Python_Version =~ ^3\.([7-9]|10)\.* ]]; then # 如果不是3.7.x到3.10.x的版本
      echo "Compatible version $Python_Version get!" >&2
      notFound=false
      break
    fi
    if [[ $Python_Version =~ ^3.7.* ]]; then
      echo "last match, but not found." >&2
      exit 0
    fi
    echo "Python version is incompatible, must between 3.7.x and 3.10.x." >&2
    Python_Version="$(echo "$Python_Version" | awk -F. '{print $1"."$2-1}')"
  done

  echo "python$Python_Version"
}
pycmd=$(deduceCompatiblePython)
$pycmd -m venv venv # 创建指定python版本的名为venv的虚拟环境
source venv/bin/activate # 激活虚拟环境
python -m pip install --require-virtualenv -r requirements.txt
#python -m pip install --require-virtualenv . # 使用当前目录的setup.py执行pip命令
