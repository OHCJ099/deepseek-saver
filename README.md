# DeepSeek 省钱计算器

[![GitHub Pages](https://img.shields.io/badge/在线体验-计算器-blue)](https://ohcj099.github.io/deepseek-saver/)
[![Reasonix](https://img.shields.io/badge/Powered%20by-Reasonix-green)](https://github.com/esengine/reasonix)

一个直观的 DeepSeek API 费用计算器，展示 Reasonix 缓存优化的省钱效果。

## 在线体验

👉 **[点击这里打开计算器](https://ohcj099.github.io/deepseek-saver/)**

## 功能特点

- 🧮 实时计算 DeepSeek API 费用
- 📊 对比普通工具 vs Reasonix 的费用差异
- 🎯 支持多种使用场景预设（学生/独立开发者/团队/重度用户）
- 📈 详细的缓存命中率分析
- 💡 个性化的优化建议

## 为什么能省钱？

DeepSeek 的 API 定价中，**缓存命中的输入 Token 只收 10% 的费用**。

但大多数 AI 编程工具的缓存命中率不到 20%，而 Reasonix 通过「不可变前缀 + 追加日志」架构，将命中率提升到 **99%+**。

| 指标 | 普通工具 | Reasonix |
|------|----------|----------|
| 缓存命中率 | 15-20% | 99%+ |
| 输入费用 | ¥2/百万 | ¥0.2/百万 |
| 月费（典型场景）| ¥60 | ¥12 |

## 使用方法

### 在线计算器

直接打开 [index.html](index.html) 或访问 [GitHub Pages](https://ohcj099.github.io/deepseek-saver/)。

### 本地运行

```bash
# 克隆仓库
git clone https://github.com/OHCJ099/deepseek-saver.git

# 打开计算器
cd deepseek-saver
start index.html
```

## Reasonix 安装

```bash
# 安装 Reasonix
npm install -g reasonix

# 初始化配置
reasonix init

# 配置 DeepSeek API Key
reasonix config set provider.deepseek.api_key "your-api-key"
```

## 自动化工具

本项目包含自动化发布脚本：

```bash
# 自动发布到闲鱼
python auto_post.py

# 多平台推广（知乎/CSDN/掘金）
python auto_promote.py

# 一键启动（Windows）
run_all.bat
```

## 费用对比

以典型开发者使用场景为例（每天 50 轮对话，每轮 8000 输入 Token）：

| 项目 | 普通工具 | Reasonix |
|------|----------|----------|
| 输入 Token 缓存命中 | 15% | 99% |
| 输入费用（缓存命中）| ¥2.64 | ¥17.42 |
| 输入费用（缓存未命中）| ¥42.24 | ¥2.64 |
| 输出费用 | ¥17.60 | ¥17.60 |
| **月总费用** | **¥62.48** | **¥37.66** |
| **每月节省** | - | **¥24.82（40%）** |

## 相关资源

- [Reasonix GitHub](https://github.com/esengine/reasonix) - DeepSeek 专用 AI 编程助手
- [Reasonix npm](https://www.npmjs.com/package/reasonix) - npm 安装包
- [DeepSeek API](https://platform.deepseek.com/) - DeepSeek API 官网

## 赞赏支持

如果这个工具对你有帮助，欢迎请我喝杯咖啡 ☕

- [GitHub Sponsors](https://github.com/sponsors/OHCJ099)
- [爱发电](https://afdian.net/a/yourusername)

## 许可证

MIT License

---

**需要帮忙配置 Reasonix？** 联系我，10 块钱包搞定 ✌️
