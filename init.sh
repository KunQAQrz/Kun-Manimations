#!/bin/bash

OS=$(uname -s)
case $OS in
"Linux")
    PLATFORM="Linux"
    ;;
"Darwin")
    PLATFORM="MacOS"
    ;;
"MINGW"* | "CYGWIN"* | "MSYS"*)
    PLATFORM="Windows"
    ;;
*)
    PLATFORM="Unknown"
    ;;
esac

if ! command -v uv &>/dev/null; then
    echo -e "\033[33m检测到未安装uv，正在安装...\033[0m"

    if [ "Windows" = "$PLATFORM" ]; then
        powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    else
        curl -LsSf https://astral.sh/uv/install.sh | sh
    fi

    if [ $? -ne 0 ]; then
        echo -e "\033[31muv安装失败!\033[0m"
        exit 1
    fi
fi

uv python install
if [ $? -ne 0 ]; then
    echo -e "\033[31mpython安装失败!\033[0m"
    exit 2
fi

if [ -f "pyproject.toml" ]; then
    echo -e "\033[33m检测到已有 pyproject.toml，正在删除...\033[0m"
    rm pyproject.toml
fi

echo -e "\033[32m正在初始化项目...\033[0m"
uv init --author-from git --bare --no-description
if [ $? -ne 0 ]; then
    echo -e "\033[31m初始化失败!\033[0m"
    exit 3
fi

echo -e "\033[32m正在安装 Manim 依赖...\033[0m"
uv add manim
if [ $? -ne 0 ]; then
    echo -e "\033[31m依赖安装失败!\033[0m"
    exit 4
fi

echo -e "\033[32m正在验证 Manim 安装...\033[0m"
TEST_VALUE=""
for arg in "$@"; do
    case $arg in
    test=*)
        TEST_VALUE="${arg#test=}" # 提取等号后的内容
        ;;
    esac
done
if [ -n "$TEST_VALUE" ]; then
    echo "$TEST_VALUE" | manim checkhealth
    echo -e "\n"
else
    manim checkhealth
fi

if [ $? -ne 0 ]; then
    echo -e "\033[31mManim 安装验证失败!\033[0m"

    echo -e "\033[33m请确保 FFmpeg 已正确安装，并在 PATH 中。\033[0m"
    echo -e "下载地址：https://ffmpeg.org/download.html 。"

    echo -e "\033[33m请确保 LaTeX 已正确安装，并在 PATH 中。\033[0m"
    if [ "Windows" = "$PLATFORM" ]; then
        echo -e "下载地址：https://miktex.org/download 。"
    elif [ "Linux" = "$PLATFORM" ]; then
        echo -e "下载地址：https://www.tug.org/texlive 。"
    elif [ "MacOS" = "$PLATFORM" ]; then
        echo -e "下载地址：https://www.tug.org/mactex/mactex-download.html 。"
    fi
    exit 5
fi

echo -e "\033[32m项目初始化完成!\033[0m"
