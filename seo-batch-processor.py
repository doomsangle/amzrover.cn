#!/usr/bin/env python3
"""
SEO Batch Processor for amzrover.cn
批量添加SEO meta标签和结构化数据到所有HTML文件
"""

import os
import re
from pathlib import Path

# SEO配置数据
SEO_CONFIG = {
    # 中文页面SEO配置
    'zh': {
        'site_name': '亚马逊运营知识库 - amzrover.cn',
        'site_url': 'https://www.amzrover.cn',
        'language': 'zh-CN',
        'locale': 'zh_CN',
        'geo_region': 'CN-BJ',
        'geo_placename': 'Beijing, China',
        'geo_position': '39.9042;116.4074',
        'theme_color': '#FF9900',
        'twitter_site': '@amzrover',
        'pages': {
            '01-account-registration.html': {
                'title': '亚马逊账号注册流程详解',
                'desc': '亚马逊账号注册完整流程指南，包括卖家计划选择、KYC认证、营业执照准备、双币信用卡、收款账户设置等步骤详解。',
                'keywords': '亚马逊注册,账号注册,KYC认证,卖家计划,营业执照,亚马逊开店'
            },
            '02-worldfirst.html': {
                'title': 'WorldFirst跨境收款账户设置',
                'desc': 'WorldFirst跨境收款账户注册与使用指南，包括账户类型、提现规则、汇率优惠、多店铺管理等功能详解。',
                'keywords': 'WorldFirst,跨境收款,亚马逊收款,提现规则,汇率优惠'
            },
            '03-listing-upload.html': {
                'title': '亚马逊Listing上传与优化指南',
                'desc': '亚马逊Listing上传流程详解，包括产品标题、五点描述、关键词埋入、主图要求、A+页面制作、A/B测试等内容。',
                'keywords': 'Listing上传,产品标题,五点描述,关键词埋入,主图,A+页面'
            },
            '04-brand-registry.html': {
                'title': '亚马逊品牌备案流程与权益详解',
                'desc': '亚马逊品牌备案完整流程指南，包括商标注册、品牌申请、Brand Registry权益、品牌保护功能等内容。',
                'keywords': '品牌备案,Brand Registry,商标注册,品牌保护,亚马逊品牌'
            },
            '05-fba-shipping.html': {
                'title': '亚马逊FBA发货操作流程详解',
                'desc': '亚马逊FBA发货完整流程指南，包括产品包装、标签制作、货件创建、运费计算、入库时间等内容。',
                'keywords': 'FBA发货,产品包装,标签制作,货件创建,运费计算'
            },
            '06-logistics.html': {
                'title': '亚马逊物流渠道选择与对比',
                'desc': '亚马逊物流渠道对比分析，包括FBA、FBM、第三方物流的优缺点、成本分析、时效对比等内容。',
                'keywords': '物流渠道,FBA,FBM,第三方物流,运费对比'
            },
            '07-advertising.html': {
                'title': '亚马逊广告投放策略与操作指南',
                'desc': '亚马逊广告投放完整指南，包括广告类型、竞价策略、关键词优化、否定词应用、广告组架构等内容。',
                'keywords': '亚马逊广告,广告投放,竞价策略,关键词优化,否定词'
            },
            '08-after-sales.html': {
                'title': '亚马逊售后服务与客户沟通指南',
                'desc': '亚马逊售后服务操作流程，包括退货处理、退款规则、客户沟通、差评处理、投诉应对等内容。',
                'keywords': '售后服务,退货处理,退款规则,差评处理,客户沟通'
            },
            '09-settlement.html': {
                'title': '亚马逊结算与资金管理指南',
                'desc': '亚马逊结算流程与资金管理，包括回款周期、预留金、资金风险、现金流管理、汇率影响等内容。',
                'keywords': '亚马逊结算,回款周期,预留金,资金管理,现金流'
            },
            '10-data-analysis.html': {
                'title': '亚马逊数据分析方法与工具指南',
                'desc': '亚马逊数据分析方法论，包括销售报表、广告数据、库存分析、流量分析、竞品分析等内容。',
                'keywords': '数据分析,销售报表,广告数据,库存分析,竞品分析'
            },
            '10-review-management.html': {
                'title': '亚马逊评论管理策略与实操指南',
                'desc': '亚马逊评论管理完整指南，包括评论影响、评分管理、差评处理、正面评论获取、合规操作等内容。',
                'keywords': '评论管理,评分影响,差评处理,正面评论,合规操作'
            },
            '11-product-research.html': {
                'title': '亚马逊产品调研与选品方法论',
                'desc': '亚马逊产品调研方法论，包括市场分析、竞品研究、利润计算、需求验证、风险评估等内容。',
                'keywords': '产品调研,选品方法,市场分析,竞品研究,利润计算'
            },
            '12-inventory-management.html': {
                'title': '亚马逊库存管理与补货策略',
                'desc': '亚马逊库存管理指南，包括库存规划、补货时机、IPI指标、仓储费用、滞销处理等内容。',
                'keywords': '库存管理,补货策略,IPI指标,仓储费用,滞销处理'
            },
            '13-account-risk.html': {
                'title': '亚马逊账号风险预防与应对策略',
                'desc': '亚马逊账号风险预防指南，包括关联风险、刷单风险、侵权风险、绩效指标、申诉流程等内容。',
                'keywords': '账号风险,关联风险,刷单风险,侵权风险,申诉流程'
            },
            '14-ads-strategy.html': {
                'title': '亚马逊广告策略与优化方法',
                'desc': '亚马逊广告策略指南，包括广告架构、关键词布局、竞价优化、季节营销、新品推广等内容。',
                'keywords': '广告策略,关键词布局,竞价优化,季节营销,新品推广'
            },
            '15-profit-model.html': {
                'title': '亚马逊利润模型与成本分析',
                'desc': '亚马逊利润模型分析，包括定价策略、成本结构、利润计算、盈亏平衡、ROI分析等内容。',
                'keywords': '利润模型,定价策略,成本分析,ROI计算,盈亏平衡'
            },
            '16-product-lifecycle.html': {
                'title': '亚马逊产品生命周期管理',
                'desc': '亚马逊产品生命周期管理指南，包括新品期、成长期、成熟期、衰退期的运营策略。',
                'keywords': '产品生命周期,新品期,成长期,成熟期,运营策略'
            },
            '17-operational-decision.html': {
                'title': '亚马逊运营决策框架与方法',
                'desc': '亚马逊运营决策方法论，包括数据分析驱动决策、风险收益权衡、多维度考量等内容。',
                'keywords': '运营决策,数据分析,风险权衡,决策框架'
            },
            '18-official-docs-hub.html': {
                'title': '亚马逊官方文档中心',
                'desc': '亚马逊官方资源汇总，包括Seller Central、Help Center、Seller University、政策文档、API文档等内容。',
                'keywords': '官方文档,Seller Central,Help Center,政策文档,API'
            },
            '19-account-performance-risk.html': {
                'title': '亚马逊账号绩效与风险管理',
                'desc': '亚马逊账号绩效指标详解，包括ODR、LTR、LSR等指标要求、预警阈值、申诉流程等内容。',
                'keywords': '账号绩效,ODR指标,绩效预警,申诉流程'
            },
            '20-industry-slang.html': {
                'title': '亚马逊行业术语与黑话大全',
                'desc': '亚马逊卖家行业术语解释，包括爆款、跟卖、刷单、铺货、精品运营等专业术语详解。',
                'keywords': '行业术语,黑话解释,爆款,跟卖,刷单,铺货'
            },
            '21-advanced-operations.html': {
                'title': '亚马逊高级运营技巧与策略',
                'desc': '亚马逊高级运营技巧指南，包括多账号管理、多平台布局、品牌矩阵、数据分析进阶等内容。',
                'keywords': '高级运营,多账号管理,品牌矩阵,数据分析'
            },
            '22-risk-strategy-tradeoff.html': {
                'title': '亚马逊风险与策略权衡决策',
                'desc': '亚马逊风险与收益权衡决策框架，包括保守策略、激进策略、风险防控、决策模型等内容。',
                'keywords': '风险权衡,策略决策,风险防控,决策模型'
            },
            'compliance.html': {
                'title': '亚马逊认证与合规名词解释',
                'desc': '亚马逊认证合规指南，包括CPSC认证、CE认证、FCC认证、FDA认证、知识产权合规等内容。',
                'keywords': '认证合规,CPSC,CE认证,FCC认证,FDA认证,知识产权'
            },
            'fishbone.html': {
                'title': '亚马逊鱼骨图分析法应用',
                'desc': '亚马逊鱼骨图分析法应用指南，包括问题分析、根因挖掘、解决方案制定等内容。',
                'keywords': '鱼骨图,问题分析,根因分析,解决方案'
            }
        }
    },
    # 英文页面SEO配置
    'en': {
        'site_name': 'Amazon Seller Knowledge Base - amzrover.cn',
        'site_url': 'https://www.amzrover.cn',
        'language': 'en',
        'locale': 'en_US',
        'geo_region': 'CN-BJ',
        'geo_placename': 'Beijing, China',
        'geo_position': '39.9042;116.4074',
        'theme_color': '#FF9900',
        'twitter_site': '@amzrover',
        'pages': {
            '01-account-registration.html': {
                'title': 'Amazon Account Registration Guide',
                'desc': 'Complete guide to Amazon seller account registration, including seller plan selection, KYC verification, business license, payment account setup.',
                'keywords': 'Amazon registration,account setup,KYC verification,seller plan,business license'
            },
            '02-worldfirst.html': {
                'title': 'WorldFirst Cross-border Payment Setup',
                'desc': 'WorldFirst payment account registration and usage guide, including account types, withdrawal rules, exchange rate benefits.',
                'keywords': 'WorldFirst,cross-border payment,Amazon payment,withdrawal rules'
            },
            '03-listing-upload.html': {
                'title': 'Amazon Listing Upload & Optimization Guide',
                'desc': 'Amazon listing upload process guide, including product title, bullet points, keywords, main image, A+ content.',
                'keywords': 'Listing upload,product title,bullet points,keywords,main image,A+ content'
            },
            '04-brand-registry.html': {
                'title': 'Amazon Brand Registry Guide',
                'desc': 'Amazon Brand Registry complete guide, including trademark registration, brand application, Brand Registry benefits.',
                'keywords': 'Brand Registry,trademark registration,brand protection,Amazon brand'
            },
            '05-fba-shipping.html': {
                'title': 'Amazon FBA Shipping Process Guide',
                'desc': 'Amazon FBA shipping complete guide, including product packaging, label creation, shipment creation, shipping costs.',
                'keywords': 'FBA shipping,product packaging,label creation,shipment creation,shipping costs'
            },
            '06-logistics.html': {
                'title': 'Amazon Logistics Channel Comparison',
                'desc': 'Amazon logistics channel comparison, including FBA, FBM, third-party logistics advantages, cost analysis.',
                'keywords': 'Logistics channels,FBA,FBM,third-party logistics,cost comparison'
            },
            '07-advertising.html': {
                'title': 'Amazon Advertising Strategy Guide',
                'desc': 'Amazon advertising complete guide, including ad types, bidding strategy, keyword optimization, negative keywords.',
                'keywords': 'Amazon advertising,ad placement,bidding strategy,keyword optimization,negative keywords'
            },
            '08-after-sales.html': {
                'title': 'Amazon After-sales Service Guide',
                'desc': 'Amazon after-sales service process, including return handling, refund rules, customer communication, negative review handling.',
                'keywords': 'After-sales service,return handling,refund rules,negative review handling'
            },
            '09-settlement.html': {
                'title': 'Amazon Settlement & Fund Management Guide',
                'desc': 'Amazon settlement process and fund management, including payment cycle, reserve funds, cash flow management.',
                'keywords': 'Amazon settlement,payment cycle,reserve funds,fund management,cash flow'
            },
            '10-data-analysis.html': {
                'title': 'Amazon Data Analysis Methods Guide',
                'desc': 'Amazon data analysis methodology, including sales reports, advertising data, inventory analysis, traffic analysis.',
                'keywords': 'Data analysis,sales reports,advertising data,inventory analysis'
            },
            '10-review-management.html': {
                'title': 'Amazon Review Management Strategy Guide',
                'desc': 'Amazon review management complete guide, including review impact, rating management, negative review handling.',
                'keywords': 'Review management,rating impact,negative review handling,positive reviews'
            },
            '11-product-research.html': {
                'title': 'Amazon Product Research Methodology',
                'desc': 'Amazon product research methodology, including market analysis, competitor research, profit calculation.',
                'keywords': 'Product research,product selection,market analysis,competitor research'
            },
            '12-inventory-management.html': {
                'title': 'Amazon Inventory Management Guide',
                'desc': 'Amazon inventory management guide, including inventory planning, replenishment timing, IPI metrics.',
                'keywords': 'Inventory management,replenishment strategy,IPI metrics,storage fees'
            },
            '13-account-risk.html': {
                'title': 'Amazon Account Risk Prevention Guide',
                'desc': 'Amazon account risk prevention guide, including linking risk, fake review risk, infringement risk.',
                'keywords': 'Account risk,linking risk,fake review risk,infringement risk'
            },
            '14-ads-strategy.html': {
                'title': 'Amazon Advertising Strategy & Optimization',
                'desc': 'Amazon advertising strategy guide, including ad structure, keyword layout, bidding optimization.',
                'keywords': 'Advertising strategy,keyword layout,bidding optimization,seasonal marketing'
            },
            '15-profit-model.html': {
                'title': 'Amazon Profit Model & Cost Analysis',
                'desc': 'Amazon profit model analysis, including pricing strategy, cost structure, profit calculation, ROI.',
                'keywords': 'Profit model,pricing strategy,cost analysis,ROI calculation'
            },
            '16-product-lifecycle.html': {
                'title': 'Amazon Product Lifecycle Management',
                'desc': 'Amazon product lifecycle management guide, including new product, growth, maturity, decline phases.',
                'keywords': 'Product lifecycle,new product phase,growth phase,maturity phase'
            },
            '17-operational-decision.html': {
                'title': 'Amazon Operational Decision Framework',
                'desc': 'Amazon operational decision methodology, including data-driven decision, risk-benefit tradeoff.',
                'keywords': 'Operational decision,data analysis,risk tradeoff,decision framework'
            },
            '18-official-docs-hub.html': {
                'title': 'Amazon Official Documentation Hub',
                'desc': 'Amazon official resources summary, including Seller Central, Help Center, Seller University.',
                'keywords': 'Official documentation,Seller Central,Help Center,policy documents,API'
            },
            '19-account-performance-risk.html': {
                'title': 'Amazon Account Performance & Risk Management',
                'desc': 'Amazon account performance metrics, including ODR, LTR, LSR requirements, warning thresholds.',
                'keywords': 'Account performance,ODR metrics,performance warning,appeal process'
            },
            '20-industry-slang.html': {
                'title': 'Amazon Industry Terms & Slang Glossary',
                'desc': 'Amazon seller industry terms explanation, including hit products, hijacking, fake reviews.',
                'keywords': 'Industry terms,slang explanation,hit products,hijacking,fake reviews'
            },
            '21-advanced-operations.html': {
                'title': 'Amazon Advanced Operations Techniques',
                'desc': 'Amazon advanced operations guide, including multi-account management, brand matrix.',
                'keywords': 'Advanced operations,multi-account management,brand matrix'
            },
            '22-risk-strategy-tradeoff.html': {
                'title': 'Amazon Risk & Strategy Tradeoff Decision',
                'desc': 'Amazon risk-benefit tradeoff decision framework, including conservative strategy, aggressive strategy.',
                'keywords': 'Risk tradeoff,strategy decision,risk prevention,decision model'
            },
            'compliance.html': {
                'title': 'Amazon Certification & Compliance Guide',
                'desc': 'Amazon certification compliance guide, including CPSC certification, CE certification, FCC certification.',
                'keywords': 'Certification compliance,CPSC,CE certification,FCC certification'
            },
            'fishbone.html': {
                'title': 'Amazon Fishbone Diagram Analysis Application',
                'desc': 'Amazon fishbone diagram analysis guide, including problem analysis, root cause identification.',
                'keywords': 'Fishbone diagram,problem analysis,root cause analysis,solutions'
            }
        }
    }
}

def generate_seo_head(page_file, lang='zh', is_en_folder=False):
    """生成SEO meta标签和结构化数据"""
    
    config = SEO_CONFIG[lang]
    page_config = config['pages'].get(page_file, {
        'title': f'{page_file.replace(".html", "")} - amzrover.cn',
        'desc': '亚马逊运营知识库页面',
        'keywords': '亚马逊运营,amzrover'
    })
    
    # 构建URL
    if is_en_folder:
        canonical_url = f"{config['site_url']}/en/{page_file}"
        alternate_zh = f"{config['site_url']}/{page_file}"
        alternate_en = f"{config['site_url']}/en/{page_file}"
    else:
        canonical_url = f"{config['site_url']}/{page_file}"
        alternate_zh = f"{config['site_url']}/{page_file}"
        alternate_en = f"{config['site_url']}/en/{page_file}"
    
    seo_head = f'''
    <!-- Primary Meta Tags -->
    <meta name="title" content="{page_config['title']} - amzrover.cn">
    <meta name="description" content="{page_config['desc']}">
    <meta name="keywords" content="{page_config['keywords']}">
    <meta name="author" content="amzrover.cn">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{canonical_url}">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:title" content="{page_config['title']} - amzrover.cn">
    <meta property="og:description" content="{page_config['desc']}">
    <meta property="og:site_name" content="{config['site_name']}">
    <meta property="og:locale" content="{config['locale']}">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{page_config['title']} - amzrover.cn">
    <meta name="twitter:description" content="{page_config['desc']}">
    
    <!-- GEO Meta Tags -->
    <meta name="geo.region" content="{config['geo_region']}">
    <meta name="geo.placename" content="{config['geo_placename']}">
    <meta name="language" content="{config['language']}">
    <meta name="distribution" content="global">
    <meta name="rating" content="general">
    <meta name="revisit-after" content="7 days">
    
    <!-- Theme Meta Tags -->
    <meta name="theme-color" content="{config['theme_color']}">
    <meta name="apple-mobile-web-app-capable" content="yes">
    
    <!-- Security Meta Tags -->
    <meta name="referrer" content="strict-origin-when-cross-origin">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    <!-- hreflang Links -->
    <link rel="alternate" hreflang="zh-CN" href="{alternate_zh}">
    <link rel="alternate" hreflang="en" href="{alternate_en}">
    <link rel="alternate" hreflang="x-default" href="{alternate_zh}">
    
    <!-- Structured Data -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": "{page_config['title']} - amzrover.cn",
        "description": "{page_config['desc']}",
        "url": "{canonical_url}",
        "inLanguage": "{config['language']}",
        "isPartOf": {{
            "@type": "WebSite",
            "name": "{config['site_name']}",
            "url": "{config['site_url']}"
        }},
        "datePublished": "2026-06-27",
        "dateModified": "2026-06-27"
    }}
    </script>
'''
    
    return seo_head

def process_html_file(file_path, page_file, lang='zh', is_en_folder=False):
    """处理单个HTML文件，添加SEO标签"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已有SEO标签
        if '<meta name="description"' in content and 'og:title' in content:
            print(f"[跳过] {file_path} - 已有SEO标签")
            return False
        
        # 找到<head>标签后的位置
        head_pattern = r'(<head>.*?<title>.*?</title>)'
        match = re.search(head_pattern, content, re.DOTALL)
        
        if match:
            seo_head = generate_seo_head(page_file, lang, is_en_folder)
            new_content = content.replace(match.group(1), match.group(1) + seo_head)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"[成功] {file_path} - SEO标签已添加")
            return True
        else:
            print(f"[失败] {file_path} - 未找到<title>标签")
            return False
            
    except Exception as e:
        print(f"[错误] {file_path} - {str(e)}")
        return False

def main():
    """主函数 - 批量处理所有HTML文件"""
    
    base_path = Path('d:/网站建设/网址导航/amzrover.cn')
    
    # 处理中文页面
    zh_pages = SEO_CONFIG['zh']['pages']
    for page_file in zh_pages:
        file_path = base_path / page_file
        if file_path.exists():
            process_html_file(file_path, page_file, 'zh', False)
    
    # 处理英文页面
    en_pages = SEO_CONFIG['en']['pages']
    for page_file in en_pages:
        file_path = base_path / 'en' / page_file
        if file_path.exists():
            process_html_file(file_path, page_file, 'en', True)
    
    print("\nSEO批量处理完成！")

if __name__ == '__main__':
    main()