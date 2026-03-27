import re

path = '/Users/mfargas/Documents/4Ventures/00001-Atigravity/06.Andala/4venturesweb/opensalud/estrategia-seo.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Define boundaries for Block 10
# It starts at: <h2 id="articulos">10. Contenido...
# It ends just before: </div>\n</section>\n\n<footer>
pattern_b10 = r'(\s*<h2 id="articulos">10\..*?)(</div>\s*</section>\s*<footer>)'
match_b10 = re.search(pattern_b10, text, flags=re.DOTALL)
if not match_b10:
    print("Could not find block 10")
    exit(1)

b10_content = match_b10.group(1)
closing_part = match_b10.group(2)

# Remove block 10 from original position but keep the closing tags and footer
text = text[:match_b10.start()] + "\n" + closing_part

# Now find where to insert Block 10 (after Block 4 ends)
# Block 4 ends at </div> right before <h2 id="geo">6.
match_geo = re.search(r'(\n\s*<h2 id="geo">6\.)', text)
if not match_geo:
    print("Could not find block 6 to insert before")
    exit(1)

# Insert it
text = text[:match_geo.start()] + "\n\n" + b10_content + text[match_geo.start():]

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Success")
