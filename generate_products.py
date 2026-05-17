"""
DeepSeek 省钱工具 - 产品生成器
自动生成多个可卖的工具/计算器
"""

import os
import json
from datetime import datetime

# 产品模板
PRODUCTS = {
    "deepseek_cost_calculator": {
        "name": "DeepSeek 费用计算器",
        "description": "计算 DeepSeek API 使用费用，对比不同工具的缓存效率",
        "price": "5-10元",
        "target": "DeepSeek 用户",
        "features": [
            "实时费用计算",
            "缓存命中率分析",
            "多场景预设",
            "优化建议"
        ]
    },
    "api_key_manager": {
        "name": "API Key 管理器",
        "description": "安全管理多个 AI API Key，自动轮换和负载均衡",
        "price": "10-20元",
        "target": "多 API 用户",
        "features": [
            "Key 加密存储",
            "自动轮换",
            "余额监控",
            "使用统计"
        ]
    },
    "ai_cost_optimizer": {
        "name": "AI 费用优化器",
        "description": "分析 AI API 使用模式，提供优化建议",
        "price": "15-30元",
        "target": "AI 重度用户",
        "features": [
            "使用模式分析",
            "费用预测",
            "优化建议",
            "节省报告"
        ]
    },
    "prompt_optimizer": {
        "name": "Prompt 优化器",
        "description": "优化 Prompt 减少 Token 使用，提高响应质量",
        "price": "10-20元",
        "target": "AI 开发者",
        "features": [
            "Prompt 精简",
            "Token 计数",
            "质量评估",
            "A/B 测试"
        ]
    },
    "ai_usage_monitor": {
        "name": "AI 使用监控",
        "description": "监控 AI API 使用情况，设置预算告警",
        "price": "10-15元",
        "target": "团队/企业",
        "features": [
            "实时监控",
            "预算告警",
            "使用报告",
            "团队管理"
        ]
    }
}

def generate_product_page(product_id, product_info):
    """Generate a single product page"""
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{product_info['name']}</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"PingFang SC","Microsoft YaHei",sans-serif;background:#0a0e17;color:#e2e8f0;line-height:1.6}}
.container{{max-width:800px;margin:0 auto;padding:20px}}
.hero{{text-align:center;padding:60px 0 40px}}
.hero h1{{font-size:2.2em;background:linear-gradient(135deg,#3b82f6,#10b981);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:12px}}
.hero p{{font-size:1.1em;color:#94a3b8}}
.card{{background:#111827;border:1px solid #1e293b;border-radius:16px;padding:32px;margin:24px 0}}
.card h2{{font-size:1.3em;margin-bottom:16px;color:#3b82f6}}
.features{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;margin:20px 0}}
.feature{{background:#0f172a;border-radius:12px;padding:16px}}
.feature h3{{font-size:1em;margin-bottom:8px;color:#10b981}}
.feature p{{font-size:.9em;color:#94a3b8}}
.price{{text-align:center;padding:40px 0}}
.price .amount{{font-size:3em;font-weight:700;color:#f59e0b}}
.price .period{{color:#94a3b8}}
.btn{{display:inline-block;padding:14px 32px;background:linear-gradient(135deg,#3b82f6,#6366f1);color:#fff;border:none;border-radius:10px;font-size:1.1em;font-weight:600;cursor:pointer;text-decoration:none;transition:all .2s}}
.btn:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(59,130,246,.3)}}
.cta{{text-align:center;padding:40px 0}}
.footer{{text-align:center;padding:40px 0;color:#94a3b8;font-size:.85em}}
</style>
</head>
<body>
<div class="container">
<div class="hero">
<h1>{product_info['name']}</h1>
<p>{product_info['description']}</p>
</div>

<div class="card">
<h2>功能特点</h2>
<div class="features">
"""
    for feature in product_info['features']:
        html += f"""<div class="feature">
<h3>✓ {feature}</h3>
<p>专业级实现，稳定可靠</p>
</div>
"""
    html += f"""</div>
</div>

<div class="card">
<h2>适合人群</h2>
<p style="font-size:1.1em">{product_info['target']}</p>
</div>

<div class="price">
<div class="amount">{product_info['price']}</div>
<div class="period">一次购买，永久使用</div>
</div>

<div class="cta">
<a href="#" class="btn">立即购买</a>
<p style="margin-top:16px;color:#94a3b8;font-size:.9em">支持微信/支付宝付款</p>
</div>

<div class="footer">
<p>生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
<p>Powered by DeepSeek 省钱工具生成器</p>
</div>
</div>
</body>
</html>"""
    return html

def generate_闲鱼_listing(product_id, product_info):
    """Generate 闲鱼 listing for a product"""
    return f"""标题：{product_info['name']} | 专业版 | 即买即用

价格：{product_info['price'].split('-')[0]}

描述：
【产品名称】{product_info['name']}

【产品描述】
{product_info['description']}

【核心功能】
{chr(10).join('- ' + f for f in product_info['features'])}

【适合人群】
{product_info['target']}

【购买方式】
拍下后联系卖家，发送接收邮箱，5分钟内发货。

【售后服务】
- 提供使用文档
- 7天内免费答疑
- 终身更新

【为什么值这个价】
- 专业开发，稳定可靠
- 节省大量开发时间
- 持续更新维护
- 省下的钱远超购买成本

在线体验：https://ohcj099.github.io/deepseek-saver/"""

def main():
    print("=" * 60)
    print("DeepSeek 省钱工具 - 产品生成器")
    print("=" * 60)

    # Create output directory
    output_dir = "C:/Users/Linxiaoning/Desktop/deepseek-saver/products"
    os.makedirs(output_dir, exist_ok=True)

    print(f"\n正在生成 {len(PRODUCTS)} 个产品...")

    for i, (product_id, product_info) in enumerate(PRODUCTS.items(), 1):
        print(f"\n[{i}/{len(PRODUCTS)}] 生成: {product_info['name']}")

        # Generate HTML page
        html = generate_product_page(product_id, product_info)
        html_path = os.path.join(output_dir, f"{product_id}.html")
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  ✓ HTML 页面: {html_path}")

        # Generate 闲鱼 listing
        listing = generate_闲鱼_listing(product_id, product_info)
        listing_path = os.path.join(output_dir, f"{product_id}_闲鱼.txt")
        with open(listing_path, 'w', encoding='utf-8') as f:
            f.write(listing)
        print(f"  ✓ 闲鱼文案: {listing_path}")

    # Generate index page
    print(f"\n正在生成产品目录...")
    index_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI 工具商店</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"PingFang SC","Microsoft YaHei",sans-serif;background:#0a0e17;color:#e2e8f0;line-height:1.6}
.container{max-width:1200px;margin:0 auto;padding:20px}
.hero{text-align:center;padding:60px 0 40px}
.hero h1{font-size:2.5em;background:linear-gradient(135deg,#3b82f6,#10b981);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:12px}
.hero p{font-size:1.2em;color:#94a3b8}
.products{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px;margin:40px 0}
.product{background:#111827;border:1px solid #1e293b;border-radius:16px;padding:24px;transition:all .2s}
.product:hover{border-color:#3b82f6;transform:translateY(-4px)}
.product h2{font-size:1.3em;margin-bottom:12px;color:#3b82f6}
.product p{color:#94a3b8;margin-bottom:16px}
.product .price{font-size:1.5em;font-weight:700;color:#f59e0b;margin-bottom:16px}
.product .btn{display:inline-block;padding:10px 24px;background:linear-gradient(135deg,#3b82f6,#6366f1);color:#fff;border:none;border-radius:8px;font-size:1em;font-weight:600;cursor:pointer;text-decoration:none;transition:all .2s}
.product .btn:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(59,130,246,.25)}
.footer{text-align:center;padding:40px 0;color:#94a3b8;font-size:.85em}
</style>
</head>
<body>
<div class="container">
<div class="hero">
<h1>AI 工具商店</h1>
<p>实用的 AI 开发工具，帮你省钱提效</p>
</div>

<div class="products">
"""
    for product_id, product_info in PRODUCTS.items():
        index_html += f"""<div class="product">
<h2>{product_info['name']}</h2>
<p>{product_info['description']}</p>
<div class="price">{product_info['price']}</div>
<a href="products/{product_id}.html" class="btn">了解详情</a>
</div>
"""
    index_html += """</div>

<div class="footer">
<p>所有工具均为一次购买，永久使用</p>
<p style="margin-top:8px">支持微信/支付宝付款</p>
</div>
</div>
</body>
</html>"""

    index_path = os.path.join(output_dir, "..", "store.html")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_html)
    print(f"  ✓ 产品目录: {index_path}")

    # Generate summary
    print(f"\n{'='*60}")
    print(f"产品生成完成！")
    print(f"{'='*60}")
    print(f"\n已生成 {len(PRODUCTS)} 个产品：")
    for product_id, product_info in PRODUCTS.items():
        print(f"  • {product_info['name']} ({product_info['price']})")
    print(f"\n文件位置: {output_dir}")
    print(f"产品目录: {index_path}")
    print(f"\n下一步：")
    print(f"  1. 打开 store.html 查看所有产品")
    print(f"  2. 将产品页面上传到 GitHub Pages")
    print(f"  3. 使用闲鱼文案在闲鱼发布")
    print(f"  4. 在社交媒体推广产品目录")

if __name__ == "__main__":
    main()
