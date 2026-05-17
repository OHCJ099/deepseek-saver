"""
DeepSeek 省钱工具 - 全自动推广脚本
自动在多个平台发布推广内容
"""

import time
import json
from playwright.sync_api import sync_playwright

PLATFORMS = {
    "知乎": {
        "url": "https://www.zhihu.com/",
        "title": "如何大幅降低 DeepSeek API 费用？",
        "content": """# 如何大幅降低 DeepSeek API 费用？

最近发现一个很实用的工具 **Reasonix**，专门针对 DeepSeek API 做了缓存优化，可以把 API 费用降低 60-90%。

## 核心原理

DeepSeek 的 API 定价中，**缓存命中的输入 Token 只收 10% 的费用**。但大多数 AI 编程工具（包括很多知名工具）的缓存命中率不到 20%。

Reasonix 通过「不可变前缀 + 追加日志 + 临时区」的三支柱架构，将缓存命中率提升到 **99%+**。

## 实际效果

我做了一个在线计算器，可以直观看到省多少钱：

👉 **在线体验**：https://ohcj099.github.io/deepseek-saver/

以典型开发者使用场景为例：
- 普通工具月费：¥60
- Reasonix 月费：¥12
- **每月节省：¥48（80%）**

## 如何使用

```bash
npm install -g reasonix
reasonix init
```

配置好 DeepSeek API Key 就可以了。

## 为什么值得用？

1. **省钱**：最直接的好处，缓存命中率从 15% → 99%
2. **省心**：自动管理上下文，不用担心 Token 浪费
3. **开源免费**：MIT 协议，完全免费使用

如果你也想优化 DeepSeek 费用，可以试试这个工具。
需要帮忙配置的可以联系我，10 块钱包搞定 ✌️"""
    },
    "CSDN": {
        "url": "https://editor.csdn.net/",
        "title": "DeepSeek API 费用优化实战：用 Reasonix 实现 99% 缓存命中率",
        "content": """# DeepSeek API 费用优化实战：用 Reasonix 实现 99% 缓存命中率

## 背景

在使用 DeepSeek API 进行 AI 编程时，费用是一个重要考虑因素。DeepSeek 的定价策略中，**缓存命中的输入 Token 只收取 10% 的费用**，这是一个巨大的优化空间。

然而，大多数 AI 编程工具的缓存命中率通常只有 15-20%，这意味着 80% 以上的输入 Token 都在按原价计费。

## 解决方案：Reasonix

Reasonix 是一个专为 DeepSeek 设计的终端 AI 编程助手，其核心创新在于**缓存优先架构**。

### 三支柱架构

1. **不可变前缀**：系统提示和初始上下文保持字节级稳定
2. **追加日志**：对话历史只追加不修改，保持前缀一致性
3. **临时区**：可变数据（如工具调用结果）隔离处理

### 实际效果

通过这种架构，Reasonix 实现了：
- 缓存命中率：**99%+**（vs 普通工具的 15-20%）
- 输入费用降低：**约 90%**
- 总费用降低：**60-80%**

## 动手实践

### 安装

```bash
npm install -g reasonix
```

### 初始化

```bash
reasonix init
```

### 配置

在 `~/.reasonix/config.yaml` 中配置：

```yaml
providers:
  deepseek:
    api_key: "your-api-key"
    model: "deepseek-chat"
cache:
  strategy: "immutable-prefix"
  auto_compact: true
```

## 在线计算器

我做了一个在线计算器，可以直观看到你能省多少钱：

👉 **DeepSeek 省钱计算器**：https://ohcj099.github.io/deepseek-saver/

## 总结

通过 Reasonix 的缓存优化架构，DeepSeek API 的费用可以大幅降低。对于重度用户来说，每月可以节省几十甚至上百元。

如果你也想优化 DeepSeek 费用，建议试试 Reasonix。需要帮忙配置的可以联系我。

---
**相关资源**：
- Reasonix GitHub：https://github.com/esengine/reasonix
- 在线计算器：https://ohcj099.github.io/deepseek-saver/"""
    },
    "掘金": {
        "url": "https://juejin.cn/",
        "title": "DeepSeek API 省钱指南：Reasonix 缓存优化实战",
        "content": """# DeepSeek API 省钱指南：Reasonix 缓存优化实战

## 前言

大家好，今天分享一个实用的 DeepSeek API 费用优化方案。

最近在使用 DeepSeek 进行 AI 编程时，发现 API 费用比预期高很多。经过调研，发现大多数 AI 编程工具的缓存命中率都很低，导致大量 Token 按原价计费。

## 问题分析

DeepSeek 的 API 定价：
- 输入 Token（缓存未命中）：¥2/百万
- 输入 Token（缓存命中）：¥0.2/百万（**10% 折扣**）
- 输出 Token：¥8/百万

关键点：**缓存命中的输入 Token 只收 10% 的费用**。

但问题在于，大多数工具每轮对话都会重新组织上下文（加时间戳、重排序、注入系统提示），导致前缀不一致，缓存命中率通常低于 20%。

## 解决方案：Reasonix

Reasonix 是一个专为 DeepSeek 设计的终端 AI 编程助手，其核心创新在于**缓存优先架构**。

### 架构设计

```
┌─────────────────────────────────────┐
│           不可变前缀                 │
│    (系统提示 + 初始上下文)           │
├─────────────────────────────────────┤
│           追加日志                   │
│    (对话历史，只追加不修改)          │
├─────────────────────────────────────┤
│           临时区                     │
│    (可变数据，隔离处理)              │
└─────────────────────────────────────┘
```

### 核心优势

1. **字节级前缀稳定**：跨轮次保持前缀一致，最大化缓存命中
2. **自动压缩**：当上下文过大时，自动压缩旧的工具调用结果
3. **Flash-first 策略**：简单任务用低成本模型，复杂任务才升级

### 实际效果

通过 Reasonix 优化后：
- 缓存命中率：**99%+**
- 输入费用降低：**约 90%**
- 总费用降低：**60-80%**

## 动手实践

### 安装配置

```bash
# 安装
npm install -g reasonix

# 初始化
reasonix init

# 配置 API Key
reasonix config set provider.deepseek.api_key "your-key"
```

### 使用示例

```bash
# 启动 Reasonix
reasonix

# 查看缓存统计
reasonix cache stats
```

## 在线计算器

为了方便大家直观看到省多少钱，我做了一个在线计算器：

👉 **DeepSeek 省钱计算器**：https://ohcj099.github.io/deepseek-saver/

支持：
- 自定义使用场景（学生/独立开发者/团队/重度用户）
- 实时计算费用对比
- 详细的缓存命中率分析
- 优化建议

## 总结

通过 Reasonix 的缓存优化架构，DeepSeek API 的费用可以大幅降低。对于重度用户来说，每月可以节省几十甚至上百元。

如果你也想优化 DeepSeek 费用，建议试试 Reasonix。需要帮忙配置的可以联系我，10 块钱包搞定 ✌️

---
**相关资源**：
- Reasonix GitHub：https://github.com/esengine/reasonix
- npm 包：https://www.npmjs.com/package/reasonix
- 在线计算器：https://ohcj099.github.io/deepseek-saver/"""
    }
}

def post_to_platform(platform_name, platform_info, browser_context):
    """Auto-post to a specific platform"""
    print(f"\n{'='*60}")
    print(f"正在发布到: {platform_name}")
    print(f"{'='*60}")

    page = browser_context.new_page()

    try:
        # Navigate to platform
        print(f"  [1/4] 打开 {platform_name}...")
        page.goto(platform_info["url"], timeout=30000)
        time.sleep(3)

        # Wait for user to log in
        print(f"  [2/4] 请在浏览器中登录 {platform_name} 账号")
        print(f"        登录完成后，按 Enter 继续...")
        input()

        # Try to find and click publish/create button
        print(f"  [3/4] 正在寻找发布入口...")
        time.sleep(2)

        # Try common publish button selectors
        publish_selectors = [
            "text=写文章",
            "text=发布",
            "text=创作",
            "text=写回答",
            "text=发帖",
            "[class*='write']",
            "[class*='publish']",
            "[class*='create']"
        ]

        for selector in publish_selectors:
            try:
                btn = page.locator(selector).first
                if btn.is_visible():
                    btn.click()
                    print(f"    ✓ 找到发布入口: {selector}")
                    time.sleep(3)
                    break
            except:
                continue

        # Try to fill title
        print(f"  [4/4] 正在填写内容...")
        try:
            title_selectors = [
                "input[placeholder*='标题']",
                "textarea[placeholder*='标题']",
                "[class*='title'] input",
                "[class*='title'] textarea"
            ]
            for selector in title_selectors:
                try:
                    title_input = page.locator(selector).first
                    if title_input.is_visible():
                        title_input.fill(platform_info["title"])
                        print(f"    ✓ 标题已填写")
                        break
                except:
                    continue
        except Exception as e:
            print(f"    标题填写失败: {e}")

        # Try to fill content
        try:
            content_selectors = [
                "textarea[placeholder*='内容']",
                "textarea[placeholder*='正文']",
                "[class*='content'] textarea",
                "[class*='editor'] textarea",
                ".CodeMirror",
                "[contenteditable='true']"
            ]
            for selector in content_selectors:
                try:
                    content_input = page.locator(selector).first
                    if content_input.is_visible():
                        content_input.fill(platform_info["content"])
                        print(f"    ✓ 内容已填写")
                        break
                except:
                    continue
        except Exception as e:
            print(f"    内容填写失败: {e}")

        # Take screenshot
        page.screenshot(path=f"C:/Users/Linxiaoning/Desktop/deepseek-saver/{platform_name}_preview.png")
        print(f"    ✓ 截图已保存到 {platform_name}_preview.png")

        # Ask user to verify and submit
        print(f"\n请检查 {platform_name} 中的内容是否正确。")
        print(f"确认无误后，按 Enter 提交...")
        input()

        # Try to submit
        try:
            submit_selectors = [
                "button:has-text('发布')",
                "button:has-text('提交')",
                "button:has-text('确认')",
                "button:has-text('发表')",
                "[class*='submit']",
                "[class*='publish']"
            ]
            for selector in submit_selectors:
                try:
                    submit_btn = page.locator(selector).first
                    if submit_btn.is_visible():
                        submit_btn.click()
                        print(f"    ✓ 已点击提交按钮")
                        time.sleep(3)
                        break
                except:
                    continue
        except Exception as e:
            print(f"    自动提交失败: {e}")
            print(f"    请手动点击发布按钮。")

        # Take final screenshot
        page.screenshot(path=f"C:/Users/Linxiaoning/Desktop/deepseek-saver/{platform_name}_result.png")
        print(f"    ✓ 最终截图已保存到 {platform_name}_result.png")

    except Exception as e:
        print(f"  发布到 {platform_name} 失败: {e}")
    finally:
        page.close()

def main():
    print("=" * 60)
    print("DeepSeek 省钱工具 - 全自动推广脚本")
    print("=" * 60)
    print("\n本脚本将自动在以下平台发布推广内容：")
    for i, name in enumerate(PLATFORMS.keys(), 1):
        print(f"  {i}. {name}")

    print("\n请选择要发布的平台（输入数字，多个用逗号分隔，0=全部）：")
    choice = input().strip()

    if choice == "0":
        selected = list(PLATFORMS.keys())
    else:
        indices = [int(x.strip()) - 1 for x in choice.split(",")]
        selected = [list(PLATFORMS.keys())[i] for i in indices if 0 <= i < len(PLATFORMS)]

    print(f"\n将发布到: {', '.join(selected)}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=[
            "--start-maximized",
            "--disable-blink-features=AutomationControlled"
        ])
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        )

        for platform_name in selected:
            if platform_name in PLATFORMS:
                post_to_platform(platform_name, PLATFORMS[platform_name], context)

        browser.close()

    print("\n" + "=" * 60)
    print("推广发布完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()
