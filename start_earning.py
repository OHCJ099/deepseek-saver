"""
DeepSeek 省钱工具 - 一键启动赚钱系统
自动执行所有赚钱流程
"""

import os
import sys
import time
import subprocess
from datetime import datetime

def print_banner():
    print("=" * 70)
    print("   DeepSeek 省钱工具 - 自动赚钱系统")
    print("=" * 70)
    print(f"   启动时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    print()

def check_dependencies():
    """Check if required dependencies are installed"""
    print("[1/5] 检查依赖...")
    try:
        import playwright
        print("  ✓ Playwright 已安装")
    except ImportError:
        print("  ✗ Playwright 未安装，正在安装...")
        subprocess.run([sys.executable, "-m", "pip", "install", "playwright"], check=True)
        subprocess.run([sys.executable, "-m", "playwright", "install"], check=True)
        print("  ✓ Playwright 安装完成")

    try:
        import requests
        print("  ✓ Requests 已安装")
    except ImportError:
        print("  ✗ Requests 未安装，正在安装...")
        subprocess.run([sys.executable, "-m", "pip", "install", "requests"], check=True)
        print("  ✓ Requests 安装完成")

    print()

def generate_products():
    """Generate all product pages"""
    print("[2/5] 生成产品页面...")
    try:
        subprocess.run([sys.executable, "generate_products.py"], check=True)
        print("  ✓ 产品页面生成完成")
    except Exception as e:
        print(f"  ✗ 产品页面生成失败: {e}")
    print()

def open_store():
    """Open the store page"""
    print("[3/5] 打开产品商店...")
    store_path = os.path.join(os.path.dirname(__file__), "store.html")
    if os.path.exists(store_path):
        os.startfile(store_path)
        print("  ✓ 产品商店已打开")
    else:
        print("  ✗ 产品商店文件不存在")
    print()

def open_calculator():
    """Open the calculator page"""
    print("[4/5] 打开省钱计算器...")
    calc_url = "https://ohcj099.github.io/deepseek-saver/"
    print(f"  ✓ 计算器地址: {calc_url}")
    print()

def show_menu():
    """Show the main menu"""
    print("[5/5] 请选择要执行的操作：")
    print()
    print("  1. 自动发布到闲鱼")
    print("  2. 多平台推广（知乎/CSDN/掘金）")
    print("  3. 打开产品商店")
    print("  4. 打开省钱计算器")
    print("  5. 查看所有闲鱼文案")
    print("  6. 生成更多产品")
    print("  7. 退出")
    print()
    return input("请输入选项 (1-7): ").strip()

def run_闲鱼_post():
    """Run the 闲鱼 posting script"""
    print("\n正在启动闲鱼发布脚本...")
    try:
        subprocess.run([sys.executable, "auto_post.py"], check=True)
    except Exception as e:
        print(f"启动失败: {e}")

def run_promotion():
    """Run the multi-platform promotion script"""
    print("\n正在启动多平台推广脚本...")
    try:
        subprocess.run([sys.executable, "auto_promote.py"], check=True)
    except Exception as e:
        print(f"启动失败: {e}")

def show_listings():
    """Show all 闲鱼 listings"""
    print("\n可用的闲鱼文案：")
    print("-" * 50)

    products_dir = os.path.join(os.path.dirname(__file__), "products")
    if os.path.exists(products_dir):
        for file in os.listdir(products_dir):
            if file.endswith("_闲鱼.txt"):
                filepath = os.path.join(products_dir, file)
                print(f"\n📄 {file}")
                print("-" * 30)
                with open(filepath, 'r', encoding='utf-8') as f:
                    print(f.read()[:500] + "..." if len(f.read()) > 500 else f.read())
                print()

    # Also show the main listing
    main_listing = os.path.join(os.path.dirname(__file__), "闲鱼文案.md")
    if os.path.exists(main_listing):
        print("\n📄 主要闲鱼文案")
        print("-" * 30)
        with open(main_listing, 'r', encoding='utf-8') as f:
            print(f.read())

def main():
    print_banner()

    # Check dependencies
    check_dependencies()

    # Generate products
    generate_products()

    # Open store
    open_store()

    # Open calculator
    open_calculator()

    # Main loop
    while True:
        choice = show_menu()

        if choice == "1":
            run_闲鱼_post()
        elif choice == "2":
            run_promotion()
        elif choice == "3":
            open_store()
        elif choice == "4":
            open_calculator()
        elif choice == "5":
            show_listings()
        elif choice == "6":
            generate_products()
        elif choice == "7":
            print("\n感谢使用！祝你赚钱顺利！")
            break
        else:
            print("\n无效选项，请重新选择。")

        input("\n按 Enter 继续...")

if __name__ == "__main__":
    main()
