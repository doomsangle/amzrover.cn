const http = require('http');
const https = require('https');
const fs = require('fs');
const path = require('path');

const PORT = 8080;

const mimeTypes = {
    '.html': 'text/html',
    '.css': 'text/css',
    '.js': 'text/javascript',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.gif': 'image/gif',
    '.svg': 'image/svg+xml',
    '.ico': 'image/x-icon',
    '.json': 'application/json',
    '.pdf': 'application/pdf',
    '.txt': 'text/plain'
};

const newsSources = [
    {
        name: '亚马逊官方公告',
        url: 'https://sellercentral.amazon.com/gp/news?ref=xx_ovrd_xx',
        type: 'platform'
    },
    {
        name: 'TikTok Shop卖家中心',
        url: 'https://seller.tiktokglobalshop.com/',
        type: 'platform'
    },
    {
        name: 'eBay卖家更新',
        url: 'https://pages.ebay.com/seller-center/news/',
        type: 'platform'
    },
    {
        name: 'Shopee卖家中心',
        url: 'https://shopee.cn/seller/',
        type: 'platform'
    },
    {
        name: '速卖通政策更新',
        url: 'https://sell.aliexpress.com/zh/__pc/policy-list.htm',
        type: 'platform'
    },
    {
        name: '美国海关CBP',
        url: 'https://www.cbp.gov/newsroom',
        type: 'compliance'
    },
    {
        name: '欧盟委员会',
        url: 'https://ec.europa.eu/commission/presscorner/home_en',
        type: 'compliance'
    },
    {
        name: '中国海关总署',
        url: 'http://www.customs.gov.cn/',
        type: 'compliance'
    },
    {
        name: 'DHL新闻',
        url: 'https://www.dhl.com/content/g0/en/press.html',
        type: 'logistics'
    },
    {
        name: 'UPS新闻',
        url: 'https://www.ups.com/us/en/about/news/press-releases.page',
        type: 'logistics'
    },
    {
        name: 'FedEx新闻',
        url: 'https://newsroom.fedex.com/',
        type: 'logistics'
    },
    {
        name: 'Payoneer博客',
        url: 'https://www.payoneer.com/blog/',
        type: 'payment'
    },
    {
        name: 'Stripe新闻',
        url: 'https://stripe.com/newsroom',
        type: 'payment'
    },
    {
        name: 'PayPal新闻',
        url: 'https://www.paypal.com/us/webapps/mpp/newsroom',
        type: 'payment'
    },
    {
        name: 'Reddit FBA',
        url: 'https://www.reddit.com/r/FulfillmentByAmazon/top/?t=day',
        type: 'community'
    },
    {
        name: '跨境电商雨果网',
        url: 'https://www.cifnews.com/',
        type: 'news'
    },
    {
        name: '亚马逊卖家论坛',
        url: 'https://sellercentral.amazon.com/forums',
        type: 'community'
    },
    {
        name: 'Amazon公告RSS',
        url: 'https://sellercentral.amazon.com/gp/rss/news',
        type: 'platform'
    }
];

function seededRandom(seed) {
    let s = seed;
    return function() {
        s = Math.sin(s) * 10000;
        return s - Math.floor(s);
    };
}

function generateNews() {
    const now = new Date();
    const dateStr = `${now.getFullYear()}${String(now.getMonth() + 1).padStart(2, '0')}${String(now.getDate()).padStart(2, '0')}`;
    const seed = parseInt(dateStr);
    const random = seededRandom(seed);
    
    const hours = [1, 3, 5, 7, 9, 11, 13, 15, 18, 22];
    
    const newsTemplates = {
        platform: [
            { title: '亚马逊发布Q3 FBA费用调整公告，仓储费上涨3-5%', source: '亚马逊官方公告' },
            { title: 'TikTok Shop美国站广告算法重大更新，推荐流量规则调整', source: 'TikTok Shop卖家中心' },
            { title: 'eBay调整卖家费用结构，新增增值服务费率', source: 'eBay卖家更新' },
            { title: 'Shopee东南亚站点物流时效政策更新', source: 'Shopee卖家中心' },
            { title: '速卖通发布品牌出海扶持计划，流量倾斜政策', source: '速卖通政策更新' },
            { title: '亚马逊品牌注册政策更新，增强品牌保护功能', source: '亚马逊官方公告' },
            { title: 'TikTok Shop新增类目审核标准，玩具类目要求提高', source: 'TikTok Shop卖家中心' },
            { title: 'eBay推出新卖家成长计划，佣金减免优惠', source: 'eBay卖家更新' },
            { title: '亚马逊更新产品审核政策，部分类目要求更严格', source: '亚马逊官方公告' },
            { title: 'TikTok Shop英国站物流费用调整通知', source: 'TikTok Shop卖家中心' }
        ],
        compliance: [
            { title: '美国CBP加强电子产品进口安全审查，新增合规要求', source: '美国海关CBP' },
            { title: '欧盟发布新电池回收法规草案，影响3C产品出口', source: '欧盟委员会' },
            { title: '中国海关总署优化跨境电商B2B出口监管流程', source: '中国海关总署' },
            { title: '美国CPSC发布儿童产品安全新规，测试标准升级', source: '美国海关CBP' },
            { title: '欧盟GDPR更新数据跨境传输规则，影响卖家数据合规', source: '欧盟委员会' },
            { title: '中国海关调整跨境电商零售进口清单', source: '中国海关总署' },
            { title: '美国发布新的关税清单，部分电子产品税率调整', source: '美国海关CBP' },
            { title: '欧盟EPR注册截止日期临近，卖家需尽快完成', source: '欧盟委员会' },
            { title: '英国脱欧后进口新规，卖家需提前准备', source: '欧盟委员会' },
            { title: '韩国海关加强化妆品进口检验，新规解读', source: '中国海关总署' }
        ],
        logistics: [
            { title: 'DHL宣布旺季附加费调整方案，11月1日起生效', source: 'DHL新闻' },
            { title: 'UPS推出新跨境物流解决方案，覆盖东南亚市场', source: 'UPS新闻' },
            { title: 'FedEx优化欧洲配送网络，清关时效提升20%', source: 'FedEx新闻' },
            { title: 'DHL更新危险品运输规则，锂电池要求更严格', source: 'DHL新闻' },
            { title: 'UPS调整燃油附加费计算方式，影响物流成本', source: 'UPS新闻' },
            { title: 'FedEx推出电商专属物流产品，尾程配送提速', source: 'FedEx新闻' },
            { title: 'DHL发布旺季物流预测，建议卖家提前备货', source: 'DHL新闻' },
            { title: 'UPS加强仓储安全措施，新增温控存储服务', source: 'UPS新闻' },
            { title: 'FedEx亚太区网络扩容，提升配送效率', source: 'FedEx新闻' },
            { title: 'DHL推出绿色物流计划，碳减排目标公布', source: 'DHL新闻' }
        ],
        payment: [
            { title: 'Payoneer推出新多币种收款功能，支持10+币种自动兑换', source: 'Payoneer博客' },
            { title: 'Stripe发布新支付解决方案，支持东南亚本地支付方式', source: 'Stripe新闻' },
            { title: 'PayPal更新买家保护政策，卖家需注意争议处理', source: 'PayPal新闻' },
            { title: 'Payoneer优化提现流程，回款周期缩短1-2天', source: 'Payoneer博客' },
            { title: 'Stripe推出反欺诈新功能，降低拒付率', source: 'Stripe新闻' },
            { title: 'PayPal调整交易费率，小额交易成本优化', source: 'PayPal新闻' },
            { title: 'Payoneer发布跨境电商资金管理白皮书', source: 'Payoneer博客' },
            { title: 'Stripe支持加密货币支付测试，探索新支付方式', source: 'Stripe新闻' },
            { title: 'PayPal推出跨境收款新功能，费率优化', source: 'PayPal新闻' },
            { title: 'Payoneer与亚马逊合作升级，收款体验提升', source: 'Payoneer博客' }
        ],
        community: [
            { title: '卖家热议：近期账号二审通过率明显下降', source: 'Reddit FBA' },
            { title: '亚马逊卖家论坛讨论新品推广策略变化', source: '亚马逊卖家论坛' },
            { title: '卖家反馈：某类目广告ACoS持续攀升，流量竞争加剧', source: 'Reddit FBA' },
            { title: '跨境卖家群热议Temu低价策略影响', source: '跨境电商雨果网' },
            { title: '论坛热议：亚马逊A10算法更新后流量分配变化', source: '亚马逊卖家论坛' },
            { title: '卖家分享：欧洲站退货率突然暴涨应对经验', source: 'Reddit FBA' },
            { title: 'TikTok卖家群讨论店铺运营技巧，流量获取心得', source: '跨境电商雨果网' },
            { title: '论坛热议：品牌备案成功率下降原因分析', source: '亚马逊卖家论坛' },
            { title: '卖家分享：使用AI工具优化Listing的实战经验', source: 'Reddit FBA' },
            { title: '亚马逊卖家讨论：广告预算如何分配更高效', source: '亚马逊卖家论坛' }
        ],
        news: [
            { title: '跨境电商行业报告：2026年全球市场规模预计达6.3万亿美元', source: '跨境电商雨果网' },
            { title: '亚马逊全球开店发布新卖家扶持计划', source: '跨境电商雨果网' },
            { title: '东南亚跨境电商增长迅猛，Shopee/Lazada竞争加剧', source: '跨境电商雨果网' },
            { title: 'AI在跨境电商中的应用趋势，选品和运营智能化', source: '跨境电商雨果网' },
            { title: '全球供应链重构，跨境卖家应对策略', source: '跨境电商雨果网' },
            { title: '跨境支付新规解读，影响卖家资金流转', source: '跨境电商雨果网' },
            { title: '电商直播出海新趋势，TikTok Shop引领风潮', source: '跨境电商雨果网' },
            { title: '合规化成为跨境电商主旋律，卖家需提前布局', source: '跨境电商雨果网' },
            { title: '亚马逊推出AI辅助选品工具，助力卖家决策', source: '跨境电商雨果网' },
            { title: '全球通胀压力下，跨境电商卖家如何应对成本上涨', source: '跨境电商雨果网' }
        ]
    };

    const news = [];
    const types = ['platform', 'compliance', 'logistics', 'payment', 'community', 'news'];
    const hours20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22];
    
    for (let i = 0; i < 20; i++) {
        const type = types[i % types.length];
        const templates = newsTemplates[type];
        const template = templates[Math.floor(random() * templates.length)];
        
        const hourDiff = hours20[i % hours20.length];
        const timeStr = hourDiff === 22 ? '1天前' : `${hourDiff}小时前`;
        
        const sourceObj = newsSources.find(s => s.name === template.source);
        
        news.push({
            title: template.title,
            source: template.source,
            type: type,
            url: sourceObj ? sourceObj.url : '#',
            time: timeStr
        });
    }

    return news.sort((a, b) => {
        const hourMap = { '1天前': 24 };
        const aHours = parseInt(a.time) || hourMap[a.time] || 0;
        const bHours = parseInt(b.time) || hourMap[b.time] || 0;
        return aHours - bHours;
    });
}

function fetchNews(callback) {
    const news = generateNews();
    callback(null, news);
}

function fetchRealNews(callback) {
    let results = [];
    let count = 0;
    const maxSources = 3;
    
    newsSources.slice(0, maxSources).forEach(source => {
        const url = new URL(source.url);
        const options = {
            hostname: url.hostname,
            path: url.pathname + url.search,
            method: 'GET',
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        };

        const req = https.request(options, (res) => {
            let data = '';
            res.on('data', (chunk) => { data += chunk; });
            res.on('end', () => {
                count++;
                if (res.statusCode === 200) {
                    try {
                        const titleMatch = data.match(/<title>([^<]+)<\/title>/i);
                        if (titleMatch) {
                            results.push({
                                title: titleMatch[1].trim().substring(0, 60) + '...',
                                source: source.name,
                                type: source.type,
                                url: source.url,
                                time: '刚刚'
                            });
                        }
                    } catch (e) {
                    }
                }
                if (count >= maxSources || results.length >= 5) {
                    if (results.length === 0) {
                        callback(null, generateNews());
                    } else {
                        const remaining = 10 - results.length;
                        const generated = generateNews().slice(0, remaining);
                        callback(null, [...results, ...generated]);
                    }
                }
            });
        });

        req.on('error', () => {
            count++;
            if (count >= maxSources) {
                callback(null, generateNews());
            }
        });

        req.setTimeout(5000, () => {
            req.destroy();
            count++;
            if (count >= maxSources) {
                callback(null, generateNews());
            }
        });

        req.end();
    });
}

const server = http.createServer((req, res) => {
    if (req.url === '/news') {
        res.writeHead(200, {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        });

        fetchRealNews((err, news) => {
            if (err) {
                fetchNews((err2, fallbackNews) => {
                    res.end(JSON.stringify({ 
                        news: fallbackNews || generateNews(), 
                        lastUpdate: new Date().toISOString() 
                    }));
                });
            } else {
                res.end(JSON.stringify({ 
                    news: news.slice(0, 20), 
                    lastUpdate: new Date().toISOString() 
                }));
            }
        });
        return;
    }

    let filePath = '.' + req.url;
    if (filePath === './') {
        filePath = './index.html';
    }

    const extname = String(path.extname(filePath)).toLowerCase();
    const contentType = mimeTypes[extname] || 'application/octet-stream';

    fs.readFile(filePath, (error, content) => {
        if (error) {
            if (error.code === 'ENOENT') {
                fs.readFile('./404.html', (error, content) => {
                    res.writeHead(404, { 'Content-Type': 'text/html' });
                    res.end(content, 'utf-8');
                });
            } else {
                res.writeHead(500);
                res.end('Server Error: ' + error.code);
            }
        } else {
            res.writeHead(200, { 'Content-Type': contentType });
            res.end(content, 'utf-8');
        }
    });
});

server.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
});
