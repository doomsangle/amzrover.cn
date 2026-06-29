# Amazon Seller Knowledge Base (amzrover.cn)

> From beginner to expert — a one-stop guide to Amazon operations core concepts

## About

An Amazon seller operations knowledge navigation website covering the full workflow: certification & compliance, advertising, on-site operations, logistics & fulfillment, data analytics, and more. A pure static HTML site with no build tools required — ready to deploy directly.

## Key Features

- **Bilingual Support**: Complete English mirror in the `en/` directory with language switcher
- **SEO Optimization**: Full Meta tags, Open Graph, Twitter Card, JSON-LD structured data, robots.txt, sitemap.xml (with hreflang language tags)
- **Fishbone Diagram**: Pure CSS/SVG hand-drawn visualization, embedded via iframe on homepage, auto-switches to list layout on mobile
- **Responsive Design**: Mobile-friendly via `@media` queries
- **Knowledge Cross-references**: Pages interconnected via FAQ tags (blue) and terminology tags (purple)
- **Cost Calculators**: Integrated commission calculator, FBA fee calculator, profit calculator with real-time calculation
- **Review Management**: Detailed strategies for review management, rating impact on sales, and compliant review acquisition methods

## Project Architecture

```
amzrover.cn/
├── index.html                  # Homepage navigation (Fishbone diagram + Operations timeline + Advanced knowledge grid)
├── fishbone.html               # Fishbone diagram visualization (embedded via iframe on homepage)
├── compliance.html             # Certification & compliance guide
├── privacy-policy.html         # Privacy policy page
├── robots.txt                  # Search engine crawling rules (with malicious bot restrictions)
├── sitemap.xml                 # Site map (with hreflang tags, 140+ URLs)
├── ads.txt                     # Authorized Digital Sellers file
├── nginx.conf                  # Nginx deployment configuration (with HTTPS support)
│
├── 01-account-registration.html ~ 09-settlement.html   # Operations workflow (9 beginner steps)
├── 10-data-analysis.html ~ 23-cost-calculator.html     # Advanced topics (14 subjects)
│
├── faq/                        # FAQs (20 topic categories)
│   ├── faq-index.html          #   FAQ index page
│   ├── faq-registration.html   #   Registration FAQ
│   ├── faq-account.html        #   Account FAQ
│   ├── faq-brand.html          #   Brand FAQ
│   ├── faq-ads.html            #   Advertising FAQ
│   ├── faq-optimization.html   #   Ad optimization FAQ
│   ├── faq-fba.html            #   FBA logistics FAQ
│   ├── faq-shipping.html       #   International shipping FAQ
│   ├── faq-listing.html        #   Listing optimization FAQ
│   ├── faq-product-research.html # Product research FAQ
│   ├── faq-performance.html    #   Performance metrics FAQ
│   ├── faq-risk.html           #   Risk control & appeal FAQ
│   ├── faq-settlement.html     #   Settlement process FAQ
│   ├── faq-finance.html        #   Financial management FAQ
│   ├── faq-data.html           #   Data analytics FAQ
│   ├── faq-tools.html          #   Tools FAQ
│   ├── faq-ip.html             #   Intellectual property FAQ
│   ├── faq-compliance.html     #   Compliance requirements FAQ
│   ├── faq-policy.html         #   Platform policy FAQ
│   ├── faq-multi-platform.html #   Multi-platform FAQ
│   └── faq-tiktok.html         #   TikTok e-commerce FAQ
│
├── terms/                      # Terminology glossary (24 core terms)
│   ├── terms-index.html        #   Terms index page
│   ├── acos.html               #   ACoS
│   ├── roas.html               #   ROAS
│   ├── cpc.html                #   CPC
│   ├── ctr.html                #   CTR
│   ├── fba.html                #   FBA
│   ├── fbm.html                #   FBM
│   ├── kyc.html                #   KYC verification
│   ├── conversion-rate.html    #   Conversion rate
│   ├── sponsored-products.html #   Sponsored Products
│   ├── sponsored-brands.html   #   Sponsored Brands
│   ├── sponsored-display.html  #   Sponsored Display
│   ├── exact-match.html        #   Exact match
│   ├── phrase-match.html       #   Phrase match
│   ├── broad-match.html        #   Broad match
│   ├── negative-keywords.html  #   Negative keywords
│   ├── dynamic-bidding.html    #   Dynamic bidding
│   ├── head-haul.html          #   Head haul (first-leg shipping)
│   ├── professional-seller.html #  Professional seller
│   ├── baokuan.html            #   Best seller (hit product)
│   ├── honghai.html            #   Red ocean (saturated market)
│   ├── fenghao.html            #   Account suspension
│   ├── guanlian.html           #   Account association
│   ├── qiliang.html            #   Traction (scaling up)
│   └── poa.html                #   POA (Plan of Action)
│
├── assets/                     # Stylesheets
│   ├── style.css               #   Global styles (612 lines)
│   └── term-style.css          #   Terminology page styles (325 lines)
│
├── en/                         # English mirror directory (complete replica)
│   ├── index.html, fishbone.html, compliance.html
│   ├── privacy-policy.html
│   ├── 01-account-registration.html ~ 23-cost-calculator.html
│   ├── faq/                    # 20 English FAQ pages
│   ├── terms/                  # 24 English terminology pages
│   └── assets/                 # English stylesheets
│
└── translate-*.py              # Python translation scripts (7 tools)
    ├── translate-all.py        # Batch translate all English pages
    └── ...                     # Other translation helper scripts
```

## Content Modules

### Operations Workflow (9 Beginner Steps)

| # | Topic | File |
|---|-------|------|
| 1 | Amazon store registration | `01-account-registration.html` |
| 2 | WorldFirst registration & bank account linking | `02-worldfirst.html` |
| 3 | Listing product upload | `03-listing-upload.html` |
| 4 | Brand registration & binding | `04-brand-registry.html` |
| 5 | FBA shipment to Amazon warehouse | `05-fba-shipping.html` |
| 6 | Amazon warehouse logistics | `06-logistics.html` |
| 7 | Amazon advertising | `07-advertising.html` |
| 8 | After-sales service | `08-after-sales.html` |
| 9 | Account settlement & payouts | `09-settlement.html` |

### Advanced Topics (14 Subjects)

| Topic | File |
|-------|------|
| Data analytics | `10-data-analysis.html` |
| Review management | `10-review-management.html` |
| Product research | `11-product-research.html` |
| Inventory management | `12-inventory-management.html` |
| Account risk | `13-account-risk.html` |
| Advertising strategy | `14-ads-strategy.html` |
| Profit model | `15-profit-model.html` |
| Product lifecycle | `16-product-lifecycle.html` |
| Operational decisions | `17-operational-decision.html` |
| Official documentation hub | `18-official-docs-hub.html` |
| Account performance risk | `19-account-performance-risk.html` |
| Industry slang | `20-industry-slang.html` |
| Advanced operations | `21-advanced-operations.html` |
| Risk vs. strategy trade-offs | `22-risk-strategy-tradeoff.html` |
| Cost calculator | `23-cost-calculator.html` |

## Tech Stack

- **Pure static site**: HTML + CSS, no JS frameworks, no build tools
- **Responsive design**: Mobile-friendly via `@media` queries
- **Design style**: Gradient backgrounds, rounded cards, hover animations
- **Fishbone diagram**: Hand-crafted in pure CSS, embedded on the homepage via iframe
- **Internationalization**: `en/` directory mirror structure with hreflang language tags
- **SEO**: Complete robots.txt, sitemap.xml, Meta tags, JSON-LD structured data
- **Real-time calculation**: JavaScript-powered cost calculators for commission, FBA fees, profit, etc.

## Page Statistics

| Category | Count |
|----------|-------|
| Chinese HTML pages | 72 |
| English HTML pages | 72 |
| **Total HTML pages** | **144** |
| Operations workflow (beginner) | 9 |
| Advanced topic pages | 14 |
| FAQ categories | 20 |
| FAQ pages (with index) | 21 |
| Terminology entries | 24 |
| Terminology pages (with index) | 25 |
| CSS files | 4 (2 Chinese + 2 English) |
| Python translation scripts | 8 |

## SEO Infrastructure

- **robots.txt**: Crawling rules and sitemap location with language version declarations, including malicious bot restrictions
- **sitemap.xml**: Contains all 144+ URLs with `xhtml:link rel="alternate"` hreflang tags for each URL
- **Meta tags**: Complete title, description, keywords, robots, canonical
- **Open Graph**: Social sharing preview support (og:type, og:url, og:title, og:description)
- **Twitter Card**: Twitter sharing support (twitter:card, twitter:title, twitter:description)
- **JSON-LD**: Structured data markup for enhanced search display
- **GEO tags**: geo.region, geo.placename, language, distribution
- **ads.txt**: Authorized Digital Sellers file to prevent ad fraud

## Deployment Guide

### Local Development

```bash
# Start local development server
node server.js

# Visit http://localhost:8080/
```

### Nginx Deployment

The project includes a complete Nginx configuration file `nginx.conf` with support for:

- HTTP → HTTPS automatic redirection
- SSL/TLS certificate configuration (Let's Encrypt)
- HTTP/2 protocol support
- Gzip compression optimization
- Static file caching configuration
- Security headers (HSTS, X-Frame-Options, X-XSS-Protection)

### Server-side Configuration

```bash
# Upload files to server
scp -r * root@your-server-ip:/var/www/html/amzrover.cn/

# Set permissions (CentOS/RHEL)
chown -R nginx:nginx /var/www/html/amzrover.cn
chmod -R 755 /var/www/html/amzrover.cn

# Apply SSL certificate
certbot --nginx -d amzrover.cn -d www.amzrover.cn

# Test configuration
nginx -t

# Reload Nginx
systemctl reload nginx
```

## Translation Toolchain

The project includes Python translation scripts for synchronizing Chinese-English content:

```bash
# Batch translate all English pages
python translate-all.py
```

Translation scripts use dictionary mapping for Chinese-to-English replacement, with length-based sorting to avoid partial matching issues.

## Contributing

1. Fork this repository
2. Create a Feat_xxx branch
3. Commit your code
4. Open a Pull Request

## License

MIT License
