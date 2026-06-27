# Amazon Seller Knowledge Base (amzrover.cn)

> From beginner to expert — a one-stop guide to Amazon operations core concepts

## About

An Amazon seller operations knowledge navigation website covering the full workflow: certification & compliance, advertising, on-site operations, logistics & fulfillment, data analytics, and more. A pure static HTML site with no build tools required — ready to deploy directly.

## Project Architecture

```
amzrover.cn/
├── index.html                  # Homepage navigation (Fishbone diagram + Operations timeline + Advanced knowledge grid)
├── fishbone.html               # Fishbone diagram visualization (embedded via iframe on homepage)
├── compliance.html             # Certification & compliance guide
│
├── 01-account-registration.html ~ 09-settlement.html   # Operations workflow (9 beginner steps)
├── 10-data-analysis.html ~ 22-risk-strategy-tradeoff.html # Advanced topics (13 subjects)
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
└── assets/                     # Stylesheets
    ├── style.css               #   Global styles (612 lines)
    └── term-style.css          #   Terminology page styles (325 lines)
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

### Advanced Topics (13 Subjects)

| Topic | File |
|-------|------|
| Data analytics | `10-data-analysis.html` |
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

## Tech Stack

- **Pure static site**: HTML + CSS, no JS frameworks, no build tools
- **Responsive design**: Mobile-friendly via `@media` queries
- **Design style**: Gradient backgrounds, rounded cards, hover animations
- **Fishbone diagram**: Hand-crafted in pure CSS, embedded on the homepage via iframe
- **Cross-references**: Pages are interconnected via tag links (FAQ / Terminology)

## Page Statistics

| Category | Count |
|----------|-------|
| Total HTML pages | ~50 |
| Operations workflow (beginner) | 9 |
| Advanced topic pages | 13 |
| FAQ categories | 20 |
| Terminology entries | 24 |
| CSS files | 2 |

## Getting Started

This is a pure static site — no dependencies to install or build steps required.

1. Double-click `index.html` to open it directly in your browser
2. Or deploy to any static hosting service (Nginx, GitHub Pages, Gitee Pages, Vercel, etc.)

## Contributing

1. Fork this repository
2. Create a Feat_xxx branch
3. Commit your code
4. Open a Pull Request
