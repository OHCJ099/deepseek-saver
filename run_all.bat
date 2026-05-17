@echo off
chcp 65001 >nul
echo ========================================
echo   DeepSeek 省钱工具 - 自动赚钱系统
echo ========================================
echo.
echo 可用功能：
echo.
echo   1. 发布到闲鱼（自动填写商品信息）
echo   2. 多平台推广（知乎/CSDN/掘金）
echo   3. 打开在线计算器
echo   4. 查看已生成的文案
echo   5. 退出
echo.
echo ========================================
echo.

set /p choice=请选择功能 (1-5):

if "%choice%"=="1" (
    echo.
    echo 正在启动闲鱼发布脚本...
    python "%~dp0auto_post.py"
) else if "%choice%"=="2" (
    echo.
    echo 正在启动多平台推广脚本...
    python "%~dp0auto_promote.py"
) else if "%choice%"=="3" (
    echo.
    echo 正在打开在线计算器...
    start https://ohcj099.github.io/deepseek-saver/
) else if "%choice%"=="4" (
    echo.
    echo 已生成的文案文件：
    echo.
    dir /b "%~dp0*.md"
    echo.
    echo 文件位置: %~dp0
    pause
) else if "%choice%"=="5" (
    exit
) else (
    echo 无效选择，请重新运行。
    pause
)
