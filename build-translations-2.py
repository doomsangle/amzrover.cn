"""
Comprehensive translation of all remaining Chinese in en/ HTML files.
Uses a large dictionary + pattern-based replacements.
"""
import re, os, json

base = r'd:\网站建设\网址导航\amzrover.cn\en'

def build_dict():
    D = {}
    # ===== SECTION 1: Bullet points and list items =====
    D["- 中部Advertising位"] = "- Middle ad positions"
    D["- 为不同受众创建不同Campaign"] = "- Create different Campaigns for different audiences"
    D["- 主图：产品放在白色背景上，但角度不好，细节不清晰"] = "- Main image: Product on white background, but poor angle, details unclear"
    D["- 主图：重新拍摄，展示产品Usage Scenarios，角度更佳"] = "- Main image: Reshot showing product Usage Scenarios, better angle"
    D["- 买家Search Terms与Keyword完全相同（不区分大小写）"] = "- Buyer's Search Terms exactly match the Keyword (case-insensitive)"
    D["- 买家Search Terms与Keyword顺序相同"] = "- Buyer's Search Terms match the Keyword in the same order"
    D["- 买家Search Terms包含Keyword或Keyword的Variations时会触发"] = "- Triggered when buyer's Search Terms contain the Keyword or its variations"
    D["- 买家Search Terms包含Keyword的任何部分"] = "- Buyer's Search Terms contain any part of the Keyword"
    D["- 买家Search Terms包含Keyword的任何部分或相关词时都会触发"] = "- Triggered when buyer's Search Terms contain any part of the Keyword or related terms"
    D["- 买家Search Terms包含Keyword（顺序相同）"] = "- Buyer's Search Terms contain the Keyword (same order)"
    D["- 亚马逊仓库中价值$20,000的库存无法取回"] = "- $20,000 worth of inventory in Amazon warehouse cannot be retrieved"
    D["- 亚马逊认为Advertising不太可能转化时自动降低Bid"] = "- Amazon automatically lowers Bid when advertising is unlikely to convert"
    D["- 亚马逊认为Advertising可能转化时提高Bid（最高100%），认为不太可能转化时降低Bid"] = "- Amazon increases Bid when advertising may convert (up to 100%), decreases when unlikely to convert"
    D["- 亚马逊负责Warehousing、打包、配送、客服和Return"] = "- Amazon handles Warehousing, packing, shipping, customer service, and Returns"
    D["- 产品Innovation：开发带支架功能的手机壳"] = "- Product Innovation: Develop phone case with stand function"
    D["- 产品价格、Sales Volume、评价数量和评分"] = "- Product price, Sales Volume, review count, and rating"
    D["- 产品占图片面积的85%以上"] = "- Product occupies 85%+ of image area"
    D["- 产品安全问题（FDA Certification等）"] = "- Product safety issues (FDA Certification, etc.)"
    D["- 产品定位：中端价位，主打便携性和音质"] = "- Product positioning: Mid-range pricing, focusing on portability and sound quality"
    D["- 产品必须标注\"Made in China\""] = "- Products must be labeled \"Made in China\""
    D["- 产品特点和卖点"] = "- Product features and selling points"
    D["- 产品获得Prime标识"] = "- Product receives Prime badge"
    D["- 人工成本：$2.00/件"] = "- Labor cost: $2.00/item"
    D["- 价格和时效介于Express和Sea Freight之间"] = "- Price and delivery time between Express and Sea Freight"
    D["- 价格操纵"] = "- Price manipulation"
    D["- 价格范围：$5-$20"] = "- Price range: $5-$20"
    D["- 价格：$49.99，无Promotion标签"] = "- Price: $49.99, no Promotion badge"
    D["- 价格：设置Promotion价$39.99，添加\"Save 20%\"标签"] = "- Price: Set Promotion price $39.99, add \"Save 20%\" badge"
    D["- 优点：Process简单，无授权风险"] = "- Advantage: Simple process, no authorization risk"
    D["- 使用Brand词和类目词组合投放"] = "- Use combination of Brand words and category words"
    D["- 使用TikTok Ads投放Advertising"] = "- Use TikTok Ads for advertising"
    D["- 使用热门音乐和特效"] = "- Use trending music and effects"
    D["- 使用购买定向推广互补产品"] = "- Use purchase targeting for complementary products"
    D["- 侵犯Intellectual Property（Trademark、Patents、版权）"] = "- Intellectual Property infringement (Trademarks, Patents, copyright)"
    D["- 公司主体被列入黑名单"] = "- Company entity blacklisted"
    D["- 公司主体被列入黑名单，无法再Registration新Account"] = "- Company entity blacklisted, cannot register new Accounts"
    D["- 关注粉丝"] = "- Follow fans"
    D["- 典型类目：3C电子、家居用品、美妆个护等"] = "- Typical categories: Electronics, home goods, beauty & personal care, etc."
    D["- 删除无效Keyword（如\"bluetooth headphones\"）"] = "- Remove ineffective Keywords (e.g., \"bluetooth headphones\")"
    D["- 利润（Profit）：总利润"] = "- Profit: Total profit"
    D["- 前3秒抓住Note力"] = "- Capture attention in the first 3 seconds"
    D["- 包含产品名称、规格、材质等信息"] = "- Includes product name, specifications, material, etc."
    D["- 包含同义词、近义词、拼写错误"] = "- Includes synonyms, near-synonyms, spelling errors"
    D["- 包含常见拼写Variations和同义词"] = "- Includes common spelling variations and synonyms"
    D["- 包含常见拼写Variations和同义词（亚马逊自动识别）"] = "- Includes common spelling variations and synonyms (auto-detected by Amazon)"
    D["- 包含相关类目词"] = "- Includes related category words"
    D["- 包装材料：$1.00/件"] = "- Packaging material: $1.00/item"
    D["- 单件Head Haul成本：$2.50"] = "- Per-unit Head Haul cost: $2.50"
    D["- 卖家众多、Price War激烈、Profit Margin小、Advertising Cost高"] = "- Many sellers, intense Price War, small Profit Margin, high Advertising Cost"
    D["- 卖家少、价格稳定、Profit Margin大、Advertising Cost低"] = "- Few sellers, stable prices, large Profit Margin, low Advertising Cost"
    D["- 卖家手动设置Bid，亚马逊不自动调整"] = "- Seller manually sets Bid, Amazon does not auto-adjust"
    D["- 卖家自己负责Warehousing、打包、配送、客服和Return"] = "- Seller handles Warehousing, packing, shipping, customer service, and Returns"
    D["- 参与热门挑战"] = "- Participate in trending challenges"
    D["- 只有当买家Search Terms与Keyword完全匹配时才会触发"] = "- Only triggered when buyer's Search Terms exactly match the Keyword"
    D["- 可以使用文字说明"] = "- Text descriptions can be used"
    D["- 否定Exact Match：只排除\"cheap\"，不排除\"cheap wireless headphones\""] = "- Negative Exact Match: Only excludes \"cheap\", not \"cheap wireless headphones\""
    D["- 否定Phrase Match：排除\"cheap\"和包含\"cheap\"的所有搜索"] = "- Negative Phrase Match: Excludes \"cheap\" and all searches containing \"cheap\""
    D["- 周花费减少：$100 → $60"] = "- Weekly spend reduced: $100 → $60"
    D["- 售价：$39.99"] = "- Selling price: $39.99"
    D["- 回复评论"] = "- Reply to comments"
    D["- 国际运费：$8.00-$12.00/件"] = "- International shipping: $8.00-$12.00/item"
    D["- 在Product Images和Listing中使用了NikeBrand的Swoosh Logo"] = "- Used Nike Brand's Swoosh Logo in Product Images and Listing"
    D["- 在TikTok Shop后台申请开店"] = "- Apply to open store in TikTok Shop backend"
    D["- 在目标客户活跃时间发布"] = "- Post during target customer active hours"
    D["- 备货：从供应商采购50件，成本$15/件"] = "- Stock: Purchase 50 units from supplier at $15/unit"
    D["- 备货：采购100件（Recommendations最低备货量），成本$15/件"] = "- Stock: Purchase 100 units (recommended minimum), $15/unit"
    D["- 复购率提升：+22%"] = "- Repeat purchase rate increase: +22%"
    D["- 大批量Restock：Sea FreightFCL"] = "- Large batch Restock: Sea Freight FCL"
    D["- 头部卖家月销10000+件"] = "- Top sellers sell 10,000+ units/month"
    D["- 如果ROAS = 1.5（ACoS = 66.7%）：Advertising亏损，每花费$1Advertising亏$0.1"] = "- If ROAS = 1.5 (ACoS = 66.7%): Advertising at a loss, lose $0.1 per $1 spent"
    D["- 如果ROAS = 1.67（ACoS = 60%）：Advertising刚好盈亏平衡"] = "- If ROAS = 1.67 (ACoS = 60%): Advertising breaks even"
    D["- 如果ROAS = 2.0（ACoS = 50%）：Advertising利润为正，每花费$1Advertising赚$0.2"] = "- If ROAS = 2.0 (ACoS = 50%): Advertising profit is positive, earn $0.2 per $1 spent"
    D["- 如果选择Individual Seller：费用 = $0.99 × 30 = $29.7"] = "- If choosing Individual Seller: Fee = $0.99 × 30 = $29.7"
    D["- 如果选择Professional Seller：费用 = $39.99"] = "- If choosing Professional Seller: Fee = $39.99"
    D["- 如窒息危险Warning、高温Warning等"] = "- Such as choking hazard warnings, high temperature warnings, etc."
    D["- 存储：放在自己仓库，无Storage Fee"] = "- Storage: Stored in own warehouse, no Storage Fee"
    D["- 完成实名认证"] = "- Complete real-name verification"
    D["- 定价：$24.99（高于市场平均）"] = "- Pricing: $24.99 (above market average)"
    D["- 定向方式：购买定向（购买过厨房用品的用户）"] = "- Targeting: Purchase targeting (users who purchased kitchen products)"
    D["- 定期发布，保持活跃度"] = "- Post regularly to maintain activity"
    D["- 定期更换Advertising创意和产品组合"] = "- Regularly update ad creatives and product combinations"
    D["- 定期更新Advertising创意"] = "- Regularly update ad creatives"
    D["- 实际CPC降至$1.20"] = "- Actual CPC reduced to $1.20"
    D["- 实际CPC：$1.85"] = "- Actual CPC: $1.85"
    D["- 客户复购率：15%"] = "- Customer repeat purchase rate: 15%"
    D["- 将个人名下的Trademark转让给公司"] = "- Transfer personally owned Trademark to the company"
    D["- 小批量Restock：Sea FreightLCL或Air Freight"] = "- Small batch Restock: Sea Freight LCL or Air Freight"
    D["- 尺寸至少1000x1000像素（支持缩放）"] = "- Size at least 1000x1000 pixels (supports zoom)"
    D["- 展示产品细节、Usage Scenarios、尺寸Comparison等"] = "- Show product details, Usage Scenarios, size Comparison, etc."
    D["- 展示产品：瑜伽垫、瑜伽球、运动毛巾"] = "- Display products: yoga mat, yoga ball, sports towel"
    D["- 底部Advertising位"] = "- Bottom ad positions"
    D["- 建立Brand旗舰店，打造Brand形象"] = "- Build Brand Store to create Brand image"
    D["- 总体积：100立方米"] = "- Total volume: 100 cubic meters"
    D["- 总体积：20立方米"] = "- Total volume: 20 cubic meters"
    D["- 总费用（按月销100件）：$4.72/件"] = "- Total cost (based on 100 units/month): $4.72/unit"
    D["- 总费用：$11.00-$15.00/件"] = "- Total cost: $11.00-$15.00/unit"
    D["- 总重量：100kg"] = "- Total weight: 100kg"
    D["- 总重量：2000kg"] = "- Total weight: 2000kg"
    D["- 总重量：400kg"] = "- Total weight: 400kg"
    D["- 恶意竞争（跟卖、恶意投诉）"] = "- Malicious competition (hijacking, malicious complaints)"
    D["- 成本最高，但时效最快"] = "- Highest cost, but fastest delivery"
    D["- 成本高于Sea Freight，低于Express"] = "- Cost higher than Sea Freight, lower than Express"
    D["- 手机壳类目有500+卖家"] = "- Phone case category has 500+ sellers"
    D["- 打造高质量Listing，突出差异化卖点"] = "- Build high-quality Listing, highlight differentiation"
    D["- 投放Sponsored BrandsAdvertising，提升Brand认知"] = "- Run Sponsored Brands ads to boost Brand awareness"
    D["- 持续OptimizationAdvertisingKeyword"] = "- Continuously optimize Advertising Keywords"
    D["- 持续Optimization：每周调整Advertising Strategy和Listing"] = "- Continuous Optimization: Adjust Advertising Strategy and Listing weekly"
    D["- 提交材料等待审核"] = "- Submit materials and wait for review"
    D["- 操纵评价（刷单、虚假评论）"] = "- Review manipulation (brushing, fake reviews)"
    D["- 收集客户反馈，持续Optimization产品"] = "- Collect customer feedback, continuously optimize products"
    D["- 旗舰店访问量：+28%"] = "- Store traffic: +28%"
    D["- 无Prime标识"] = "- No Prime badge"
    D["- 无Storage Fee，但需要支付国际运费"] = "- No Storage Fee, but international shipping costs apply"
    D["- 无文字、无水印、无Logo"] = "- No text, no watermarks, no Logo"
    D["- 日均订单：15-20单"] = "- Daily orders: 15-20"
    D["- 日均订单：2-3单"] = "- Daily orders: 2-3"
    D["- 日均订单：5-8单"] = "- Daily orders: 5-8"
    D["- 日均订单：80-100单"] = "- Daily orders: 80-100"
    D["- 时效：20-35天"] = "- Delivery time: 20-35 days"
    D["- 时效：3-5天"] = "- Delivery time: 3-5 days"
    D["- 时效：5-10天"] = "- Delivery time: 5-10 days"
    D["- 曝光量（Impressions）：产品被展示的次数"] = "- Impressions: Number of times product is displayed"
    D["- 曝光：12,000次/周"] = "- Impressions: 12,000/week"
    D["- 曝光：15,000次"] = "- Impressions: 15,000"
    D["- 曝光：25,000次"] = "- Impressions: 25,000"
    D["- 曝光：30,000次/周"] = "- Impressions: 30,000/week"
    D["- 曝光：40,000次/周"] = "- Impressions: 40,000/week"
    D["- 曝光：5,000次/周"] = "- Impressions: 5,000/week"
    D["- 曝光：50,000次/周"] = "- Impressions: 50,000/week"
    D["- 更容易获得Buy Box"] = "- Easier to win Buy Box"
    D["- 月Sales Volume：3000+件"] = "- Monthly Sales Volume: 3,000+ units"
    D["- 月度Storage Fee：按立方英尺计算，Standards尺寸$0.87-$2.40/立方英尺"] = "- Monthly Storage Fee: Calculated per cubic foot, Standard size $0.87-$2.40/cu ft"
    D["- 月度Storage Fee：按立方英尺计算，Standards尺寸$0.87-$2.40/立方英尺，大件$0.53-$1.20/立方英尺"] = "- Monthly Storage Fee: Per cubic foot, Standard $0.87-$2.40/cu ft, Oversize $0.53-$1.20/cu ft"
    D["- 月度Storage Fee：约$0.50/件/月"] = "- Monthly Storage Fee: approx. $0.50/unit/month"
    D["- 有经验卖家：Fixed Bidding"] = "- Experienced sellers: Fixed Bidding"
    D["- 未获得Brand方授权"] = "- No Brand authorization obtained"
    D["- 未通过Second Review/KYC审核"] = "- Failed Second Review/KYC review"
    D["- 材质升级：使用环保材质，可降解"] = "- Material upgrade: Use eco-friendly, biodegradable materials"
    D["- 标签位置明显"] = "- Label position is prominent"
    D["- 标签清晰、不易脱落"] = "- Labels are clear and durable"
    D["- 核心Keyword排名：前3页"] = "- Core Keyword ranking: Top 3 pages"
    D["- 根据产品Features添加Warning标签"] = "- Add Warning labels based on product Features"
    D["- 每个产品必须有唯一的FNSKU标签"] = "- Each product must have a unique FNSKU label"
    D["- 每日点击：100次"] = "- Daily clicks: 100"
    D["- 每日点击：150次（由于Quality Score提升获得更多展示）"] = "- Daily clicks: 150 (more impressions due to Quality Score improvement)"
    D["- 每日花费：$180（花费更少但获得更多点击）"] = "- Daily spend: $180 (spending less but getting more clicks)"
    D["- 每日花费：$185"] = "- Daily spend: $185"
    D["- 毛利率：45%"] = "- Gross margin: 45%"
    D["- 毛利：$39.99 - $15 - $3.50 - $2 - $0.50 = $18.99/件"] = "- Gross profit: $39.99 - $15 - $3.50 - $2 - $0.50 = $18.99/unit"
    D["- 毛利：$39.99 - $15 - $8 = $16.99/件"] = "- Gross profit: $39.99 - $15 - $8 = $16.99/unit"
    D["- 流量最大，Precision低"] = "- Highest traffic, lowest Precision"
    D["- 测试不同的AdvertisingCreative Assets"] = "- Test different Ad Creatives"
    D["- 浏览定向：浏览过特定产品但未购买的用户"] = "- Browse targeting: Users who viewed specific products but didn't purchase"
    D["- 添加Negative Keywords"] = "- Add Negative Keywords"
    D["- 添加字幕和标签"] = "- Add subtitles and tags"
    D["- 点击量（Clicks）：产品被点击的次数"] = "- Clicks: Number of times product is clicked"
    D["- 点击：150次/周"] = "- Clicks: 150/week"
    D["- 点击：240次/周"] = "- Clicks: 240/week"
    D["- 点击：300次"] = "- Clicks: 300"
    D["- 点击：450次"] = "- Clicks: 450"
    D["- 点击：500次/周"] = "- Clicks: 500/week"
    D["- 点击：600次/周"] = "- Clicks: 600/week"
    D["- 点击：800次/周"] = "- Clicks: 800/week"
    D["- 然后用公司名义进行Brand Registry"] = "- Then proceed with Brand Registry under the company name"
    D["- 用身份证Registration一家公司，用护照Registration另一家公司，然后分别Registration两个亚马逊店铺是可行的"] = "- It is feasible to register one company with ID card and another with passport, then register two Amazon stores respectively"
    D["- 电池法Registration（EU）"] = "- Battery Law Registration (EU)"
    D["- 目标："] = "- Goal:"
    D["- 目标：>95%"] = "- Target: >95%"
    D["- 相似受众：与现有客户相似的用户"] = "- Similar audience: Users similar to existing customers"
    D["- 确保BrandSearch Terms带来的流量精准转化"] = "- Ensure Brand Search Terms traffic converts precisely"
    D["- 禁止价格欺诈"] = "- Price fraud prohibited"
    D["- 禁止使用他人Trademark"] = "- Use of others' Trademarks prohibited"
    D["- 禁止引导客户留评"] = "- Soliciting reviews prohibited"
    D["- 禁止提供奖励换取评论"] = "- Incentivized reviews prohibited"
    D["- 禁止操纵搜索排名"] = "- Search ranking manipulation prohibited"
    D["- 禁止虚假折扣"] = "- Fake discounts prohibited"
    D["- 禁止虚假订单"] = "- Fake orders prohibited"
    D["- 禁止购买或销售评论"] = "- Buying or selling reviews prohibited"
    D["- 禁止销售Infringement产品"] = "- Selling Infringing products prohibited"
    D["- 积累了50+条评价"] = "- Accumulated 50+ reviews"
    D["- 税务问题（VAT未Registration）"] = "- Tax issues (VAT not registered)"
    D["- 竞争极其激烈的市场"] = "- Extremely competitive market"
    D["- 竞争相对较小但市场Demand较高的市场"] = "- Relatively low competition but high market Demand"
    D["- 紧急Restock：Express"] = "- Emergency Restock: Express"
    D["- 纯白色背景（RGB: 255,255,255）"] = "- Pure white background (RGB: 255,255,255)"
    D["- 结合Video Format增强Brand Story传达"] = "- Combine Video Format to enhance Brand Story delivery"
    D["- 缺少Beneficial Owner Information（公司有3个股东，持股比例分别为40%、35%、25%）"] = "- Missing Beneficial Owner Information (company has 3 shareholders with 40%, 35%, 25% stakes)"
    D["- 自然订单占比：30%"] = "- Organic order ratio: 30%"
    D["- 自然订单占比：50%"] = "- Organic order ratio: 50%"
    D["- 花费：$120"] = "- Spend: $120"
    D["- 花费：$90"] = "- Spend: $90"
    D["- 获得Buy Box几率低"] = "- Low chance of winning Buy Box"
    D["- 订单保持：25单/周（不变）"] = "- Orders maintained: 25/week (unchanged)"
    D["- 订单数（Orders）：成交订单数量"] = "- Orders: Number of completed orders"
    D["- 订单量：15单/周 → 45单/周"] = "- Order volume: 15/week → 45/week"
    D["- 订单：15单"] = "- Orders: 15"
    D["- 订单：28单/周"] = "- Orders: 28/week"
    D["- 订单：30单/周"] = "- Orders: 30/week"
    D["- 订单：35单"] = "- Orders: 35"
    D["- 订单：35单/周"] = "- Orders: 35/week"
    D["- 订单：45单/周"] = "- Orders: 45/week"
    D["- 设计独特：与设计师合作推出限量版图案"] = "- Unique design: Collaborate with designers for limited edition patterns"
    D["- 评价积累：通过Early Reviewer Program获得20条评价"] = "- Review accumulation: Get 20 reviews through Early Reviewer Program"
    D["- 评价：500+条，4.6星"] = "- Reviews: 500+, 4.6 stars"
    D["- 购买定向：购买过特定产品的用户"] = "- Purchase targeting: Users who purchased specific products"
    D["- 费率：0.3%"] = "- Fee rate: 0.3%"
    D["- 费率：0.3%-0.5%"] = "- Fee rate: 0.3%-0.5%"
    D["- 费率：1%-2%"] = "- Fee rate: 1%-2%"
    D["- 费用：约$2,500"] = "- Cost: approx. $2,500"
    D["- 费用：约$600，单件$12.00"] = "- Cost: approx. $600, $12.00 per unit"
    D["- 超标后果：Account可能被Suspension"] = "- Consequence of exceeding limit: Account may be Suspended"
    D["- 身份证照片模糊，无法辨认姓名和身份证号"] = "- ID card photo blurry, name and ID number unreadable"
    D["- 适合新手卖家进入"] = "- Suitable for new sellers to enter"

    return D

D = build_dict()

# Load existing translations if any
try:
    with open(r'd:\网站建设\网址导航\amzrover.cn\translations.json', 'r', encoding='utf-8') as f:
        T = json.load(f)
except:
    T = {}

T.update(D)

with open(r'd:\网站建设\网址导航\amzrover.cn\translations.json', 'w', encoding='utf-8') as f:
    json.dump(T, f, ensure_ascii=False, indent=2)
print(f"Total entries: {len(T)}")

# Apply translations
def translate_file(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    for cn, en in sorted(T.items(), key=lambda x: len(x[0]), reverse=True):
        content = content.replace(cn, en)
    if content != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

count = 0
for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith('.html'):
            fp = os.path.join(root, f)
            if translate_file(fp):
                count += 1

print(f"Files translated: {count}")

# Check remaining
remaining = 0
for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith('.html'):
            fp = os.path.join(root, f)
            with open(fp, 'r', encoding='utf-8') as f:
                c = len(re.findall(r'[\u4e00-\u9fff]', f.read()))
            remaining += c
print(f"Remaining Chinese chars: {remaining}")
