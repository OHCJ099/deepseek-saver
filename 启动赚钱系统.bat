@echo off
chcp 65001 >nul
title DeepSeek 省钱工具 - 自动赚钱系统

echo.
echo ========================================
echo   DeepSeek 省钱工具 - 自动赚钱系统
echo ========================================
echo.
echo 正在启动...
echo.

cd /d "%~dp0"
python start_earning.py

echo.
echo 系统已退出。
pause
