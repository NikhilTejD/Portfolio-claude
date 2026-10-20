import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
idx = (root/'index.html').read_text()
css = re.search(r'<style>(.*?)</style>', idx, re.S).group(1)
extra = (root/'_build/case-extra.css').read_text()
fonts = re.search(r'(<link rel="preconnect".*?display=swap">)', idx, re.S).group(1)
for name, title in [('mana-mitra','Mana Mitra Rollout'),('case-template','Case File Template')]:
    body = (root/f'_build/{name}.body.html').read_text()
    html = f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} · Nikhil Tej D</title>
{fonts}
<style>
:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}
body{{margin:0}} img{{max-width:100%}} [hidden]{{display:none!important}}
{css}
{extra}
</style>
</head><body>
{body}
</body></html>
'''
    (root/f'cases/{name}.html').write_text(html)
print('built')
