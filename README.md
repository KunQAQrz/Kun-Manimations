# Kun-Manimations

[manim](https://www.manim.community)（Mathematical Animation Engine）是由 [3Blue1Brown](https://space.bilibili.com/88461692) 创作者 Grant Sanderson 开发的数学动画引擎，主要用于创建精确的数学可视化视频。

该项目（Kun-Manimations）用于存放本人平时制作视频或文档时用到的 manim 动画代码，方便以后查看和使用，同时也可以作为学习 manim 的参考。

> main 分支为模板代码，其他分支为生成实际视频或文档的项目代码。

## 目录结构

```
Kun-Manimations/
├── README.md     # 项目说明
├── init.sh       # 初始化项目脚本
├── manim.cfg     # 项目配置，可以配置默认背景色、帧率、分辨率等属性
├── media/        # 存放视频、图片等生成的媒体文件
│   ├── ...
└── src/          # 存放代码
    ├── patterns/ # 存放图案代码
    │   ├── ...
    ├── helper.py # 存放辅助类或函数
    └── scenes.py # 场景代码，通过图案代码进行组合生成各种场景，而主场景（Main）则会将这些场景组合成一个总的场景。
```

## 准备

#### 安装 FFmpeg：

下载地址：https://ffmpeg.org/download.html 。

> 注意：需要将 FFmpeg 加入到环境变量中。

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

如果还有问题，请参考 [manim 社区版安装](https://docs.manim.community/en/stable/installation.html) 进行环境配置。

## 运行

#### 场景快速预览（可用于开发阶段）：

```cmd
manim -pql --renderer=opengl src/scenes.py Main
```

> 如果使用的是 VS Code 编辑器，由于已经配置了 launch，可以按 F5 执行以上命令进行预览。

#### 生成视频并预览：

```cmd
manim -p --write_to_movie --renderer=opengl --format=mp4 src/scenes.py Main
```

#### 生成动图并预览：

```cmd
manim -p --write_to_movie --renderer=opengl --format=gif --fps=50 src/scenes.py Main
```

#### 生成最后一帧的图片并预览：

```cmd
manim -p --write_to_movie --renderer=opengl --format=png -s src/scenes.py Main
```

> 注意：`Main` 可以更改为其他场景名称，例如：`MyRotations`。

> 想了解更多命令请阅读 [manim 社区版配置](https://docs.manim.community/en/stable/guides/configuration.html)

## 开发建议

如果使用 VS Code 进行开发，推荐安装以下插件：

- [Manim Sideview](https://marketplace.visualstudio.com/items?itemName=Rickaym.manim-sideview)
  - 可以按 `F1` 打开命令面板，输入 `Manim: Open Mobject Gallery` 打开侧视图，方便查看和生成图案。
  - 可以按右上角菜单 `Manim: Runs a Sideview` 打开侧视图，方便预览场景。(不过现阶段该功能只能生成 1080P 60 帧的 mp4 文件后才能预览，速度远不如`场景快速预览`的命令快)

> 关于如何使用请阅读 [manim 社区版快速入门](https://docs.manim.community/en/stable/tutorials/quickstart.html)
