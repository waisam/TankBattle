## Buildozer

### Prerequisites

* Java Development Kit(JDK) 8 or higher

### 初始化buildozer环境

```shell
buildozer init
```

### 编译打包APK指南 

#### 配置 buildozer.spec

建议下载安装Android NDK 和 Android Command-Line Tools，
不然每次clean后都需要重新下载 1.5G 大小的文件

1. android.ndk_path
   * 路径为`$Android_SDK_ROOT/ndk/$ndkVersion`
2. android.sdk_path
   * $Android_SDK_ROOT/tools中的sdkmanager有问题，需要使用下方的路径设置
   * 实际是调用cmdline-tools的sdkmanager，路径为`$Android_SDK_ROOT/cmdline-tools/tools/sdkmanager`
3. android.ant_path
   * Apache Ant 90+M大小，开发者自行决定是否重新下载

#### 打包命令

```shell
buildozer android release deploy run
```

#### 清除临时文件

```shell
# 清除.buildozer目录
buildozer appclean
```

```shell
# 清除整个buildozer环境
buildozer distclean
```

```shell
# 清除Android的构建缓存
buildozer android clean
```