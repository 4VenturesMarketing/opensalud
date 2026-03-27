import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Wrap index results in grid-2 (Block 1)
pattern_b1 = r'(<h2 id="salud">1\. Índice de salud seo</h2>.*?)(\s+<div class="card">.*?<h3.*?OpenSalud\.es.*?</h3.*?>\s+<p.*?>.*?</p>\s+<table>.*?</table>\s+</div>\s+<div class="card">.*?Menttum\.com.*?</h3.*?>\s+<p.*?>.*?</p>\s+<table>.*?</table>\s+</div>)'
def repl_b1(m):
    return m.group(1) + '\n    <div class="grid-2">' + m.group(2) + '\n    </div>'

text = re.sub(pattern_b1, repl_b1, text, flags=re.DOTALL)

# 2. Wrap opportunities/barriers in grid-2 (Block 2)
pattern_b2 = r'(<h2 id="hallazgos">2\. Resumen de Hallazgos y Prioridades</h2>.*?)(\s+<div class="card">\s+<h3.*?Oportunidades en opensalud\.es.*?</h3.*?>.*?</div>\s+<div class="card">\s+<h3.*?Barreras en menttum\.com.*?</h3.*?>.*?</div>)'
def repl_b2(m):
    return m.group(1) + '\n  <div class="grid-2">' + m.group(2) + '\n  </div>'

text = re.sub(pattern_b2, repl_b2, text, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Success")
