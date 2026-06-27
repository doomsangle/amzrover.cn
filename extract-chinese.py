import re, os, json

base = r'd:\网站建设\网址导航\amzrover.cn\en'
segments = set()

# Patterns to extract Chinese text segments
patterns = [
    # Text content between tags (including mixed Chinese/English)
    r'>([^<]*[\u4e00-\u9fff][^<]*)<',
    # Attribute values with Chinese
    r'content="([^"]*[\u4e00-\u9fff][^"]*)"',
    r'keywords" content="([^"]*)"',
]

for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith('.html'):
            fp = os.path.join(root, f)
            with open(fp, encoding='utf-8') as fh:
                content = fh.read()
                for pat in patterns:
                    for m in re.finditer(pat, content):
                        text = m.group(1).strip()
                        if text and re.search(r'[\u4e00-\u9fff]', text):
                            segments.add(text)

# Write to file for review
with open(r'd:\网站建设\网址导航\amzrover.cn\chinese-segments.json', 'w', encoding='utf-8') as f:
    json.dump(sorted(list(segments)), f, ensure_ascii=False, indent=2)

print(f"Found {len(segments)} unique Chinese text segments")
