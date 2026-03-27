import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replacement ensuring we keep the exact HTML structure
old = '<h2 id="elite">8. Módulo Élite: Programmatic SEO controlado (escalabilidad B2B)</h2>'
new = '<h2 id="elite">8. Programmatic SEO (escalabilidad B2B)</h2>'

# Also check for menu link if needed (just in case)
content = content.replace(old, new)
content = content.replace('8. Módulo Élite', '8. Programmatic SEO') # For the menu if it was still old

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
