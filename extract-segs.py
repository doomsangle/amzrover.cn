import re, os, json

base = r'd:\网站建设\网址导航\amzrover.cn\en'
segments = set()

for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith('.html'):
            continue
        fp = os.path.join(root, f)
        with open(fp, 'r', encoding='utf-8') as fh:
            content = fh.read()
        # Extract text content containing Chinese between tags
        for m in re.finditer(r'>([^<]*[\u4e00-\u9fff][^<]*)<', content):
            segments.add(m.group(1).strip())
        # Also meta content attributes
        for m in re.finditer(r'content="([^"]*[\u4e00-\u9fff][^"]*?)"', content):
            segments.add(m.group(1).strip())

segs = sorted(segments, key=len, reverse=True)
with open(r'd:\网站建设\网址导航\amzrover.cn\cn-segs.json', 'w', encoding='utf-8') as f:
    json.dump(segs, f, ensure_ascii=False, indent=1)
print(f'Unique segments: {len(segs)}')
