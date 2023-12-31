# diz

目前开源的大模型项目普遍来说都有如下问题：
1. 安装环境复杂，需要安装大量依赖包，而且依赖包版本之间有冲突，导致安装失败
2. 模型往往存放在 huggeface 上，下载速度慢，且不符合国情，使用 git lfs 也不方便

本项目重点解决上述 2 个问题，提供一个简单的模型下载和使用的框架，方便大家快速使用。
总结一句话来说就是：目标就是干出一个大模型的 homebrew。

## 安装

```bash
pip install diz
```

系统依赖：
1. tmux
2. git
3. git lfs

## 使用

### 使用 install 来安装模型
```bash
diz install ChatGLM2-6B --path /root/autodl-tmp/chatglm2
```
当前支持对的模型有：
- ChatGLM2-6B

`--path` 如果不填写，程序会提醒你输入，如果填写了，程序会自动创建目录

### 使用 setup 来使用自定义配置安装模型
```bash
diz setup
```
根据提示输入你要安装的目录和配置文件的 url 即可
配置文件写法可参考：[ChatGLM2-6B](https://gist.githubusercontent.com/mjason/a616dcb8f9fd09fb2c7fb18ff3bb6279/raw/bb530a7d4101edf8aa474883d1f54a6aef58bc44/chatglm2-6b.yml)

也可以一句话安装：
```bash
diz setup --path /root/autodl-tmp/chatglm2 --pkg https://gist.githubusercontent.com/mjason/a616dcb8f9fd09fb2c7fb18ff3bb6279/raw/bb530a7d4101edf8aa474883d1f54a6aef58bc44/chatglm2-6b.yml
```

### 使用 venv 来进入虚拟环境
```bash
diz venv
```
1. 检查当前目录是否存在 `venv` 目录存在就进入

### 虚拟环境

- `diz shell` 进入虚拟环境，如果使用 `diz shell --auto-venv` 进入的同时会执行 `diz venv` 进入虚拟环境
- `diz shell --mode o` 退出虚拟环境，环境进入后台
- `diz shell --mode k` 退出虚拟环境，环境进入后台，且 kill 掉原来的进程

你也可以使用 `Ctrl + b d` 来退出虚拟tmux环境，让任务在后台运行

## 路线图
- [x] 提供 install 命令，统一安装源
- [x] 提供 venv 指令，快速进入对应的虚拟环境
- [ ] 提供 generate 命令，根据生成本地模型调用代码