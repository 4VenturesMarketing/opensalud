import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Current H3 structure: 
# <h3 style="margin-top:0; color:var(--blue)">Artículo X: TITLE — slug: <code>SLUG</code></h3>
# New structure wanted: 
# <h3 style="margin-top:0; color:var(--blue)">Artículo X: TITLE</h3>
# <p style="color:var(--grey6); margin-top:-10px; margin-bottom:15px; font-size:0.9rem">slug: <code>SLUG</code></p>

pattern = re.compile(r'<h3 style="margin-top:0; color:var(--blue)">(Artículo \d+:.*?) — slug: (<code>.*?</code>)</h3>')

def replace_with_newline(match):
    title = match.group(1)
    slug = match.group(2)
    return f'<h3 style="margin-top:0; color:var(--blue); margin-bottom:5px;">{title}</h3>\n    <p style="color:var(--grey6); font-size:0.9rem; margin-bottom:15px;">slug: {slug}</p>'

new_text = pattern.sub(replace_with_newline, text)

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Slugs moved under titles successfully")
