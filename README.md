---
manager-apk介绍
---

## manager-apk安装和卸载apk的测试小工具，依赖于adb的python脚本;支持单个/批量

#### 使用环境:
- Python3.6
- 安装adb
- MacOS/Linux

#### 安装操作步骤

- 进入Python虚拟环境
```
pyenv activate py3.6.3
```

- 将要安装的apk包拷贝到apk目录下

- 直接调用执行installapk.py [...] 可选参数可给可不给，默认安装apk下所有包文件,可以指定apk文件安装
```
# 默认全部安装apk
python3 installapk.py

# 单个/多个安装apk
python3 installapk.py xxx.apk xxxx.apk
```

#### 卸载操作步骤

- 将要卸载的apk包拷贝到uninstallapk目录下

- 直接调用执行uninstallapk.py [...] 可选参数可给可不给，默认卸载uninstallapk目录下所有包文件，可以指定apk卸载
```
# 默认全部卸载apk
python3 uninstallapk.py

# 单个/多个卸载apk
python3 uninstallapk.py xxxx.apk
```


