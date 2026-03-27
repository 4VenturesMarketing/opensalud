import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Capture Block 10 content and remove it
b10_start = text.find('<h2 id="articulos">10.')
if b10_start == -1:
    print("B10 start not found")
    exit(1)

# Find footer start to end B10 capture
footer_start = text.find('<footer', b10_start)
if footer_start == -1:
    footer_start = text.find('</body>', b10_start)

b10_content = text[b10_start:footer_start].strip()

# New text without B10 (temporarily) and without the broken footer line before it
text_clean = text[:b10_start].strip()

# Cleanup trailing broken part of text_clean
if text_clean.endswith('<footer'):
    text_clean = text_clean[:-7].strip()

# 2. Re-insert Block 10 right after Block 4
# Block 4 is: <h2 id="contenidos">4. Plan... </div>
step4_marker = '<h2 id="contenidos">4. Plan de contenidos b2b'
step4_start = text_clean.find(step4_marker)
step4_end = text_clean.find('</div>', step4_start) + 6

# Insert B10
text_final = text_clean[:step4_end] + "\n\n  " + b10_content + "\n" + text_clean[step4_end:]

# 3. Add footer back correctly
if not text_final.strip().endswith('</html>'):
    text_final = text_final.strip() + '\n\n</div>\n</section>\n\n<footer>\n  <p>© 2026 4Ventures · Informe Analítico de Posicionamiento</p>\n</footer>\n</body>\n</html>'

# 4. Final casing and formatting for h2
text_final = text_final.replace('10. Contenido de los 10 blogposts b2b', '10. Contenido de los 10 blogposts b2b')

# 5. Correct the double grid-2 and stray closures if any
text_final = text_final.replace('<div class="grid-2">\n    <div class="grid-2">', '<div class="grid-2">')
text_final = text_final.replace('<div class="grid-2">\n  <div class="grid-2">', '<div class="grid-2">')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text_final)

print("Success")
