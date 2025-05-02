# Kun-Manimations

[manim](https://www.manim.community)（Mathematical Animation Engine）是由 [3Blue1Brown](https://space.bilibili.com/88461692) 创作者 Grant Sanderson 开发的数学动画引擎，主要用于创建精确的数学可视化视频。

该项目（Kun-Manimations）用于存放本人平时制作视频或文档时用到的 manim 动画代码，方便以后查看和使用，同时也可以作为学习 manim 的参考。

> main 分支为模板代码，其他分支为生成实际视频或文档的项目代码。

## 目录结构

```
Kun-Manimations/
├── init.sh       # 初始化项目脚本
├── README.md     # 项目说明
├── media/        # 存放视频、图片等生成的媒体文件
│   ├── ...
└── src/          # 存放代码
    ├── patterns/ # 存放图案代码
    │   ├── ...
    ├── helper.py # 存放辅助类或函数
    └── scenes.py # 场景代码，通过图案代码进行组合生成各种场景，而主场景（Main）则会将这些场景组合成一个总的场景。
```

## 准备

#### 安装 LaTeX：

Windows 平台下载：https://miktex.org/download 。

Linux 平台下载：https://www.tug.org/texlive 。

MacOS 平台下载：https://www.tug.org/mactex/mactex-download.html 。

#### 初始化项目：

```cmd
sh init.sh test=no
```

#### 初始化项目并预览测试：

```cmd
sh init.sh test=yes
```

> 在 Windows 平台上，可以使用 Git Bash 执行。

如果初始化项目失败，请参考 [manim 社区版安装](https://docs.manim.community/en/stable/installation.html) 进行环境配置。

## 运行

#### 生成低质量视频（可用于开发阶段预览，不过还是建议使用 VS Code 插件 Manim Sideview）：

```cmd
manim -pql --renderer=opengl src/scenes.py Main
```

#### 生成视频：

```cmd
manim -pqk --renderer=opengl src/scenes.py Main
```

#### 生成动图：

```cmd
manim -pqk -r "1920,1080" --fps=50 --format=gif src/scenes.py Main
```

#### 生成图片：

```cmd
manim -pqk -r "1920,1080" --format=png -s src/scenes.py Main
```

> 了解更多命令请阅读 [manim 社区版配置](https://docs.manim.community/en/stable/guides/configuration.html)

## 开发建议

如果使用 VS Code 进行开发，推荐安装以下插件：

- [Manim Sideview](https://marketplace.visualstudio.com/items?itemName=Rickaym.manim-sideview)

> 关于如何使用请阅读 [manim 社区版快速入门](https://docs.manim.community/en/stable/tutorials/quickstart.html)
