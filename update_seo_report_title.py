import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace in Navigation Menu
text = text.replace('2. Estrategia de cross-linking (el puente de autoridad)', '2. Estrategia de cross-linking')

# Replace in Body Content
text = text.replace('<h2>2. Estrategia de cross-linking (el puente de autoridad)</h2>', '<h2>2. Estrategia de cross-linking</h2>')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
