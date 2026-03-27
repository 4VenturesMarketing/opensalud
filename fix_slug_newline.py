import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern is exactly:
# <h3 style="margin-top:0; color:var(--blue)">Artículo 1: Cómo realizar la evaluación de riesgos psicosociales (ley 31/1995) — slug: <code>ley-riesgos-psicosociales-empresa</code></h3>
# want:
# <h3 style="margin-top:0; color:var(--blue); margin-bottom: 5px;">Artículo 1: Cómo realizar la evaluación de riesgos psicosociales (ley 31/1995)</h3>
# <p style="color:var(--grey6); font-size:0.85rem; margin-bottom:15px;">slug: <code>ley-riesgos-psicosociales-empresa</code></p>

# Regex components
# <h3 style="margin-top:0; color:var(--blue)">(Artículo \d+:.*?) — slug: (<code>.*?</code>)</h3>
pattern = re.compile(r'<h3 style="margin-top:0; color:var(--blue)">(Artículo \d+:.*?) — slug: (<code>.*?</code>)</h3>')

def replace_with_separate_line(match):
    title = match.group(1).strip()
    slug_code = match.group(2).strip()
    return (
        f'<h3 style="margin-top:0; color:var(--blue); margin-bottom:5px;">{title}</h3>\n'
        f'    <p style="color:var(--grey6); font-size:0.85rem; margin-top:0; margin-bottom:12px;">slug: {slug_code}</p>'
    )

new_text = pattern.sub(replace_with_separate_line, text)

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Slug split to next line")
