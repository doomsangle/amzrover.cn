# 亚马逊运营知识库（amzrover.cn）

> 从入门到精通，一站式学习亚马逊运营核心概念

## 项目简介

亚马逊卖家运营知识导航网站，涵盖认证合规、广告投放、站内运营、物流配送、数据分析等全流程。纯静态 HTML 站点，无需构建工具，可直接部署。

## 核心特性

- **中英双语**：完整镜像的 `en/` 英文目录，支持语言切换器一键切换
- **SEO 优化**：完整的 Meta 标签、Open Graph、Twitter Card、JSON-LD 结构化数据、robots.txt、sitemap.xml（含 hreflang 语言标记）
- **鱼骨图可视化**：CSS/SVG 纯手绘，通过 iframe 嵌入首页，移动端自动切换为列表布局
- **响应式设计**：通过 `@media` 查询适配移动端和桌面端
- **知识交叉引用**：各页面通过 FAQ 标签（蓝色）和术语标签（紫色）互相关联
- **成本计算器**：集成佣金计算器、FBA费用计算器、利润计算器等实时计算工具
- **评论管理专题**：详细说明评论管理策略、评分对销量的影响及合规获取评价方法

## 项目架构

```
amzrover.cn/
├── index.html                  # 首页导航（鱼骨图总览 + 运营流程时间线 + 进阶知识网格）
├── fishbone.html               # 鱼骨图可视化（SVG手绘，通过 iframe 嵌入首页）
├── compliance.html             # 认证与合规专项
├── privacy-policy.html         # 隐私政策页面
├── robots.txt                  # 搜索引擎爬取规则（含恶意爬虫限制）
├── sitemap.xml                 # 站点地图（含 hreflang 语言标记，共 140+ URL）
├── ads.txt                     # Authorized Digital Sellers 文件
├── nginx.conf                  # Nginx 部署配置文件（含 HTTPS 配置）
│
├── 01-account-registration.html ~ 09-settlement.html   # 运营流程（入门 9 步）
├── 10-data-analysis.html ~ 23-cost-calculator.html     # 进阶知识（14 个主题）
│
├── faq/                        # FAQ 问答（20 个主题分类）
│   ├── faq-index.html
│   ├── faq-registration.html
│   ├── faq-account.html
│   ├── faq-brand.html
│   ├── faq-ads.html
│   ├── faq-optimization.html
│   ├── faq-fba.html
│   ├── faq-shipping.html
│   ├── faq-listing.html
│   ├── faq-product-research.html
│   ├── faq-performance.html
│   ├── faq-risk.html
│   ├── faq-settlement.html
│   ├── faq-finance.html
│   ├── faq-data.html
│   ├── faq-tools.html
│   ├── faq-ip.html
│   ├── faq-compliance.html
│   ├── faq-policy.html
│   ├── faq-multi-platform.html
│   └── faq-tiktok.html
│
├── terms/                      # 名词术语详解（24 个核心词条）
│   ├── terms-index.html
│   ├── acos.html, roas.html, cpc.html, ctr.html
│   ├── fba.html, fbm.html, kyc.html
│   ├── conversion-rate.html
│   ├── sponsored-products.html, sponsored-brands.html, sponsored-display.html
│   ├── exact-match.html, phrase-match.html, broad-match.html
│   ├── negative-keywords.html, dynamic-bidding.html
│   ├── head-haul.html, professional-seller.html
│   └── baokuan.html, honghai.html, fenghao.html, guanlian.html, qiliang.html, poa.html
│
├── assets/                     # 样式文件
│   ├── style.css               # 通用样式（612 行）
│   └── term-style.css          # 术语页专用样式（325 行）
│
├── en/                         # 英文镜像目录（完整复制品）
│   ├── index.html, fishbone.html, compliance.html
│   ├── privacy-policy.html
│   ├── 01-account-registration.html ~ 23-cost-calculator.html
│   ├── faq/                    # 20 个英文 FAQ 页面
│   ├── terms/                  # 24 个英文术语页面
│   └── assets/                 # 英文样式文件
│
└── translate-*.py              # Python 翻译脚本工具（7 个）
    ├── translate-all.py        # 批量翻译所有英文页面
    └── ...                     # 其他翻译辅助脚本
```

## 内容模块

### 运营流程（入门 9 步）

| 序号 | 主题 | 文件 |
|------|------|------|
| 1 | 亚马逊店铺注册 | `01-account-registration.html` |
| 2 | 注册万里汇 & 绑定银行信息 | `02-worldfirst.html` |
| 3 | 上传 Listing 产品 | `03-listing-upload.html` |
| 4 | 注册绑定品牌 | `04-brand-registry.html` |
| 5 | FBA 发货亚马逊仓库 | `05-fba-shipping.html` |
| 6 | 亚马逊仓库物流 | `06-logistics.html` |
| 7 | 亚马逊广告 | `07-advertising.html` |
| 8 | 亚马逊系统售后 | `08-after-sales.html` |
| 9 | 亚马逊账号回款 | `09-settlement.html` |

### 进阶知识（14 个主题）

| 主题 | 文件 |
|------|------|
| 数据分析 | `10-data-analysis.html` |
| 评论管理 | `10-review-management.html` |
| 产品调研 | `11-product-research.html` |
| 库存管理 | `12-inventory-management.html` |
| 账号风险 | `13-account-risk.html` |
| 广告策略 | `14-ads-strategy.html` |
| 盈利模型 | `15-profit-model.html` |
| 产品生命周期 | `16-product-lifecycle.html` |
| 运营决策 | `17-operational-decision.html` |
| 官方文档中心 | `18-official-docs-hub.html` |
| 账号绩效风险 | `19-account-performance-risk.html` |
| 行业黑话 | `20-industry-slang.html` |
| 高级运营 | `21-advanced-operations.html` |
| 风险策略权衡 | `22-risk-strategy-tradeoff.html` |
| 成本计算器 | `23-cost-calculator.html` |

## 技术栈

- **纯静态站点**：HTML + CSS，无 JS 框架、无构建工具
- **响应式设计**：通过 `@media` 查询适配移动端
- **设计风格**：渐变背景、圆角卡片、hover 动效
- **鱼骨图**：CSS/SVG 纯手绘，通过 iframe 嵌入首页，移动端自动降级为列表
- **国际化**：`en/` 目录镜像结构，支持 hreflang 语言标记
- **SEO**：完整的 robots.txt、sitemap.xml、Meta 标签、JSON-LD 结构化数据
- **实时计算**：JavaScript 实现的成本计算器，支持佣金、FBA费用、利润等实时计算

## 页面统计

| 类别 | 数量 |
|------|------|
| 中文 HTML 页面 | 72 个 |
| 英文 HTML 页面 | 72 个 |
| **HTML 总页面** | **144 个** |
| 运营流程（入门） | 9 个 |
| 进阶知识主题 | 14 个 |
| FAQ 页面（含索引） | 21 个 |
| FAQ 主题分类 | 20 个 |
| 术语页面（含索引） | 25 个 |
| 术语词条 | 24 个 |
| CSS 文件 | 4 个（2 个中文 + 2 个英文） |
| Python 翻译脚本 | 8 个 |

## SEO 基础设施

- **robots.txt**：配置爬取规则和 sitemap 位置，支持语言版本声明，包含恶意爬虫限制
- **sitemap.xml**：包含全部 144+ URL，每个 URL 都有 `xhtml:link rel="alternate"` hreflang 标记
- **Meta 标签**：完整的 title、description、keywords、robots、canonical
- **Open Graph**：支持社交分享预览（og:type、og:url、og:title、og:description）
- **Twitter Card**：支持 Twitter 分享（twitter:card、twitter:title、twitter:description）
- **JSON-LD**：结构化数据标记，提升搜索展示效果
- **GEO 标签**：geo.region、geo.placename、language、distribution
- **ads.txt**：Authorized Digital Sellers 文件，防止广告欺诈

## 部署指南

### 本地开发

```bash
# 启动本地开发服务器
node server.js

# 访问 http://localhost:8080/
```

### Nginx 部署

项目包含完整的 Nginx 配置文件 `nginx.conf`，支持：

- HTTP → HTTPS 自动重定向
- SSL/TLS 证书配置（Let's Encrypt）
- HTTP/2 协议支持
- Gzip 压缩优化
- 静态文件缓存配置
- 安全头设置（HSTS、X-Frame-Options、X-XSS-Protection）

### 服务器端配置

```bash
# 上传文件到服务器
scp -r * root@your-server-ip:/var/www/html/amzrover.cn/

# 设置权限（CentOS/RHEL）
chown -R nginx:nginx /var/www/html/amzrover.cn
chmod -R 755 /var/www/html/amzrover.cn

# 申请 SSL 证书
certbot --nginx -d amzrover.cn -d www.amzrover.cn

# 测试配置
nginx -t

# 重启 Nginx
systemctl reload nginx
```

## 翻译工具链

项目包含 Python 翻译脚本，用于中英文内容同步：

```bash
# 批量翻译所有英文页面
python translate-all.py
```

翻译脚本通过字典映射方式进行中文到英文的替换，支持按长度排序避免部分匹配问题。

## 参与贡献

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request

## 许可证

MIT License
