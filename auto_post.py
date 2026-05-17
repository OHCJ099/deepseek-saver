"""
DeepSeek 省钱工具 - 全自动发布脚本
使用 Playwright 自动化闲鱼发布
"""

import time
import sys
from playwright.sync_api import sync_playwright

# 商品信息
TITLE = "DeepSeek API 省钱配置 | 缓存命中率99% | 月费直降80%"
PRICE = "10"
DESCRIPTION = """【服务内容】
帮你配置 Reasonix（DeepSeek 专用 AI 编程助手），通过缓存优化技术，将 DeepSeek API 月费降低 60-90%。

【效果保证】
- 缓存命中率从 15% → 99%+
- 输入费用降低约 90%
- 附赠专属省钱计算器，实时查看费用节省

【服务流程】
1. 远程协助安装 Reasonix（npm install -g reasonix）
2. 配置 DeepSeek API Key
3. 优化缓存策略，确保命中率 95%+
4. 交付省钱计算器，教你使用

【适合人群】
- 用 DeepSeek 写代码的开发者
- 学生课设/毕设用 AI 辅助编程
- 小团队使用 DeepSeek API

【为什么值这个价】
- Reasonix 是开源工具，但配置优化需要经验
- 不同使用场景需要不同的缓存策略
- 配置不当反而会增加费用
- 省下的钱远超服务费

在线计算器体验：https://ohcj099.github.io/deepseek-saver/"""

CALCULATOR_URL = "https://ohcj099.github.io/deepseek-saver/"

def main():
    print("=" * 60)
    print("DeepSeek 省钱工具 - 自动发布脚本")
    print("=" * 60)

    with sync_playwright() as p:
        # Launch browser (non-headless so user can log in)
        browser = p.chromium.launch(headless=False, args=[
            "--start-maximized",
            "--disable-blink-features=AutomationControlled"
        ])
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        # Step 1: Go to 闲鱼
        print("\n[1/5] 正在打开闲鱼...")
        page.goto("https://www.goofish.com/")
        time.sleep(3)

        # Step 2: Wait for user to log in
        print("\n[2/5] 请在浏览器中登录闲鱼账号")
        print("      登录完成后，按 Enter 继续...")
        input()

        # Step 3: Navigate to posting page
        print("\n[3/5] 正在进入发布页面...")
        try:
            # Try to find and click publish button
            page.goto("https://www.goofish.com/publish")
            time.sleep(3)
        except Exception as e:
            print(f"    直接导航失败，尝试其他方式: {e}")
            # Try alternative URL
            page.goto("https://www.goofish.com/")
            time.sleep(2)
            # Look for publish button
            try:
                publish_btn = page.locator("text=发布").first
                publish_btn.click()
                time.sleep(3)
            except:
                print("    请手动点击发布按钮，然后按 Enter 继续...")
                input()

        # Step 4: Fill in the listing
        print("\n[4/5] 正在填写商品信息...")
        time.sleep(2)

        # Try to fill title
        try:
            title_input = page.locator("input[placeholder*='标题'], input[placeholder*='宝贝'], textarea[placeholder*='标题']").first
            title_input.fill(TITLE)
            print("    ✓ 标题已填写")
        except Exception as e:
            print(f"    标题填写失败: {e}")
            print("    请手动填写标题，然后按 Enter 继续...")
            input()

        # Try to fill price
        try:
            price_input = page.locator("input[placeholder*='价格'], input[placeholder*='¥']").first
            price_input.fill(PRICE)
            print("    ✓ 价格已填写")
        except Exception as e:
            print(f"    价格填写失败: {e}")
            print("    请手动填写价格，然后按 Enter 继续...")
            input()

        # Try to fill description
        try:
            desc_input = page.locator("textarea[placeholder*='描述'], textarea[placeholder*='详细']").first
            desc_input.fill(DESCRIPTION)
            print("    ✓ 描述已填写")
        except Exception as e:
            print(f"    描述填写失败: {e}")
            print("    请手动填写描述，然后按 Enter 继续...")
            input()

        # Step 5: Take screenshot for verification
        print("\n[5/5] 正在截图确认...")
        page.screenshot(path="C:/Users/Linxiaoning/Desktop/deepseek-saver/listing_preview.png")
        print("    ✓ 截图已保存到 listing_preview.png")

        # Ask user to verify and submit
        print("\n" + "=" * 60)
        print("商品信息已填写完成！")
        print("请检查浏览器中的信息是否正确。")
        print("确认无误后，按 Enter 自动提交...")
        input()

        # Try to submit
        try:
            submit_btn = page.locator("button:has-text('发布'), button:has-text('提交'), button:has-text('确认')").first
            submit_btn.click()
            print("\n✓ 商品已发布！")
            time.sleep(3)
        except Exception as e:
            print(f"\n自动提交失败: {e}")
            print("请手动点击发布按钮。")

        # Take final screenshot
        page.screenshot(path="C:/Users/Linxiaoning/Desktop/deepseek-saver/listing_result.png")
        print("最终截图已保存到 listing_result.png")

        browser.close()

    print("\n" + "=" * 60)
    print("发布流程完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()
