import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix Block 1: Add <div class="grid-2"> after <h2 id="salud">...</h2>
pattern_b1 = r'(<h2 id="salud">1\. Índice de salud seo</h2>\s+)(<div class="card">.*?<h3.*?OpenSalud\.es.*?</h3.*?>)'
def repl_b1(m):
    return m.group(1) + '<div class="grid-2">\n    ' + m.group(2).lstrip()

text = re.sub(pattern_b1, repl_b1, text, flags=re.DOTALL)

# Block 1 already has a stray </div> at line 147 that now perfectly closes <div class="grid-2">!
# Wait, let's just make sure we close Block 2 correctly too.

# Fix Block 2: Add <div class="grid-2"> after <h2 id="hallazgos">...</h2>
pattern_b2 = r'(<h2 id="hallazgos">2\. Resumen de Hallazgos y Prioridades</h2>\s+)(<div class="card">.*?Oportunidades en opensalud\.es.*?</div>\s*<div class="card">.*?Barreras en menttum\.com.*?</div>)'
def repl_b2(m):
    return m.group(1) + '<div class="grid-2">\n  ' + m.group(2) + '\n  </div>'

text = re.sub(pattern_b2, repl_b2, text, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Success")
