import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Capture Block 6 content and remove it from its current position
# Block 6: <h2 id="geo">6. Estrategia... </div>
b6_marker = '<h2 id="geo">6. Estrategia global seo & geo: opensalud + menttum</h2>'
b6_start = text.find(b6_marker)
if b6_start == -1:
    print("B6 start not found")
    exit(1)

# End of Block 6 is usually before Block 7 or next h2
b6_end = text.find('<h2', b6_start + 10)
if b6_end == -1:
    b6_end = text.find('</div>\n</section>', b6_start)

b6_content = text[b6_start:b6_end].strip()

# New text without B6
text_no_6 = text[:b6_start] + text[b6_end:]

# 2. Re-insert after Block 5
# Block 5: <h2 id="articulos">5. Contenido...
# Need to find the REAL end of Block 5 (after all 10 blogpost cards)
# Block 5 ends before Block 6 (Wait, Block 6 is currently after all blogposts? Let me check)
# My previous capture removed B6. Let me find a better insertion point.

# Find Block 5's end. It contains 10 cards (#art1 to #art10). 
# Art 10 is the last one.
art10_marker = 'id="art10"'
art10_pos = text_no_6.find(art10_marker)
if art10_pos == -1:
    print("Art 10 not found")
    exit(1)

# Find the CLOSING of that card div.
art10_end = text_no_6.find('</details>\n  </div>', art10_pos) + 20

# Re-insert B6 after that
text_final = text_no_6[:art10_end] + "\n\n  " + b6_content + "\n\n" + text_no_6[art10_end:]

# 3. Ensure Step 5 title is correctly formatted (SENTENCE CASE - all but first word lower if requested previously)
# "En todos los títulos del documento, solo la letra de la primera palabra tiene que ser en mayúsculas" -> user rule from previous session.
text_final = text_final.replace('5. Contenido de los 10 blogposts b2b', '5. Contenido de los 10 blogposts b2b')
text_final = text_final.replace('6. Estrategia global seo & geo: opensalud + menttum', '6. Estrategia global seo & geo: opensalud + menttum')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text_final)

print("Success")
